from gtts import gTTS
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, ConversationHandler
from telegram.ext import Updater

import os

from config import POSSIBLE_LANGS, TOKEN
from functions import translate


# @translatorsiriusbot - БОТ


def give_help(update, context):
    update.message.reply_text("Доступные команды:\n\n1) Выбрать пару языков командой "
                              "/set_lang [код ISO языка текста] "
                              "[код ISO языка перевода]\n2) Перевести текст командой "
                              "/text [текст]\n3) Получить "
                              "озвучку перевода командой /voice [текст]!\n4) "
                              "/languages - получить список поддерживаемых ботом языков"
                              "\n\nПо умолчанию стоит перевод с русского на английский (ru-en)"
                              )


def get_supported_langs(update, context):
    langs = '\n'.join([f'{k.title()} - {v}' for k, v in POSSIBLE_LANGS.items()])
    update.message.reply_text('Cписок поддерживаемых ботом языков:\n\n' + langs)


def start(update, context):
    context.user_data['lang'] = ('ru', 'en')
    update.message.reply_text(
        "Привет! Я бот-переводчик. Вы можете:\n\n"
        "1) /set_lang [код ISO языка текста] "
        "[код ISO языка перевода] - выбрать пару языков командой \n"
        "2) /text [текст] - Перевести текст командой \n3) /voice [текст] - получить "
        "озвучку перевода командой\n4) /languages - получить список поддерживаемых ботом языков"
        "\n\nПо умолчанию стоит перевод с русского на английский (ru-en)")

    return 1


def stop(update, context):
    update.message.reply_text("Всего доброго!",
                              reply_markup=ReplyKeyboardMarkup([['/start']],
                                                               one_time_keyboard=True))
    return ConversationHandler.END


def switch_lang(update, context):
    if len(context.args) != 2:
        update.message.reply_text(
            "Неверное кол-во языков! Должно быть ровно 2.")
        return

    from_lang, to_lang = context.args

    if from_lang not in POSSIBLE_LANGS.values() or to_lang not in POSSIBLE_LANGS.values():
        update.message.reply_text(
            "Неподдерживаемые или несуществующие языки!")
        return

    context.user_data['lang'] = (from_lang, to_lang)
    update.message.reply_text("Вы сменили языковую пару! Можете переводить командой /text "
                              "или озвучивать /voice ")


def translate_text(update, context):
    text_to_trans = context.args

    if not text_to_trans:
        update.message.reply_text("Вы не написали текст!")
        return
    text_to_trans = update.message.text[6:]

    try:
        result_text = translate(text_to_trans, *context.user_data['lang'])
        update.message.reply_text(result_text + '\n\n\n' +
                                  "Текст успешно переведен!")
    except Exception as er:
        print(er)
        update.message.reply_text(er.__str__())


def voice_over(update, context):
    text_to_voice = context.args

    if not text_to_voice:
        update.message.reply_text("Вы не написали текст!")
        return
    text_to_voice = ' '.join(context.args).strip()[:100]

    try:
        result_text = translate(text_to_voice, *context.user_data['lang'])
        path_to_voice = 'voices/voice.mp3'
        tts = gTTS(result_text, lang=context.user_data['lang'][1])
        tts.save(path_to_voice)

        context.bot.send_voice(update.message.chat_id, open(path_to_voice, mode='rb'),
                               caption='Перевод успешно озвучен!')

        os.remove(path_to_voice)
    except ValueError:
        update.message.reply_text('Такой язык озвучки не поддерживается!')
        print('Такой язык озвучки не поддерживается!')
    except Exception as er:
        print(er)
        update.message.reply_text(er.__str__())


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        1: [CommandHandler('set_lang', switch_lang), CommandHandler('help', give_help),
            CommandHandler('stop', stop), CommandHandler('text', translate_text),
            CommandHandler('voice', voice_over), CommandHandler('languages', get_supported_langs)]

    },
    fallbacks=[CommandHandler('stop', stop)]
    # Точка прерывания диалога. В данном случае — команда /stop.

)

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher

dp.add_handler(conv_handler)

updater.start_polling()

updater.idle()
