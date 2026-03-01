import math

class EcuacionCuadratica:
    
    def __init__(self, a, b, c):
        # Atributos privados
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return self.__b**2 - 4*self.__a*self.__c

    def getRaiz1(self):
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return 0
        return (-self.__b + math.sqrt(discriminante)) / (2*self.__a)

    def getRaiz2(self):
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return 0
        return (-self.__b - math.sqrt(discriminante)) / (2*self.__a)

print("Ingrese a, b, c separados por espacios:")
a, b, c = map(float, input().split())

ecuacion = EcuacionCuadratica(a, b, c)

discriminante = ecuacion.getDiscriminante()

if discriminante > 0:
    print("La ecuación tiene dos raíces",
          round(ecuacion.getRaiz1(), 5),
          "y",
          round(ecuacion.getRaiz2(), 5))

elif discriminante == 0:
    print("La ecuación tiene una raíz",
          round(ecuacion.getRaiz1(), 5))

else:
    print("La ecuación no tiene raíces reales")