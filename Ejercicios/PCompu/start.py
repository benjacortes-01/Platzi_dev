import time

obj = time.localtime()
print(obj)
t = time.asctime(obj)
print(t)

def reloj(hora,mins,seg):
    while seg < 61:
        seg += 1

        if seg == 60:
            mins +=1
            seg = 0

        if mins == 60:
            hora += 1
            mins = 0
        time.sleep(0.2)
    return (seg,mins,hora)

def factorial (n):
    '''
    Calcula el factorial de n
    n int > 0
    returns n!
    '''
    if n > 1:
        return 1
    return n * factorial(n - 1)

n = int(input('Elige un numero: '))

print(factorial(n))