import math

class PoligonoRegular:

    def __init__(self, n=3, lado=1, x=0, y=0):
        self.n = n
        self.lado = lado
        self.x = x
        self.y = y

    def getPerimetro(self):
        return self.n * self.lado

    def getArea(self):
        return (self.n * self.lado ** 2) / (4 * math.tan(math.pi / self.n))


# Programa de prueba
def mostrar_datos(p):
    print("Número de lados:", p.n)
    print("Perímetro:", p.getPerimetro())
    print("Área:", p.getArea())
    print("-------------------------")

p1 = PoligonoRegular()
p2 = PoligonoRegular(6, 4)
p3 = PoligonoRegular(10, 4, 5.6, 7.8)

mostrar_datos(p1)
mostrar_datos(p2)
mostrar_datos(p3)