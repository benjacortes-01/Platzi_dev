def capicua(string):
    try:
        if len(string) == 0:
            raise ValueError('No se puede colocar un string empty')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(capicua(''))
except TypeError:
    print('Se permiten str unicamente')
