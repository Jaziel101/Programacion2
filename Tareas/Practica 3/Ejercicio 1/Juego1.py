import random

class Juego:
    
    def __init__(self, vidas: int):
        #Atributos protegidos
        self._numeroDeVidas = vidas  
        self._record = 0              
    
    def reiniciaPartida(self):
        if not hasattr(self, '_vidasIniciales'):
            self._vidasIniciales = self._numeroDeVidas
        self._numeroDeVidas = self._vidasIniciales
    
    def actualizaRecord(self):
        pass
    
    def quitaVida(self) -> bool:
        self._numeroDeVidas -= 1        
        if self._numeroDeVidas > 0:
            print(f" Incorrecto! Te quedan {self._numeroDeVidas} vidas.")
            return True
        else:
            print("¡GAME OVER!")
            return False

class JuegoAdivinaNumero(Juego):    
    def __init__(self, vidas: int):
        super().__init__(vidas)
        self.__numeroAAdivinar = 0  
        self._vidasIniciales = vidas  
    
    def reiniciaPartida(self):
        super().reiniciaPartida() 
        self.__numeroAAdivinar = random.randint(0, 10)  
    
    def actualizaRecord(self):
        self._record += 1
        print(f"¡Nuevo récord! Has acertado {self._record} veces.")
    
    def juega(self):
        self.reiniciaPartida()
        print("\n" + "="*50)
        print("JUEGO: ADIVINA EL NÚMERO")
        print("="*50)
        print(f"Tienes {self._numeroDeVidas} vidas.")
        print("Adivina un número entre 0 y 10")
        print("-"*50)
        juego_activo = True
        while juego_activo:
            try:
                entrada = input("\n Ingresa tu número: ")
                numero_usuario = int(entrada)
                if numero_usuario < 0 or numero_usuario > 10:
                    print("El número debe estar entre 0 y 10. Intenta de nuevo.")
                    continue
                if numero_usuario == self.__numeroAAdivinar:
                    print("\n ¡Lo lograste! ")
                    print(f"El número era {self.__numeroAAdivinar}")
                    self.actualizaRecord()
                    juego_activo = False 
                else:
                    if numero_usuario < self.__numeroAAdivinar:
                        print(f"El número {numero_usuario} es MENOR que el número a adivinar.")
                    else:
                        print(f"El número {numero_usuario} es MAYOR que el número a adivinar.")

                    if not self.quitaVida():

                        print(f"\n El número era {self.__numeroAAdivinar}")
                        juego_activo = False
                    else:
                        print("Intenta de nuevo...")
                        
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")

class Aplicacion:
 
    @staticmethod
    def main():

        print("Iniciando...")
        print("Bienvenido a Adivina el Número!")
        print("-"*40)
        
        while True:
            try:
                vidas = int(input("¿Con cuántas vidas quieres jugar? "))
                if vidas > 0:
                    break
                else:
                    print("El número de vidas debe ser positivo.")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
        
        juego = JuegoAdivinaNumero(vidas)
        
        juego.juega()
        
        print("\n" + "="*50)
        print("¡Gracias por jugar!")
        print("="*50)

if __name__ == "__main__":
    Aplicacion.main()