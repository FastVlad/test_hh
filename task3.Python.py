def largest_number(nums: list) -> str:
    """
    Функция сортировки через lambda и склеивание строки
    :param nums: принимает целое число
    :return: возвращает строку
    """
    sorted_nums = sorted(nums, key=lambda x: x * 3, reverse=True)
    result = ''.join(sorted_nums)
    result = result.lstrip('0')

    return result if result else '0'


input_strings = ['11', '234', '005', '89']
max_number = largest_number(input_strings)
print(f"Максимальное число: {max_number}")
