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


'''
[Junior] 4. Число "наоборот"
Дано: целое число (int).

Задание: написать программу, которая будет инвертировать целое число

Пример:

1) x = 123 -> 321 2) x = -325 -> -523 3) x = 0 -> 0
'''


def reverse_int(num: int):
    reversed = 0
    negative = False

    if num < 0:
        num *= -1
        negative = True

    while num != 0:
        reversed = reversed * 10 + num % 10
        num //= 10

    if negative:
        reversed *= -1

    return reversed


'''
[Junior+] 5. Число "наоборот" (усложненное)
Дано: целое число (int).

Задание: написать программу, которая будет инвертировать целое число. Если инвертированное число выходит за границы (32-bit integer)

Пример:

1) x = 123 -> 321 2) x = -325 -> -523 3) x = 0 -> 0 4) x = 1563847412 -> 0
'''


def reverse_int32(num: int):
    MAX_INT32 = 2147483647
    _num = reverse_int(num)

    if abs(_num) > MAX_INT32:
        return 0
    else:
        return  _num


def main():
    print("Average of three random ints:", rand_mean())

    division()

    num = float(input("Please enter any float number: "))
    rounding(num)

    num = int(input("Please enter any number: "))
    print("Reversed number: ", reverse_int(num))

    num = int(input("Please enter any 32bit-number: "))
    print("Reversed number: ", reverse_int32(num))


if __name__ == '__main__':
    main()
