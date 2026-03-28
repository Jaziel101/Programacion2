import random

class Juego:
    
    def __init__(self, vidas: int):
        #Atributos protegidos
        self._numeroDeVidas = vidas
        self._record = 0
        self._vidasIniciales = vidas
    
    def reiniciaPartida(self):
        self._numeroDeVidas = self._vidasIniciales
    
    def actualizaRecord(self):
        pass
    
    def quitaVida(self) -> bool:
        self._numeroDeVidas -= 1
        
        if self._numeroDeVidas > 0:
            print(f"Incorrecto! Te quedan {self._numeroDeVidas} vidas.")
            return True
        else:
            print("¡GAME OVER!")
            return False

class JuegoAdivinaNumero(Juego):
    
    def __init__(self, vidas: int):
        super().__init__(vidas)
        self.__numeroAAdivinar = 0
    
    def reiniciaPartida(self):
        super().reiniciaPartida()
        self.__numeroAAdivinar = random.randint(0, 10)
    
    def actualizaRecord(self):
        self._record += 1
        print(f"¡Nuevo récord! Has acertado {self._record} veces.")
    
    def validaNumero(self, num: int) -> bool:
        return 0 <= num <= 10
    
    def juega(self): 
        self.reiniciaPartida()
        print("\n" + "="*50)
        print(f"Juego: {self.__class__.__name__} ")
        print("="*50)
        print(f"Tienes {self._numeroDeVidas} vidas.")
        print("Adivina un número entre 0 y 10")
        print("-"*50)
        
        juego_activo = True
        
        while juego_activo:
            try:
                entrada = input("\n Ingresa tu número: ")
                numero_usuario = int(entrada)

                if not self.validaNumero(numero_usuario):
                    print("Número inválido. Debe estar entre 0 y 10.")
                    continue
                
                if numero_usuario == self.__numeroAAdivinar:
                    print("\n¡Lo lograste!")
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

class JuegoAdivinaPar(JuegoAdivinaNumero):
    
    def __init__(self, vidas: int):

        super().__init__(vidas)
    
    def validaNumero(self, num: int) -> bool:
        
        if not super().validaNumero(num):
            print("Error: El número debe estar entre 0 y 10.")
            return False
        
        if num % 2 == 0:
            return True
        else:
            print("Error: Debes ingresar un número PAR.")
            return False
    
    def reiniciaPartida(self):
        super().reiniciaPartida()
        pares = [0, 2, 4, 6, 8, 10]
        self._JuegoAdivinaNumero__numeroAAdivinar = random.choice(pares)

class JuegoAdivinaImpar(JuegoAdivinaNumero):
        
    def __init__(self, vidas: int):
        super().__init__(vidas)
    
    def validaNumero(self, num: int) -> bool:
    
        if not super().validaNumero(num):
            print("Error: El número debe estar entre 0 y 10.")
            return False
        
        if num % 2 != 0:
            return True
        else:
            print("Error: Debes ingresar un número IMPAR.")
            return False
    
    def reiniciaPartida(self):
        super().reiniciaPartida()
        impares = [1, 3, 5, 7, 9]
        self._JuegoAdivinaNumero__numeroAAdivinar = random.choice(impares)

class Aplicacion:
    
    @staticmethod
    def main():
    
        print("Iniciando...")
        print("="*60)
        juego_normal = JuegoAdivinaNumero(3)
        juego_par = JuegoAdivinaPar(3)
        juego_impar = JuegoAdivinaImpar(3)
        juegos = [
            ("ADIVINA EL NÚMERO (0-10)", juego_normal),
            ("ADIVINA EL NÚMERO PAR (0-10)", juego_par),
            ("ADIVINA EL NÚMERO IMPAR (0-10)", juego_impar)
        ]
        
        for i, (nombre, juego) in enumerate(juegos, 1):
            print(f"\n{'='*60}")
            print(f"Juego {i}: {nombre}")
            print(f"{'='*60}")
            input("Presiona ENTER para comenzar...")
            juego.juega()
            print("\n" + "="*60)
            print("Juego terminado")
            print("="*60)
        
        print("\n" + ""*30)
        print("¡Gracias por jugar!")
        print(""*30)

if __name__ == "__main__":
    Aplicacion.main()