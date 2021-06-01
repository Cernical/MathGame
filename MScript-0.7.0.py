#!/usr/bin/python

#Funcion Limpiar Pantalla-------------------------------------------------------
import subprocess
clear = lambda: subprocess.call('cls||clear', shell=True)
#-------------------------------------------------------------------------------

#Programa Entero----------------------------------------------------------------
Programa = 1
while Programa == 1:

    #Bienvenida y pedida por pantalla Dificultad -------------------------------
    bucle = 1

    clear()                                                    #Limpiar Pantalla
    while bucle == 1:                      #Bienvenida e Introducción Dificultad

        print("-----------------------------------------------")
        print("       ¡Bienvenido a MathGame! v0.7.0")
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
                    clear()                            #Funcion Limpiar Pantalla
                    print("...Entrada incorrecta")
                    print("")

    print("")
    print("has seleccionado la dificultad "+dificultadSalida)
    print("")
    print("-----------------------------------------------")
    print("")

    #---------------------------------------------------------------------------

    #Pedida por pantalla NºPreguntas--------------------------------------------
    bucle2 = 1
    while bucle2 == 1:                                #Introducción nº preguntas

        numPreguntas = input("Cuántas preguntas quieres (del 1 al 5): ")
        try:
            numPreguntas = int(numPreguntas)
        except:
            print("")
            clear()
            print("...No has introducido un número")
            print("")
        else:
            if numPreguntas <1:
                print("Debe seleccionar un número igual o mayor que 1")
            else:
                if numPreguntas >5:
                    print("Has seleccionado un número incorrecto")
                else:
                    bucle2 = 2

    #---------------------------------------------------------------------------

    #Selección Problemas--------------------------------------------------------
    BucleSeleccionProblemas = 1
    while BucleSeleccionProblemas == 1:
        print("")
        SeleccionProblemas = input("Seleccione tipo de problemas; Sumas o Restas (s,r): ")
        if SeleccionProblemas == "s":
            #Sumas--------------------------------------------------------------
            sumas = "s"
            while sumas == "s":                     #Mantener el modulo de sumas

                #Reinicialización-----------------------------------------------
                puntuacion = 0
                ContadorPreguntas = 0
                #---------------------------------------------------------------

                while ContadorPreguntas < numPreguntas:     #Generación de dos números aleatorios

                    #Reinicialización Variables---------------------------------
                    randomnumero1 = 0
                    randomnumero2 = 0
                    resultadoreal = 0
                    solucion = 0
                    salidaOperacionSumas = 1
                    #-----------------------------------------------------------

                    print("")
                    print("Sumas entre dos números:")
                    print("")
                    from random import randrange
                    randomnumero1=(randrange(RangoMin,RangoMax))          #Rango de suma
                    randomnumero2=(randrange(RangoMin,RangoMax))          #Rango de suma
                    print(randomnumero1,"+",randomnumero2)
                    resultadoreal = randomnumero1+randomnumero2           #Resultadoreal
                    resultadoreal = int(resultadoreal)              #Convertir a Integer

                    #Debugging (Muestra el resultado por pantalla)--------------
                    #print("")
                    #print(resultadoreal)
                    #-----------------------------------------------------------

                    while salidaOperacionSumas == 1:   #Para mantener los números anteriores

                        print("")
                        solucion = input("Cuál es la solución: ")   #Solucion introducida pantalla

                        try:
                            solucion = int(solucion)                #Convertir a integer
                        except:
                            clear()
                            print("...No has introducido un número")
                            print("")
                            print(randomnumero1,"+",randomnumero2)

                        else:
                            if solucion == resultadoreal:
                                puntuacion = puntuacion + 1
                                print("")
                                print("OK")
                                ContadorPreguntas = ContadorPreguntas + 1
                                salidaOperacionSumas = 0
                            else:
                                print("")
                                print("Respuesta incorrecta, el resultado era ",resultadoreal)
                                ContadorPreguntas = ContadorPreguntas + 1
                                salidaOperacionSumas = 0


                    print("")
                    print("Has acertado ",puntuacion," preguntas de un total de ",numPreguntas)

                print("")
                sumas = input("¿Quieres seguir realizando operaciones? (s/N) ")
                if sumas != "s":
                    print("")
                    Programa = input("¿Quieres salir? (s/N) ")
                    if Programa == "s":
                        Programa = 0
                        BucleSeleccionProblemas = 0
                    else:
                        Programa = 1
                        BucleSeleccionProblemas = 0
                clear()
        else:
            if SeleccionProblemas == "r":
                #Restas---------------------------------------------------------
                restas = "s"
                while restas == "s":               #Mantener el modulo de Restas

                    #Reinicialización-------------------------------------------
                    puntuacion = 0
                    ContadorPreguntas = 0
                    #-----------------------------------------------------------

                    while ContadorPreguntas < numPreguntas:     #Generación de dos números aleatorios

                        #Reinicialización Variables-----------------------------
                        randomnumero1 = 0
                        randomnumero2 = 0
                        resultadoreal = 0
                        solucion = 0
                        salidaOperacionRestas = 1
                        #-------------------------------------------------------

                        print("")
                        print("Restas entre dos números:")
                        print("")
                        from random import randrange
                        randomnumero1=(randrange(RangoMin,RangoMax))          #Rango de suma
                        randomnumero2=(randrange(RangoMin,RangoMax))          #Rango de suma
                        print(randomnumero1,"-",randomnumero2)
                        resultadoreal = randomnumero1-randomnumero2           #Resultadoreal
                        resultadoreal = int(resultadoreal)              #Convertir a Integer

                        #Debugging (Muestra el resultado por pantalla)----------
                        #print("")
                        #print(resultadoreal)
                        #-------------------------------------------------------

                        while salidaOperacionRestas == 1:   #Para mantener los números anteriores

                            print("")
                            solucion = input("Cuál es la solución: ")   #Solucion introducida pantalla

                            try:
                                solucion = int(solucion)                #Convertir a integer
                            except:
                                clear()
                                print("...No has introducido un número")
                                print("")
                                print(randomnumero1,"-",randomnumero2)

                            else:
                                if solucion == resultadoreal:
                                    puntuacion = puntuacion + 1
                                    print("")
                                    print("OK")
                                    ContadorPreguntas = ContadorPreguntas + 1
                                    salidaOperacionRestas = 0
                                else:
                                    print("")
                                    print("Respuesta incorrecta, el resultado era ",resultadoreal)
                                    ContadorPreguntas = ContadorPreguntas + 1
                                    salidaOperacionRestas = 0


                        print("")
                        print("Has acertado ",puntuacion," preguntas de un total de ",numPreguntas)

                    print("")
                    restas = input("¿Quieres seguir realizando operaciones? (s/N) ")
                    if restas != "s":
                        print("")
                        Programa = input("¿Quieres salir? (s/N) ")
                        if Programa == "s":
                            Programa = 0
                            BucleSeleccionProblemas = 0
                        else:
                            Programa = 1
                            BucleSeleccionProblemas = 0
                    clear()
            else:
                clear()
                print("...No has introducido una opción válida")

#Fin Programa-------------------------------------------------------------------
