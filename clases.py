from random import choice

class Jugador():
    
    def __init__(self,pNumero):
        self.numeroOpcion = pNumero
        
    def convertirOpcion(self):
        if self.numeroOpcion == 1:
            opcion = "piedra"
        elif self.numeroOpcion == 2:
            opcion = "papel"
        elif self.numeroOpcion == 3:
            opcion = "tijera"
        return opcion
    
    def mostrarOpcion(self):
        opcionValida = self.numeroOpcion in [1,2,3]
        if (opcionValida):
            result = self.convertirOpcion()
        elif self.numeroOpcion == 4:
            result = -1
        else:
            result = -2
        return result
        
class Partida():
    
    def __init__(self):
        self.pc = Jugador(choice([1,2,3]))
        self.usuario = None
        self.resultado = None
        
    def crearInterfaz(self):
        print("1)Piedra")
        print("2)Papel")
        print("3)Tijera")
        print("4)Salir del Programa")
        entrada = input("Que eliges: ")
        try:
            self.usuario = Jugador(int(entrada))
        except ValueError:
            print("Por favor, ingrese un número:")
            self.crearInterfaz()   

    def mostrarElecciones(self):
        print("Tu eliges: ", self.usuario.mostrarOpcion())   
        print("PC eligio: ", self.pc.mostrarOpcion())
        
    def decidirResultado(self):
        eleccionUsuario = self.usuario.mostrarOpcion()
        eleccionPC = self.pc.mostrarOpcion()
        if eleccionPC == "piedra" and eleccionUsuario == "papel":
            self.resultado = "Ganaste, papel envuelve piedra"
        elif eleccionPC == "papel" and eleccionUsuario == "tijera":
            self.resultado = "Ganaste, tijera corta papel"
        elif eleccionPC == "tijera" and eleccionUsuario == "piedra":
            self.resultado = "Ganaste, piedra pisa tijera"
        if eleccionUsuario == "piedra" and eleccionPC == "papel":
            self.resultado = "Perdiste, papel envuelve piedra"
        elif eleccionUsuario == "papel" and eleccionPC == "tijera":
            self.resultado = "Perdiste, tijera corta papel"
        elif eleccionUsuario == "tijera" and eleccionPC == "piedra":
            self.resultado = "Perdiste, piedra pisa tijera"
        elif eleccionPC == eleccionUsuario:
            self.resultado = "Empate"  

    def mostrarResultado(self):
        self.mostrarElecciones()
        self.decidirResultado()
        print(self.resultado)
        
    def preguntaContinuar(self,pValor = None):
        if (pValor == None):
            again = input("Jugamos de nuevo? Si/No: ")
        else:
            again = input(pValor)
        again = str(again).lower()
        if 'si' in again:
            result = True;
        elif 'no' in again:
            print("Nos vemos!")
            result = False;
        else:
            result = self.preguntaContinuar("Valor inválido... Seleccione Si/No:")
        return result  
        