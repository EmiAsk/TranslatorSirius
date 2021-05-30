import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QEvent
import pyperclip

from config import POSSIBLE_LANGS
from functions import translate
from untitled import Ui_MainWindow

import pyttsx3


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class TranslatorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(TranslatorWindow, self).__init__()
        super(TranslatorWindow, self).setupUi(self)
        # loadUi('untitled.ui', self)
        self.initUi()

    def initUi(self):
        self.setWindowIcon(QIcon('images/icon.ico'))
        to_combo_box = list(map(str.title, POSSIBLE_LANGS.keys()))

        self.lang_to.addItems(to_combo_box)
        self.lang_to.setCurrentText('English')

        self.lang_from.addItems(to_combo_box)
        self.lang_from.setCurrentText('Russian')

        self.btn_translate.clicked.connect(self.translate)
        self.btn_copy.clicked.connect(self.copy_translated_text)
        self.btn_play_over.clicked.connect(self.play_voice_over)

        self.lang_to.currentTextChanged.connect(self.translate)
        # self.lang_from.currentTextChanged.connect(self.translate)

        self.text_from.installEventFilter(self)

    def eventFilter(self, source, event: QEvent) -> bool:
        if source is self.text_from and event.type() == QEvent.KeyPress and \
                event.modifiers() == Qt.NoModifier and event.key() == Qt.Key_Return:
            self.translate()
            return True
        return super(TranslatorWindow, self).eventFilter(source, event)

    def get_lang_pair(self):
        lang_to = self.lang_to.currentText()
        code_lang_to = POSSIBLE_LANGS[lang_to.lower()]

        lang_from = self.lang_from.currentText()
        code_lang_from = POSSIBLE_LANGS[lang_from.lower()]

        return code_lang_from, code_lang_to

    def translate(self):
        self.clear_status_bar()
        trans_text = self.text_from.toPlainText()

        try:
            result_text = translate(trans_text, *self.get_lang_pair())
            self.text_to.setText(result_text)
        except Exception as er:
            print(er)
            self.show_status_message(er.__str__())

    def copy_translated_text(self):
        text_to_copy = self.text_to.toPlainText()
        pyperclip.copy(text_to_copy)

        self.show_status_message('Текст успешно скопирован', 'green')

    def play_voice_over(self):
        engine = pyttsx3.init()  # инициализация движка
        voices = engine.getProperty('voices')
        if self.lang_to.currentText().lower() == 'russian':
            engine.setProperty('voice', voices[0].id)
        elif self.lang_to.currentText().lower() == 'english':
            engine.setProperty('voice', voices[1].id)

        # зададим свойства
        engine.setProperty('rate', 200)  # скорость речи
        engine.setProperty('volume', 1)  # громкость (0-1)

        text = self.text_to.toPlainText()

        engine.say(text)  # запись фразы в очередь

        # очистка очереди и воспроизведение текста
        engine.runAndWait()

    def show_status_message(self, text, color='red'):
        self.statusBar().showMessage(text)
        self.statusBar().setStyleSheet(f'background-color:'
                                       f'{color}; color: white; font-size: 14pt;')

    def clear_status_bar(self):
        self.statusBar().showMessage('')
        self.statusBar().setStyleSheet('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    wind = TranslatorWindow()
    wind.show()
    sys.exit(app.exec())
