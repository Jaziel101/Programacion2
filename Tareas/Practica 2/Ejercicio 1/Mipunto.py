import math

class MiPunto:
    def __init__(self, x=0.0, y=0.0):
        #Atributos privados
        self.__x = x
        self.__y = y
    #Getters
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def distancia(self, *args):
        if len(args) == 1 and isinstance(args[0], MiPunto):
            otro = args[0]
            dx = self.__x - otro.get_x()
            dy = self.__y - otro.get_y()
            return math.sqrt(dx**2 + dy**2)
        elif len(args) == 2:
            x, y = args
            dx = self.__x - x
            dy = self.__y - y
            return math.sqrt(dx**2 + dy**2)
        else:
            raise TypeError("Argumentos inválidos")
    def __str__(self):
        return f"({self.__x}, {self.__y})"

if __name__ == "__main__":
    punto1 = MiPunto()           
    punto2 = MiPunto(10, 30.5)   
    
    distancia1 = punto1.distancia(punto2)
    print(f"Distancia entre {punto1} y {punto2}: {distancia1:.2f}")
    
    distancia2 = punto1.distancia(10, 30.5)
    print(f"Distancia desde (0,0) hasta (10, 30.5): {distancia2:.2f}")
    
    distancia3 = punto2.distancia(0, 0)
    print(f"Distancia desde {punto2} hasta el origen: {distancia3:.2f}")