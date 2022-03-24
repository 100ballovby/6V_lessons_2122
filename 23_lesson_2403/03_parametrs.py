def power(n, p=2):
    """
    Функция возводит одно число в степень другого
    :param n: число
    :param p: степень
    :return: int: результат
    """
    res = 1
    for i in range(p):
        res *= n
    return res

print(power(2, 7))  # 128  p=7
print(power(7, 2))  # 49  p=2
print(power(3))  # p=2


