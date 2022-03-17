for i in range(0,101,2**4):
    print(i)
print('\n')

lista = [1,2,3,4,5,6,7,8,9]
for x in range(len(lista)):
    print(lista[x])
print('\n')

print('Print de la lista con enumerate sin formato')
for n in enumerate(lista):
    print(n)
print('\n')

print('formato con .format')
for valor,posicion in enumerate(lista):
    print('El valor {0} esta en la posicion {1}'.format(posicion,valor))
    #El 0 hace ref al 1er parametro el 1 al 2do
print('\n')

print('formato con f""')
for posicion,valor in enumerate(lista):
    print(f'El valor {valor} esta en la posicion {posicion}')