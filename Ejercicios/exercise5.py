import numbers

from numpy import number


def read():
    numbers = []
    with open('./numeros.txt','r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
            numbers.sort()
    print(numbers)

def write():
    names = ['Juan','Rudiberto']
    with open('./nombres.txt','w', encoding='utf-8') as f: 

    #a sobreescribe \\ w sobreescribe

        for name in names:
            f.write(name)
            f.write('\n')
    print(names)

def run():
    read()
    write()

if __name__ == '__main__':
    run() 