from random import randint

'''
1. Среднее
Дано: 3 случайных числа.

Задание: написать программу, которая будет вычислять среднее значение этих чисел.

Пример: (52 + 56 + 60) / 3 = 56
'''


def rand_mean(): return (randint(0, 100) +
                         randint(0, 100) +
                         randint(0, 100)) \
                         / 3


'''
2. Деление и еще раз деление
Дано: 2 случайных числа.

Задание: написать программу, которая будет печать результат целочисленного деления этих чисел, а также остаток от деления первого от второго.

Пример:

 x = 177 и y = 10

Результат:
 17, 7
'''


def division():
    x = randint(100, 200)
    y = randint(11, 80)
    print(f"x = {x}\ny = {y}")
    print(f"x // y = {x // y}")
    print(f"x % y = {x % y}")


'''
3. Округление
Дано: число с плавающей точкой.

Задание: написать программу, которая будет округлять заданное число:

1) 2х знаков после запятой; 2) до целого; 3) дополнять слева столько нулей, сколько не хватает числу до 11 знаков.

Пример:

x = 14.721

1) 14.72

2) 15

3) 0000014.721
'''


def rounding(num: float):
    print("Rounding to two decimal places: ", round(num, 2))
    print("Rounding to integer: ", round(num))
    print("Zero filling up to 11 signs: {0:011}".format(num))


def main():
    print("Average of three random ints:", rand_mean())

    division()

    num = float(input("Please enter any float number: "))
    rounding(num)


if __name__ == '__main__':
    main()
