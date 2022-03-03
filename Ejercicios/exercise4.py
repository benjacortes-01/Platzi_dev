def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def run():
    
    num = input('Ingresar un numero: ')
    assert num.isnumeric(), 'Only intenger' ##Si es numero continua
    assert int(num) > 0, 'Only intengers'

    print('\nExcelente funciono!')
    print(divisor(int(num)))

if __name__ == '__main__':
    run() 