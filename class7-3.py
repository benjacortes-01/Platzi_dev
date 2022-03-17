def suma(a,b):
    return a + b

print(suma(10,15))

lis_pares = []

def lista_pares(start,stop):
    for i in range(start,stop):
        if i % 2 == 0:
            lis_pares.append(i)
    return lis_pares

print(f'Los elementos pares de la lista son\n{lista_pares(0,25)}')
