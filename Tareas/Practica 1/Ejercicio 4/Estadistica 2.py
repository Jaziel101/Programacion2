import math

class Estadistica:
    
    def __init__(self, datos):
        self.__datos = datos

    def promedio(self):
        return sum(self.__datos) / len(self.__datos)

    def desviacion(self):
        prom = self.promedio()
        suma = 0
        for x in self.__datos:
            suma += (x - prom) ** 2
        return math.sqrt(suma / (len(self.__datos) - 1))

print("Ingrese 10 números separados por espacios:")
numeros = list(map(float, input().split()))

estad = Estadistica(numeros)

print("El promedio es", round(estad.promedio(), 2))
print("La desviación estándar es", round(estad.desviacion(), 5))

#Las ventajas de usar POO son: el encapsulamiento de los datos, el código más organizado, la fácil reutilización, el mejor mantenimiento y permitir extender la clase.