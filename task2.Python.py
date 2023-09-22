import heapq


def new_distance(k: int, L: list) -> list:
    """
    Функция находит максимальное расстояние
    :param k: принимает целое число
    :param L: принимает список расстояний банкоматов
    :return: возвращает готовый список расстояний
    """
    max_distance = heapq.nlargest(k, L)
    for i in max_distance:
        index = L.index(i)
        L[index] = i // 2
        L.insert(index + 1, i // 2)
    return L


total_ATMs, how_much_to_build = map(int, input(
    "Введите кол-во банкоматов которые стоят на дороге и сколько нужно поставить (через пробел): "
    ).split())

l = []

print('Введите расстояние между банкоматами: ')
for _ in range(total_ATMs):
    distance = int(input())
    l.append(distance)


for new_d in new_distance(how_much_to_build, l):
    print(new_d)




