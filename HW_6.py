# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

from ast import Return


def es_primo(num , n = 2): 
    if n >= num: 
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        return False 

# print(es_primo())

# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

lista = [1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6]

# def lista_primos(start = int(input('Starts on: ')) ,stop = int(input('ends on: '))):
    
#     for e in range(start,stop):
#         if es_primo(e):
#             lista.append(e)

#     return lista

# print(f'\n{lista_primos()}')


# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

#### RESOLVIENDO CON DICCIONARIO USANDO EL ELEMENTO COMO LLAVE
# def num_moda(lista):
#     counts = {'Elementos' : []}
#     repetidos = {'Repetidos' : 0}
#     for e in lista:
#         if e not in counts['Elementos']:
#             counts['Elementos'].append(e)
#         elif e in repetidos:
#             repetidos[e] += 1
#     return print(counts['Elementos'], repetidos['Repetidos'])

# print(num_moda(lista))

# def valor_modal(lista):
    # '''
    # La def toma como parametro una lista de numeros
    # Crea una lista de elementos unicos y una lista de elementos repetidos
    # '''
    # lista_unicos = []
    # lista_repeticiones = []
    # if len(lista) == 0:
    #     return None
    # for elemento in lista:
    #     if elemento in lista_unicos:
    #         i = lista_unicos.index(elemento)
    #         lista_repeticiones[i] += 1
    #     else:
    #         lista_unicos.append(elemento)
    #         lista_repeticiones.append(1)
    # moda = lista_unicos[0]
    # maximo = lista_repeticiones[0]
    # for i, elemento in enumerate(lista_unicos):
    #     if lista_repeticiones[i] > maximo:
    #         moda = lista_unicos[i]
    #         maximo = lista_repeticiones[i]
    # return moda, maximo

# print(valor_modal(lista))

# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.

# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F
# Fórmula 2	: °C + 273.15 = °K
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino

# def Calc_grados(start =int (input('Que grados tenes?\n[1] Celsius\n[2] Farenheit\n[3] Kelvin\n\n-->')),end = int(input('A que lo queres pasar?\n[1] Celsius\n[2] Farenheit\n[3] Kelvin\n\n-->')) ,cel = int(input('cuantos grados?: '))):
#     '''
#     Esta herramienta permite pasar de un grado a otro
#     '''
#     if start == 1 :
#         start = 'Celsius'
#     elif start == 2:
#         start = 'Farenheit'
#     elif start == 3:
#         start = 'Kelvin'
#     else:
#         print('You can only can chose [1,2,3]')
#         start 

#     if end == 1 :
#         end = 'Celsius'
#     elif end == 2:
#         end = 'Farenheit'
#     elif end == 3:
#         end = 'Kelvin'
#     else:
#         print('You can only can chose [1,2,3]')

#     ##Formulas
#     if start == 'Celsius':

#         if end == 'Farenheit':
#             Far = (cel * 9/5) + 32
#             return print(Far)
    
#         if end == 'Kelvin':
#             Kel = cel + 273.15
#             return print(Kel)

#         if end == 'Celsius':
#             return print(cel)
    
#     elif start == 'Farenheit':
#         ## de Far a Cel
#         cel = (cel - 32 ) * 5/9
#         start = 1
#         if end == 'Celsius':
#             end = 1
#         elif end == 'Kelvin':
#             end = 3
#         else:
#             end = 2
#         Calc_grados(start,end,cel)

#     elif start == 'Kelvin':
#         ## de Kel a Cel
#         cel = cel - 273.15
#         start = 1
#         if end == 'Celsius':
#             end = 1
#         elif end == 'Farenheit':
#             end = 2
#         else:
#             end = 3
#         Calc_grados(start,end,cel)

# Calc_grados()

# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# 7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

def factorial(n = int(input('Choose a num: '))):
    assert n != int, 'You can only put int'
    assert n > 0, 'You can only put possitives'
    if n > 1:
        n = n * factorial(n - 1)
    return n

print(factorial())