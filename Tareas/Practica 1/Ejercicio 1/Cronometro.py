import time
import random

#---------------------------------------------------
def seleccion_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
#---------------------------------------------------

class Cronometro:
    
    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = None

    def get_inicia(self):
        return self.__inicia

    def get_finaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = time.time()
        self.__finaliza = None

    def detener(self):
        self.__finaliza = time.time()

    def lapsoDeTiempo(self):
        if self.__finaliza is None:
            return (time.time() - self.__inicia) * 1000
        return (self.__finaliza - self.__inicia) * 1000


numeros = [random.randint(1, 1000000) for _ in range(100000)]

cronometro = Cronometro()

cronometro.inicia()

numeros.sort()

cronometro.detener()

print(f"Tiempo de ejecución: {cronometro.lapsoDeTiempo():.2f} milisegundos")