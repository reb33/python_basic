# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce


def main():
    even_list = [el for el in range(100, 1001) if el % 2 == 0]
    res = reduce(lambda x,y: x*y, even_list)
    print(res)


if __name__ == '__main__':
    main()