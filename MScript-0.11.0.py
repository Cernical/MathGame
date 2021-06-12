#!/usr/bin/python

#Funcion Limpiar Pantalla-------------------------------------------------------
import subprocess
clear = lambda: subprocess.call('cls||clear', shell=True)
#-------------------------------------------------------------------------------

#Creacion Archivo Puntuaciones--------------------------------------------------
try:
    archivo = open("./points.txt", "x")
except:
    print()
else:
    archivo = open("./points.txt", "w")
    archivo.write("0")
    archivo.close()
#-------------------------------------------------------------------------------

#Programa Entero----------------------------------------------------------------
Programa = 1
while Programa == 1:

    #Bienvenida y pedida por pantalla Dificultad -------------------------------
    bucle = 1

    clear()                                                    #Limpiar Pantalla
    while bucle == 1:                      #Bienvenida e Introducción Dificultad

        print("___________________________________________________")
        print()
        print("          ¡Bienvenido a MathGame! v0.11.0")
        print("___________________________________________________")
        print("")
        archivo = open("./points.txt", "r")
        print("Tu puntuación total es de",archivo.read())
        print("___________________________________________________")
        print("")

        dificultad = input("Introduce una dificultad (f/n/d): ")

        if dificultad == "f":
            RangoMin = 0
            RangoMax = 9
            MultiPuntuacion = 1
            MultiplicadorAviso = "1"
            dificultadSalida = "fácil"
            bucle = 2
        else:
            if dificultad == "n":
                RangoMin = 10
                RangoMax = 99
                MultiPuntuacion = 2
                MultiplicadorAviso = "2"
                dificultadSalida = "normal"
                bucle = 2
            else:
                if dificultad == "d":
                    RangoMin = 100
                    RangoMax = 999
                    MultiPuntuacion = 3
                    MultiplicadorAviso = "3"
                    dificultadSalida = "difícil"
                    bucle = 2
                else:
                    print("")
                    clear()                            #Funcion Limpiar Pantalla
                    print("...No has introducido una opción válida (Introduce 'f', 'n' o 'd')")
                    print("")

    print("")
    print("has seleccionado la dificultad "+dificultadSalida)
    print("")
    print("Esto te otorga un multiplicador de "+MultiplicadorAviso)
    print("")
    print("---------------------------------------------------")
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
        print("---------------------------------------------------")
        print("")
        print("Seleccione tipo de problemas;")
        print("")
        print("Sumas | Restas | Multiplicaciones | Divisiones")
        print("")
        SeleccionProblemas = input("Introduce (s/r/m/d): ")
        clear()
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
                                clear()
                                print("¡Has acertado!")
                                ContadorPreguntas = ContadorPreguntas + 1
                                salidaOperacionSumas = 0
                            else:
                                clear()
                                print("Respuesta incorrecta, el resultado era ",resultadoreal)
                                ContadorPreguntas = ContadorPreguntas + 1
                                salidaOperacionSumas = 0


                    print("")
                    print("Has acertado ",puntuacion," preguntas de un total de ",numPreguntas)

                #Abrir archivo, lectura y procesamiento-------------------------
                archivo = open("./points.txt", "r")

                contenido = archivo.read()
                contenidoInt = int(contenido)

                puntuacionMultiplicada = puntuacion*MultiPuntuacion
                resultadoAintroducir = contenidoInt+puntuacionMultiplicada
                resultadoAintroducir = str(resultadoAintroducir)

                archivo = open("./points.txt", "w")
                archivo.write(resultadoAintroducir)
                archivo.close()
                #---------------------------------------------------------------

                print("")
                sumas = input("¿Quieres seguir realizando operaciones? (s/N) ")
                if sumas != "s":
                    clear()
                    Programa = input("¿Quieres salir? (s/N) ")
                    if Programa == "s":
                        Programa = 0
                        BucleSeleccionProblemas = 0
                    else:
                        Programa = 1
                        BucleSeleccionProblemas = 0
                clear()
                #FinSumas-------------------------------------------------------
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

                        print("Restas entre dos números:")
                        print("")
                        from random import randrange
                        randomnumero1=(randrange(RangoMin,RangoMax))          #Rango de resta
                        randomnumero2=(randrange(RangoMin,RangoMax))          #Rango de resta
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
                                    clear()
                                    print("!Has acertado¡")
                                    ContadorPreguntas = ContadorPreguntas + 1
                                    salidaOperacionRestas = 0
                                else:
                                    clear()
                                    print("Respuesta incorrecta, el resultado era ",resultadoreal)
                                    ContadorPreguntas = ContadorPreguntas + 1
                                    salidaOperacionRestas = 0


                        print("")
                        print("Has acertado ",puntuacion," preguntas de un total de ",numPreguntas)

                    #Abrir archivo, lectura y procesamiento---------------------
                    archivo = open("./points.txt", "r")

                    contenido = archivo.read()
                    contenidoInt = int(contenido)

                    puntuacionMultiplicada = puntuacion*MultiPuntuacion
                    resultadoAintroducir = contenidoInt+puntuacionMultiplicada
                    resultadoAintroducir = str(resultadoAintroducir)

                    archivo = open("./points.txt", "w")
                    archivo.write(resultadoAintroducir)
                    archivo.close()
                    #-----------------------------------------------------------

                    print("")
                    restas = input("¿Quieres seguir realizando operaciones? (s/N) ")
                    if restas != "s":
                        clear()
                        Programa = input("¿Quieres salir? (s/N) ")
                        if Programa == "s":
                            Programa = 0
                            BucleSeleccionProblemas = 0
                        else:
                            Programa = 1
                            BucleSeleccionProblemas = 0
                    clear()
                    #FinRestas--------------------------------------------------
            else:
                if SeleccionProblemas == "m":
                    #Multiplicaciones-------------------------------------------
                    multiplicaciones = "s"
                    while multiplicaciones == "s":               #Mantener el modulo de Multiplicaciones

                        #Reinicialización---------------------------------------
                        puntuacion = 0
                        ContadorPreguntas = 0
                        #-------------------------------------------------------

                        while ContadorPreguntas < numPreguntas:     #Generación de dos números aleatorios

                            #Reinicialización Variables-------------------------
                            randomnumero1 = 0
                            randomnumero2 = 0
                            resultadoreal = 0
                            solucion = 0
                            salidaOperacionMultiplicaciones = 1
                            #---------------------------------------------------

                            print("Multiplicaciones entre dos números:")
                            print("")
                            from random import randrange
                            randomnumero1=(randrange(RangoMin,RangoMax))          #Rango de Multiplicaciones
                            randomnumero2=(randrange(RangoMin,RangoMax))          #Rango de Multiplicaciones
                            print(randomnumero1,"x",randomnumero2)
                            resultadoreal = randomnumero1*randomnumero2           #Resultadoreal
                            resultadoreal = int(resultadoreal)              #Convertir a Integer

                            #Debugging (Muestra el resultado por pantalla)------
                            #print("")
                            #print(resultadoreal)
                            #---------------------------------------------------

                            while salidaOperacionMultiplicaciones == 1:   #Para mantener los números anteriores

                                print("")
                                solucion = input("Cuál es la solución: ")   #Solucion introducida pantalla

                                try:
                                    solucion = int(solucion)                #Convertir a integer
                                except:
                                    clear()
                                    print("...No has introducido un número")
                                    print("")
                                    print(randomnumero1,"x",randomnumero2)

                                else:
                                    if solucion == resultadoreal:
                                        puntuacion = puntuacion + 1
                                        clear()
                                        print("!Has acertado¡")
                                        ContadorPreguntas = ContadorPreguntas + 1
                                        salidaOperacionMultiplicaciones = 0
                                    else:
                                        clear()
                                        print("Respuesta incorrecta, el resultado era ",resultadoreal)
                                        ContadorPreguntas = ContadorPreguntas + 1
                                        salidaOperacionMultiplicaciones = 0


                            print("")
                            print("Has acertado ",puntuacion," preguntas de un total de ",numPreguntas)

                        #Abrir archivo, lectura y procesamiento-----------------
                        archivo = open("./points.txt", "r")

                        contenido = archivo.read()
                        contenidoInt = int(contenido)

                        puntuacionMultiplicada = puntuacion*MultiPuntuacion
                        resultadoAintroducir = contenidoInt+puntuacionMultiplicada
                        resultadoAintroducir = str(resultadoAintroducir)

                        archivo = open("./points.txt", "w")
                        archivo.write(resultadoAintroducir)
                        archivo.close()
                        #-------------------------------------------------------

                        print("")
                        multiplicaciones = input("¿Quieres seguir realizando operaciones? (s/N) ")
                        if multiplicaciones != "s":
                            clear()
                            Programa = input("¿Quieres salir? (s/N) ")
                            if Programa == "s":
                                Programa = 0
                                BucleSeleccionProblemas = 0
                            else:
                                Programa = 1
                                BucleSeleccionProblemas = 0
                        clear()
                        #FinMultiplicaciones------------------------------------
                else:
                    if SeleccionProblemas == "d":
                        #Divisiones---------------------------------------------
                        divisiones = "s"
                        while divisiones == "s":               #Mantener el modulo de Divisiones

                            #Reinicialización-----------------------------------
                            puntuacion = 0
                            ContadorPreguntas = 0
                            #---------------------------------------------------

                            while ContadorPreguntas < numPreguntas:     #Generación de dos números aleatorios

                                #Reinicialización Variables---------------------
                                randomnumero1 = 0
                                randomnumero2 = 0
                                resultadoreal = 0
                                solucion = 0
                                salidaOperacionDivisiones = 1
                                #-----------------------------------------------

                                print("Divisiones entre dos números:")
                                print("")
                                from random import randrange
                                randomnumero1=(randrange(RangoMin,RangoMax))          #Rango de Divisiones
                                randomnumero2=(randrange(1,9))                        #Rango de Divisiones
                                print(randomnumero1,"/",randomnumero2)
                                resultadoreal = randomnumero1/randomnumero2           #Resultadoreal
                                resultadoreal = int(resultadoreal)              #Convertir a Integer

                                #Debugging (Muestra el resultado por pantalla)--
                                #print("")
                                #print(resultadoreal)
                                #-----------------------------------------------

                                while salidaOperacionDivisiones == 1:   #Para mantener los números anteriores

                                    print("")
                                    solucion = input("Cuál es la solución: ")   #Solucion introducida pantalla

                                    try:
                                        solucion = int(solucion)                #Convertir a integer
                                    except:
                                        clear()
                                        print("...No has introducido un número")
                                        print("")
                                        print(randomnumero1,"/",randomnumero2)

                                    else:
                                        if solucion == resultadoreal:
                                            puntuacion = puntuacion + 1
                                            clear()
                                            print("!Has acertado¡")
                                            ContadorPreguntas = ContadorPreguntas + 1
                                            salidaOperacionDivisiones = 0
                                        else:
                                            clear()
                                            print("Respuesta incorrecta, el resultado era ",resultadoreal)
                                            ContadorPreguntas = ContadorPreguntas + 1
                                            salidaOperacionDivisiones = 0


                                print("")
                                print("Has acertado ",puntuacion," preguntas de un total de ",numPreguntas)

                            #Abrir archivo, lectura y procesamiento-----------------
                            archivo = open("./points.txt", "r")

                            contenido = archivo.read()
                            contenidoInt = int(contenido)

                            puntuacionMultiplicada = puntuacion*MultiPuntuacion
                            resultadoAintroducir = contenidoInt+puntuacionMultiplicada
                            resultadoAintroducir = str(resultadoAintroducir)

                            archivo = open("./points.txt", "w")
                            archivo.write(resultadoAintroducir)
                            archivo.close()
                            #-------------------------------------------------------

                            print("")
                            divisiones = input("¿Quieres seguir realizando operaciones? (s/N) ")
                            if divisiones != "s":
                                clear()
                                Programa = input("¿Quieres salir? (s/N) ")
                                if Programa == "s":
                                    Programa = 0
                                    BucleSeleccionProblemas = 0
                                else:
                                    Programa = 1
                                    BucleSeleccionProblemas = 0
                            clear()
                            #FinDivisiones--------------------------------------
                    else:
                        clear()
                        print("...No has introducido una opción válida (Introduce 's', 'r', 'm' o 'd')")

#Pregunta sobre Archivo Puntuacion----------------------------------------------
respuestaPuntuacionArchivo = input("¿Quieres ver tu puntuación total? (s/N) ")
if respuestaPuntuacionArchivo == "s":
    archivo = open("./points.txt", "r")
    clear()
    print("Tu puntuación es de",archivo.read())
else:
    clear()
#-------------------------------------------------------------------------------

#Fin Programa-------------------------------------------------------------------
