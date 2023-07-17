import random
import os
import time
from test import PalabraAdivinar 

class Main():
    # Funcion que se encargara de llamar las funciones de otros modulos
    def __init__(self):
        pass
    
    @staticmethod
    def limpiar_pantalla():
        _ = os.system('cls' if os.name == 'nt' else 'clear')

    def MenuPrincipal(self):
        vidas = 6
        palabraAdivinar = PalabraAdivinar()
        letrasAdivinadas = []
        
        for i in palabraAdivinar:
            print("_", end =" ")
        print()

        #print(palabraAdivinar)

        while vidas > 0:
            while True:
                palabraEntrada = input("Ingrese una letra: ")

                if len(palabraEntrada) != 1:
                    print("Error, debe ser una letra")
                else:
                    letras, acertada = self.VerificarPalabra(palabraEntrada, palabraAdivinar, letrasAdivinadas)
                    break
            if acertada:
                if letras:
                    letrasAdivinadas.extend(letras)
                    print("Acertaste, sigue asi")
                else:
                    print("Esta letra ya ha sido acertada")
            else:
                vidas -= 1
                print(f"Fallaste, te quedan {vidas} vidas")
            
            time.sleep(1.5)
            self.limpiar_pantalla()
            self.PalabraImpresion(palabraAdivinar, letrasAdivinadas)

            # Validamos si adivino todas las palabras
            if set(palabraAdivinar) == set(letrasAdivinadas):
                print("Felicidades, has adivinado todas las palabras")
                break

        # Imprimiendo si perdio
        if vidas == 0:
            print("Perdistes, el contador de vidas llego a cero")

    
    def PalabraImpresion(self, palabraAdivinar, letrasAdivinadas):
        for letra in palabraAdivinar:
            if letra in letrasAdivinadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print("")
    
    def VerificarPalabra(self, letra, PalabraAdivinar, letrasAdivinadas):
        if letra in letrasAdivinadas:
            return [], True    # La letra ya ha sido adivinada
        elif letra in PalabraAdivinar:
            return [letra], True # Nueva letra adivinada
        else:
            return [], False
        
instancia = Main()
instancia.MenuPrincipal()