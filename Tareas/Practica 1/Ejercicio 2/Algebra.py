class EcuacionLineal:
    
    def __init__(self, a, b, c, d, e, f):
        # Atributos privados
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0

    def getX(self):
        determinante = self.__a * self.__d - self.__b * self.__c
        return (self.__e * self.__d - self.__b * self.__f) / determinante

    def getY(self):
        determinante = self.__a * self.__d - self.__b * self.__c
        return (self.__a * self.__f - self.__e * self.__c) / determinante

print("Ingrese a, b, c, d, e, f separados por espacios:")
a, b, c, d, e, f = map(float, input().split())

ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tieneSolucion():
    print("x =", ecuacion.getX())
    print("y =", ecuacion.getY())
else:
    print("La ecuación no tiene solución")