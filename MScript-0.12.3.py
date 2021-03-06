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
        print("          ¡Bienvenido a MathGame! v0.12.3")
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

    #Modo_Preguntas-------------------------------------------------------------
    respuesta_supervivencia = 0
    modo_supervivencia = 0

    bucle_modo = 1
    while bucle_modo == 1:

        respuesta_supervivencia = input("¿Quieres activar el modo supervivencia? (s/N): ")

        if respuesta_supervivencia == "s" or respuesta_supervivencia == "S":
            modo_supervivencia = 1
            vida = 5
            vidascii = "♥♥♥♥♥"
            numPreguntas = 0
            print("")
            print("Modo de supervivencia activado")
            print("")
            print("Tienes",vida,"vidas")
            bucle_modo = 0
        else:
            modo_supervivencia = 0
            print("")
            print("Modo de supervivencia desactivado")
            print("")
            print("---------------------------------------------------")
            print("")
            vida = 0
            bucle_modo = 0

            #Pedida por pantalla NºPreguntas------------------------------------
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
                        clear()
                        print("Debe seleccionar un número igual o mayor que 1")
                        print("")
                    else:
                        if numPreguntas >5:
                            clear()
                            print("Has seleccionado un número incorrecto")
                            print("")
                        else:
                            bucle2 = 2
            #Fin_pedida_numero_preguntas----------------------------------------
    #Fin_modo_preguntas---------------------------------------------------------

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

                while ContadorPreguntas < numPreguntas or vida != 0:     #Generación de dos números aleatorios

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
                                vida = vida - 1
                                clear()
                                print("Respuesta incorrecta, el resultado era ",resultadoreal)
                                ContadorPreguntas = ContadorPreguntas + 1
                                salidaOperacionSumas = 0

                    if modo_supervivencia == 0:
                        print("")
                        print("Has acertado ",puntuacion," preguntas de un total de ",numPreguntas)
                        print("")
                    else:
                        print("")
                        print("Has acertado ",puntuacion," preguntas de un total de ",ContadorPreguntas)
                        print("")

                        if vida == 5:
                            vidascii = "♥♥♥♥♥"
                        else:
                            if vida == 4:
                                vidascii = "♥♥♥♥"
                            else:
                                if vida == 3:
                                    vidascii = "♥♥♥"
                                else:
                                    if vida == 2:
                                        vidascii = "♥♥"
                                    else:
                                        if vida == 1:
                                            vidascii = "♥"
                                        else:
                                            vidascii = "0"

                        print("Tienes",vidascii,"vidas")
                        print("")
                        print("---------------------------------------------------")
                        print("")

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

                #Desenlace_Operaciones------------------------------------------
                if modo_supervivencia == 1:
                    print("Te has quedado sin vidas")
                    print("")
                    Programa = input("¿Quieres salir? (s/N) ")
                    if Programa == "s":
                        sumas = "n"               #Para salirse del modulo sumas
                        Programa = 0
                        BucleSeleccionProblemas = 0
                    else:
                        sumas = "n"               #Para salirse del modulo sumas
                        Programa = 1
                        BucleSeleccionProblemas = 0
                else:
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
                #FinDesenlace---------------------------------------------------
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

                    while ContadorPreguntas < numPreguntas or vida != 0:     #Generación de dos números aleatorios

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
                                    vida = vida - 1
                                    clear()
                                    print("Respuesta incorrecta, el resultado era ",resultadoreal)
                                    ContadorPreguntas = ContadorPreguntas + 1
                                    salidaOperacionRestas = 0

                        if modo_supervivencia == 0:
                            print("")
                            print("Has acertado ",puntuacion," preguntas de un total de ",numPreguntas)
                            print("")
                        else:
                            print("")
                            print("Has acertado ",puntuacion," preguntas de un total de ",ContadorPreguntas)
                            print("")

                            if vida == 5:
                                vidascii = "♥♥♥♥♥"
                            else:
                                if vida == 4:
                                    vidascii = "♥♥♥♥"
                                else:
                                    if vida == 3:
                                        vidascii = "♥♥♥"
                                    else:
                                        if vida == 2:
                                            vidascii = "♥♥"
                                        else:
                                            if vida == 1:
                                                vidascii = "♥"
                                            else:
                                                vidascii = "0"

                            print("Tienes",vidascii,"vidas")
                            print("")
                            print("---------------------------------------------------")
                            print("")

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

                    #Desenlace_Operaciones--------------------------------------
                    if modo_supervivencia == 1:
                        print("Te has quedado sin vidas")
                        print("")
                        Programa = input("¿Quieres salir? (s/N) ")
                        if Programa == "s":
                            restas = "n"         #Para salirse del modulo restas
                            Programa = 0
                            BucleSeleccionProblemas = 0
                        else:
                            restas = "n"         #Para salirse del modulo restas
                            Programa = 1
                            BucleSeleccionProblemas = 0
                    else:
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
                    #FinDesenlace-----------------------------------------------

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

                        while ContadorPreguntas < numPreguntas or vida != 0:     #Generación de dos números aleatorios

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
                                        vida = vida - 1
                                        clear()
                                        print("Respuesta incorrecta, el resultado era ",resultadoreal)
                                        ContadorPreguntas = ContadorPreguntas + 1
                                        salidaOperacionMultiplicaciones = 0

                            if modo_supervivencia == 0:
                                print("")
                                print("Has acertado ",puntuacion," preguntas de un total de ",numPreguntas)
                                print("")
                            else:
                                print("")
                                print("Has acertado ",puntuacion," preguntas de un total de ",ContadorPreguntas)
                                print("")

                                if vida == 5:
                                    vidascii = "♥♥♥♥♥"
                                else:
                                    if vida == 4:
                                        vidascii = "♥♥♥♥"
                                    else:
                                        if vida == 3:
                                            vidascii = "♥♥♥"
                                        else:
                                            if vida == 2:
                                                vidascii = "♥♥"
                                            else:
                                                if vida == 1:
                                                    vidascii = "♥"
                                                else:
                                                    vidascii = "0"

                                print("Tienes",vidascii,"vidas")
                                print("")
                                print("---------------------------------------------------")
                                print("")

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
                        #Desenlace_Operaciones----------------------------------
                        if modo_supervivencia == 1:
                            print("Te has quedado sin vidas")
                            print("")
                            Programa = input("¿Quieres salir? (s/N) ")
                            if Programa == "s":
                                multiplicaciones = "n" #Para salirse del modulo multiplicaciones
                                Programa = 0
                                BucleSeleccionProblemas = 0
                            else:
                                multiplicaciones = "n" #Para salirse del modulo multiplicaciones
                                Programa = 1
                                BucleSeleccionProblemas = 0
                        else:
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
                        #FinDesenlace-------------------------------------------
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

                            while ContadorPreguntas < numPreguntas or vida != 0:     #Generación de dos números aleatorios

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
                                            vida = vida - 1
                                            clear()
                                            print("Respuesta incorrecta, el resultado era ",resultadoreal)
                                            ContadorPreguntas = ContadorPreguntas + 1
                                            salidaOperacionDivisiones = 0

                                if modo_supervivencia == 0:
                                    print("")
                                    print("Has acertado ",puntuacion," preguntas de un total de ",numPreguntas)
                                    print("")
                                else:
                                    print("")
                                    print("Has acertado ",puntuacion," preguntas de un total de ",ContadorPreguntas)
                                    print("")

                                    if vida == 5:
                                        vidascii = "♥♥♥♥♥"
                                    else:
                                        if vida == 4:
                                            vidascii = "♥♥♥♥"
                                        else:
                                            if vida == 3:
                                                vidascii = "♥♥♥"
                                            else:
                                                if vida == 2:
                                                    vidascii = "♥♥"
                                                else:
                                                    if vida == 1:
                                                        vidascii = "♥"
                                                    else:
                                                        vidascii = "0"

                                    print("Tienes",vidascii,"vidas")
                                    print("")
                                    print("---------------------------------------------------")
                                    print("")

                            #Abrir archivo, lectura y procesamiento-------------
                            archivo = open("./points.txt", "r")

                            contenido = archivo.read()
                            contenidoInt = int(contenido)

                            puntuacionMultiplicada = puntuacion*MultiPuntuacion
                            resultadoAintroducir = contenidoInt+puntuacionMultiplicada
                            resultadoAintroducir = str(resultadoAintroducir)

                            archivo = open("./points.txt", "w")
                            archivo.write(resultadoAintroducir)
                            archivo.close()
                            #---------------------------------------------------

                            #Desenlace_Operaciones------------------------------
                            if modo_supervivencia == 1:
                                print("Te has quedado sin vidas")
                                print("")
                                Programa = input("¿Quieres salir? (s/N) ")
                                if Programa == "s":
                                    divisiones = "n" #Para salirse del modulo divisiones
                                    Programa = 0
                                    BucleSeleccionProblemas = 0
                                else:
                                    divisiones = "n" #Para salirse del modulo divisiones
                                    Programa = 1
                                    BucleSeleccionProblemas = 0
                            else:
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
                            #FinDesenlace---------------------------------------

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
