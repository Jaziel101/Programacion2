import math

def promedio(lista):
    return sum(lista) / len(lista)

def desviacion(lista):
    prom = promedio(lista)
    suma = 0
    for x in lista:
        suma += (x - prom) ** 2
    return math.sqrt(suma / (len(lista) - 1))

print("Ingrese 10 números separados por espacios:")
numeros = list(map(float, input().split()))

prom = promedio(numeros)
desv = desviacion(numeros)

print("El promedio es", round(prom, 2))
print("La desviación estándar es", round(desv, 5))