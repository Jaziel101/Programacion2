import math

class Vector3D:
    #Constructor
    def __init__(self, x=0.0, y=0.0, z=0.0):
        #Atribuutos publicos
        self.x = x
        self.y = y
        self.z = z
    #Sobrecarga de operadores
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Operación no soportada")
    def __rmul__(self, other):
        return self.__mul__(other)
    def __xor__(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def normalizar(self):
        n = abs(self)
        if n == 0:
            raise ValueError("No se puede normalizar el vector nulo.")
        return Vector3D(self.x / n, self.y / n, self.z / n)
    @staticmethod
    def perpendicular(a, b, metodo=1):
        if metodo == 1:
            return abs(abs(a + b) - abs(a - b)) < 1e-10
        elif metodo == 2:
            return True   
        elif metodo == 3:
            return abs(a * b) < 1e-10
        elif metodo == 4:
            return abs(abs(a + b) ** 2 - (abs(a) ** 2 + abs(b) ** 2)) < 1e-10
        else:
            raise ValueError("Método debe ser 1, 2, 3 o 4.")
    @staticmethod
    def paralelo(a, b, metodo=1):
        if metodo == 1:
            if abs(b) < 1e-10:
                return abs(a) < 1e-10   
            if abs(b.x) > 1e-10:
                r = a.x / b.x
                return (abs(a.y - r * b.y) < 1e-10 and
                        abs(a.z - r * b.z) < 1e-10)
            elif abs(b.y) > 1e-10:
                r = a.y / b.y
                return (abs(a.x - r * b.x) < 1e-10 and
                        abs(a.z - r * b.z) < 1e-10)
            elif abs(b.z) > 1e-10:
                r = a.z / b.z
                return (abs(a.x - r * b.x) < 1e-10 and
                        abs(a.y - r * b.y) < 1e-10)
            return False
        elif metodo == 2:
            cruz = a ^ b
            return (abs(cruz.x) < 1e-10 and
                    abs(cruz.y) < 1e-10 and
                    abs(cruz.z) < 1e-10)
        else:
            raise ValueError("Método debe ser 1 o 2.")
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
    a = Vector3D(3, 4, 0)      
    b = Vector3D(4, -3, 0)     
    c = Vector3D(6, 8, 0)      
    print("Los vectores son:")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}\n")
    print("La perpendicularidad (a con b) es:")
    print(f"Método 1 (|a+b| == |a-b|) : {Vector3D.perpendicular(a, b, 1)}")
    print(f"Método 2 (|a-b| == |b-a|) : {Vector3D.perpendicular(a, b, 2)}")
    print(f"Método 3 (a·b == 0)       : {Vector3D.perpendicular(a, b, 3)}")
    print(f"Método 4 (|a+b|² == |a|²+|b|²) : {Vector3D.perpendicular(a, b, 4)}")
    print(f"a con c (paralelo)         : {Vector3D.perpendicular(a, c, 3)}\n")
    print("El paralelismo (a con c) es: ")
    print(f"Método 1 (a = r·c) : {Vector3D.paralelo(a, c, 1)}")
    print(f"Método 2 (a×c = 0) : {Vector3D.paralelo(a, c, 2)}")
    print(f"a con b (no paralelo): {Vector3D.paralelo(a, b, 2)}\n")
    print("La o las proyecciones y el o los componentes son: ")
    proy = Vector3D.proyeccion(a, b)
    comp = Vector3D.componente(a, b)
    print(f"Proyección de a sobre b   : {proy}")
    print(f"Componente de a en b      : {comp:.4f}\n")
    print("Otras operaciones son: ")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"3 * a = {3 * a}")
    print(f"a · b = {a * b}")
    print(f"a × b = {a ^ b}")
    print(f"|a|   = {abs(a):.4f}")
    print(f"a normalizado = {a.normalizar()}")