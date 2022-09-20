#encoding:UTF-8
from clases import Partida

def printSeparador():
    print("")
    print("-------------------------------------------")
    print("")

while True: 
    partida = Partida()
    printSeparador()
    partida.crearInterfaz()
    printSeparador()
    eleccionUsuario = partida.usuario.mostrarOpcion()
    if eleccionUsuario == -1:
        print ("Nos vemos!")
        break
    elif eleccionUsuario == -2:
        print ("El número ingresado no corresponde a una opción válida. Por favor, reintente...")
        continue
    else:
        partida.mostrarResultado()
        printSeparador()
        if (partida.preguntaContinuar()):
            continue
        else:
            break