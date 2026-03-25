import math

class AlgebraVectorial:
    # Constructores
    def __init__(self, x=0.0, y=0.0, z=0.0):
        #Atributos privados
        self.__x = x
        self.__y = y
        self.__z = z
    # Getters
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_z(self):
        return self.__z
    # Sobrecarga de operadores
    def __add__(self, v):
        return AlgebraVectorial(self.__x + v.get_x(), 
                                self.__y + v.get_y(), 
                                self.__z + v.get_z())
    def __sub__(self, v):
        return AlgebraVectorial(self.__x - v.get_x(), 
                                self.__y - v.get_y(), 
                                self.__z - v.get_z())
    def __mul__(self, other):
        if isinstance(other, AlgebraVectorial):
            return (self.__x * other.get_x() + 
                    self.__y * other.get_y() + 
                    self.__z * other.get_z())
        elif isinstance(other, (int, float)):
            return AlgebraVectorial(self.__x * other, 
                                    self.__y * other, 
                                    self.__z * other)
        else:
            raise TypeError("Operación no soportada")
    def __xor__(self, v):
        return AlgebraVectorial(
            self.__y * v.get_z() - self.__z * v.get_y(),
            self.__z * v.get_x() - self.__x * v.get_z(),
            self.__x * v.get_y() - self.__y * v.get_x()
        )
    def __abs__(self):
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)
    def __rmul__(self, k):
        return self.__mul__(k)
    def __str__(self):
        return f"({self.__x}, {self.__y}, {self.__z})"
    @staticmethod
    def perpendicular(a, b, metodo=1):
        if metodo == 1:
            return abs(abs(a + b) - abs(a - b)) < 1e-10
        elif metodo == 2:
            return True
        elif metodo == 3:
            return abs(a * b) < 1e-10 
        elif metodo == 4:
            return abs(abs(a + b)**2 - (abs(a)**2 + abs(b)**2)) < 1e-10
        else:
            raise ValueError("Método no válido. Usar 1, 2, 3 o 4.")
    @staticmethod
    def paralelo(a, b, metodo=1):
        if metodo == 1:
            if abs(b) < 1e-10:
                return abs(a) < 1e-10  
            r = a.get_x() / b.get_x() if abs(b.get_x()) > 1e-10 else None
            if r is not None:
                return (abs(a.get_y() - r * b.get_y()) < 1e-10 and 
                        abs(a.get_z() - r * b.get_z()) < 1e-10)
            r = a.get_y() / b.get_y() if abs(b.get_y()) > 1e-10 else None
            if r is not None:
                return (abs(a.get_x() - r * b.get_x()) < 1e-10 and 
                        abs(a.get_z() - r * b.get_z()) < 1e-10)
            r = a.get_z() / b.get_z() if abs(b.get_z()) > 1e-10 else None
            if r is not None:
                return (abs(a.get_x() - r * b.get_x()) < 1e-10 and 
                        abs(a.get_y() - r * b.get_y()) < 1e-10)
            return False
        elif metodo == 2:
            cruz = a ^ b
            return (abs(cruz.get_x()) < 1e-10 and 
                    abs(cruz.get_y()) < 1e-10 and 
                    abs(cruz.get_z()) < 1e-10)
        else:
            raise ValueError("Método no válido. Usar 1 o 2.")
    @staticmethod
    def proyeccion(a, b):
        if abs(b) < 1e-10:
            raise ValueError("No se puede proyectar sobre el vector nulo.")
        factor = (a * b) / (abs(b) ** 2)
        return b * factor
    @staticmethod
    def componente(a, b):
        if abs(b) < 1e-10:
            raise ValueError("No se puede calcular componente sobre vector nulo.")
        return (a * b) / abs(b)

if __name__ == "__main__":
    a = AlgebraVectorial(3, 4, 0)
    b = AlgebraVectorial(4, -3, 0)
    c = AlgebraVectorial(6, 8, 0)
    print("Los vectores son:")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print()
    print("La perpendicularidad es:")
    print(f"a y b: método 1 (|a+b| = |a-b|): {AlgebraVectorial.perpendicular(a, b, 1)}")
    print(f"a y b: método 3 (a·b = 0): {AlgebraVectorial.perpendicular(a, b, 3)}")
    print(f"a y c: método 4 (|a+c|² = |a|² + |c|²): {AlgebraVectorial.perpendicular(a, c, 4)}")
    print()
    print("El paralelismo es:")
    print(f"a y c: método 1 (a = r·c): {AlgebraVectorial.paralelo(a, c, 1)}")
    print(f"a y c: método 2 (a×c = 0): {AlgebraVectorial.paralelo(a, c, 2)}")
    print(f"a y b: método 2: {AlgebraVectorial.paralelo(a, b, 2)}")
    print()
    print("La proyeccion es:")
    proy = AlgebraVectorial.proyeccion(a, b)
    print(f"Proyección de a sobre b: {proy}")
    print()
    print("La componente es:")
    comp = AlgebraVectorial.componente(a, b)
    print(f"Componente de a en b: {comp:.4f}")
    print()
    print("Resultados:")
    print(f"Producto punto a·b = {a * b}")
    print(f"Producto cruz a × b = {a ^ b}")
    print(f"Módulo de a: {abs(a):.4f}")
    print(f"Módulo de b: {abs(b):.4f}")