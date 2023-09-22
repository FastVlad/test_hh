import re


def nice_number(text: str) -> str:
    """
    Функция с регулярным выражением, которая ищет хорошее цисло
    :param text: принимает строку
    :return result: возвращает сторку
    """
    r = r'(\d{2,4})\\(\d{2,5})'
    match = re.search(r, text)
    if not match.group():
        return 'Некорректный запрос'
    parts = match.group().split('\\')
    expected_length_first = 4
    expected_length_second = 5
    filled_first = parts[0].zfill(expected_length_first)
    filled_second = parts[1].zfill(expected_length_second)
    result = f"{filled_first}\\{filled_second}"
    return result


user_text = input('Введите строку: ')

print(nice_number(user_text))
