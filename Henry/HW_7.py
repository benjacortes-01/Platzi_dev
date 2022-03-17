## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

class vehiculo:

    def __init__(self,vehiculo,color,cilindradas):
        self.vehiculo = vehiculo
        self.col = color
        self.cil = cilindradas

    def acelerar(self,aceleracion):
        a = 0
        return print (a + aceleracion)

    def frenar(self,freno):
        v = 0
        return v

    def status(self):
        print(f'La aceleracion es {self.acelerar}')
    
    def doblar(self,direccion):
        direccion = int(input('Derecha [1] o Izquierda [2]?: '))
        if direccion == 1:
            direccion += 90
        elif direccion == 2:
            direccion -= 90
        return direccion

    def caracterisitas(self):
        print(f'Es un/a {self.vehiculo} de color {self.col} de {self.cil} cilindradas')
        
A1 = vehiculo('auto','rojo',750)
M1 = vehiculo('moto','azul',150)


A1.caracterisitas()
M1.caracterisitas()

A1.acelerar(40)
A1.acelerar(60)

A1.status()


# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>



# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# 6) Probar las funciones incorporadas en la clase del punto 5

# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones
