#!/usr/bin/python

#Bienvenida y pedida por pantalla Dificultad -----------------------------------

#Funcion Limpiar Pantalla-------------------------------------------------------
import subprocess
clear = lambda: subprocess.call('cls||clear', shell=True)
#-------------------------------------------------------------------------------

bucle = 1

clear()                                                        #Limpiar Pantalla
while bucle == 1:

    print("-----------------------------------------------")
    print("       ¡Bienvenido a MathGame! v0.5.0")
    print("-----------------------------------------------")
    print("")
    dificultad = input("Introduce una dificultad (f/n/d): ")

    if dificultad == "f":
        RangoMin = 0
        RangoMax = 9
        dificultadSalida = "fácil"
        bucle = 2
    else:
        if dificultad == "n":
            RangoMin = 10
            RangoMax = 99
            dificultadSalida = "normal"
            bucle = 2
        else:
            if dificultad == "d":
                RangoMin = 100
                RangoMax = 999
                dificultadSalida = "difícil"
                bucle = 2
            else:
                print("")
                clear()                                #Funcion Limpiar Pantalla
                print("...Entrada incorrecta")
                print("")

print("")
print("has seleccionado la dificultad "+dificultadSalida)
print("")
print("-----------------------------------------------")
print("")

#-------------------------------------------------------------------------------

#Pedida por pantalla NºPreguntas------------------------------------------------

bucle2 = 1
while bucle2 == 1:

    numPreguntas = input("Cuántas preguntas quieres (del 1 al 5): ")
    try:
        numPreguntas = int(numPreguntas)
    except:
        print("")
        clear()
        print("No has introducido un número")
        print("")
    else:
        if numPreguntas <1:
            print("Debe seleccionar un número igual o mayor que 1")
        else:
            if numPreguntas >5:
                print("Has seleccionado un número incorrecto")
            else:
                bucle2 = 2

#-------------------------------------------------------------------------------

#Sumas--------------------------------------------------------------------------

sumas = "s"

while sumas == "s":

    #Reinicialización-----------------------------------------------------------
    puntuacion = 0
    ContadorPreguntas = 0
    #---------------------------------------------------------------------------

    while ContadorPreguntas < numPreguntas:

        #Reinicialización Variables---------------------------------------------
        randomnumero1 = 0
        randomnumero2 = 0
        resultadoreal = 0
        solucion = 0
        #-----------------------------------------------------------------------

        print("")
        print("Sumas entre dos números:")
        print("")
        from random import randrange
        randomnumero1=(randrange(RangoMin,RangoMax))                    #Rango de suma
        randomnumero2=(randrange(RangoMin,RangoMax))                    #Rango de suma
        print(randomnumero1,"+",randomnumero2)
        resultadoreal = randomnumero1+randomnumero2         #Resultadoreal
        resultadoreal = int(resultadoreal)                  #Convertir a Integer

        #Debugging (Muestra el resultado por pantalla)--------------------------
        #print("")
        #print(resultadoreal)
        #-----------------------------------------------------------------------

        print("")
        solucion = input("Cuál es la solución: ")           #Solucion introducida pantalla
        solucion = int(solucion)                            #Convertir a integer
        if solucion == resultadoreal:
            puntuacion = puntuacion + 1
            print("")
            print("OK")
            ContadorPreguntas = ContadorPreguntas + 1
        else:
            print("")
            print("Respuesta incorrecta, el resultado era ",resultadoreal)
            ContadorPreguntas = ContadorPreguntas + 1

        print("")
        print("Has acertado ",puntuacion," preguntas de un total de ",numPreguntas)

    print("")
    sumas = input("¿Quieres seguir realizando operaciones? (s/N) ")
    clear()

#Erroes-------------------------------------------------------------------------

#ValueError: invalid literal for int() with base 10: ''
#"Se está introduciendo un string cuándo espera un integer"
