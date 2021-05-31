from config import API_KEY, POSSIBLE_LANGS, API_URL
from requests import get


def translate(text, lang_to, lang_from):
    if lang_from not in POSSIBLE_LANGS.values() and lang_to not in POSSIBLE_LANGS.values():
        raise Exception('Таких языков / языка не существует')

    params = {"key": API_KEY,
              "text": text if text else ' ',
              "lang": '-'.join([lang_to, lang_from])}

    response = get(API_URL, params=params)

    if not response.__bool__():
        if response.json()['code'] == 501:
            raise Exception('Неподдерживаемая языковая пара! Смените её!')

        print("Ошибка выполнения запроса:")
        print(response.url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        raise Exception('Ошибка выполнения запроса!')

    try:
        result_text = response.json()['text'][0]
    except Exception:
        raise Exception('Что-то пошло не так...')

    return result_text