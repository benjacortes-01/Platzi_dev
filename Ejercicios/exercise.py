from msilib.schema import Error
from os import strerror


def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def run():
    try:
        num = int(input('Ingresar un numero: '))
        if num < 0:
            raise ValueError()
    except ValueError as ve:
        print(f'{ve}Warning\nChoose only possitive interger')
        print()
        return run()

    try:
        num = int(input('Ingresar un numero: '))
        if num == str:
            raise ValueError()
    except ValueError as stre:
        print(f'{stre}Warning\nChoose only interger')
        print()
        return run()

    else:
        print('\nExcelente funciono!')
        print(divisor(num))


if __name__ == '__main__':
    run()