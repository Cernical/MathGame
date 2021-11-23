#!/usr/bin/python3
#version 0.2.0

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from random import randrange

import time
import subprocess #Necesario para usar el sistema y sus funciones
clear = lambda: subprocess.call('cls||clear', shell=True) #Llamada al sistema

class MathGameResultado(App):

    def build(self):
        print("")

class MathGameSumas(App):

    global ContadorPreguntas
    ContadorPreguntas = 0

    def build(self):

        while ContadorPreguntas < numPreguntas:

            #Modulo Sumas
            randomnumero1 = 0
            randomnumero2 = 0
            resultadoreal = 0
            solucion = 0
            salidaOperacionSumas = 1
            #-----------------------------------------------------------------------

            print("Sumas entre dos numeros:")
            print("")
            randomnumero1=(randrange(RangoMin,RangoMax))          #Rango de suma
            randomnumero2=(randrange(RangoMin,RangoMax))          #Rango de suma
            mostrarnumero1 = str(randomnumero1)
            mostrarnumero2 = str(randomnumero2)
            print(randomnumero1,"+",randomnumero2)
            resultadoreal = randomnumero1+randomnumero2           #Resultadoreal
            resultadoreal = int(resultadoreal)              #Convertir a Integer

            #Debugging--------------------------------------------------------------
            print(resultadoreal)
            #-----------------------------------------------------------------------

            #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
            superBox = BoxLayout(orientation ='vertical')

            #Widgets de cabecera añadidos en el plano horizontal
            cabecera = BoxLayout(orientation ='horizontal')

            consola = Label(text = "Sumas entre dos numeros: "+mostrarnumero1+"+"+mostrarnumero2)

            cabecera.add_widget(consola)

            #Widgets de pie de página añadidos en el plano vertical
            pie = BoxLayout(orientation ='vertical')

            def callback(instance):

                global ContadorPreguntas

                respuestaOperaciones = resultadoAintroducir #contiene el string del boton
                print(respuestaOperaciones)
                if respuestaOperaciones == resultadoreal:
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    ContadorPreguntas = ContadorPreguntas + 1
                    MathGameSumas().run()
                else:
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    ContadorPreguntas = ContadorPreguntas + 1
                    MathGameSumas().run()

            bienvenida = Button(text = "Seleccione la respuesta",background_color = (0,0.4,1,0.8))
            bienvenida.bind(on_press=callback)

            def on_text(instance, value):
                print('The widget', instance, 'have:', value)
                global resultadoAintroducir
                value = int(value)
                resultadoAintroducir = value

            textinput = TextInput()
            textinput.bind(text=on_text)

            pie.add_widget(bienvenida)
            pie.add_widget(textinput)

            #Salida por pantalla final
            superBox.add_widget(cabecera)
            superBox.add_widget(pie)

            #Mostrar layout completo
            return superBox

        if ContadorPreguntas == numPreguntas:
            MathGameResultado().run()

class MathGameO(App):

    def build(self):

        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = "¡Bienvenido a MathGame Android Edition! v0.2.0")

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = "Seleccione tipo de problemas;")

        def callback(instance):

            global operacion

            respuestaOperaciones = instance.text #contiene el string del boton
            print(instance.text)
            if respuestaOperaciones == "Sumas":
                operacion = "Sumas"
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameSumas().run()

        sumas = Button(text = "Sumas",background_color = (0,0.4,1,0.8))
        sumas.bind(on_press=callback)

        pie.add_widget(bienvenida)
        pie.add_widget(sumas)

        #Salida por pantalla final
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo
        return superBox

class MathGameP(App):

    def build(self):

        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = "¡Bienvenido a MathGame Android Edition! v0.2.0")

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = "Cuantas preguntas quieres (del 1 al 5)")

        def callback(instance):

            global numPreguntas

            respuestaPreguntas = instance.text #contiene el string del boton
            print(instance.text)
            if respuestaPreguntas == "1":
                numPreguntas = 1
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameO().run()
            else:
                if respuestaPreguntas == "2":
                    numPreguntas = 2
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGameO().run()
                else:
                    if respuestaPreguntas == "3":
                        numPreguntas = 3
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameO().run()
                    else:
                        if respuestaPreguntas == "4":
                            numPreguntas = 4
                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)
                            MathGameO().run()
                        else:
                            numPreguntas = 5
                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)
                            MathGameO().run()

        uno = Button(text = "1",background_color = (0,0.4,1,0.8))
        uno.bind(on_press=callback)

        dos = Button(text = "2",background_color = (0,0.4,1,0.8))
        dos.bind(on_press=callback)

        tres = Button(text = "3",background_color = (0,0.4,1,0.8))
        tres.bind(on_press=callback)

        cuatro = Button(text = "4",background_color = (0,0.4,1,0.8))
        cuatro.bind(on_press=callback)

        cinco = Button(text = "5",background_color = (0,0.4,1,0.8))
        cinco.bind(on_press=callback)

        pie.add_widget(bienvenida)
        pie.add_widget(uno)
        pie.add_widget(dos)
        pie.add_widget(tres)
        pie.add_widget(cuatro)
        pie.add_widget(cinco)

        #Salida por pantalla final
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo
        return superBox

class MathGameS(App):

    def build(self):

        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = "¡Bienvenido a MathGame Android Edition! v0.2.0")

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = "¿Quieres activar el modo supervivencia?")

        def callback(instance):

            global supervivencia

            respuestaSupervivencia = instance.text #contiene el string del boton
            print(instance.text)
            if respuestaSupervivencia == "Si":
                supervivencia = 1
                global vida
                vida = 5
                global vidascii
                vidascii = "♥♥♥♥♥"

                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameO().run()
            else:
                supervivencia = 0
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameP().run()

        aceptar = Button(text = "Si",background_color = (0,0.4,1,0.8))
        aceptar.bind(on_press=callback)

        rechazar = Button(text = "No",background_color = (0,0.4,1,0.8))
        rechazar.bind(on_press=callback)

        pie.add_widget(bienvenida)
        pie.add_widget(aceptar)
        pie.add_widget(rechazar)

        #Salida por pantalla final
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo
        return superBox

class MathGame(App):

    def build(self):

        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = "¡Bienvenido a MathGame Android Edition! v0.2.0")

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = "Seleccione dificultad")

        def callback(instance):

            global dificultad
            global RangoMin
            global RangoMax
            global MultiPuntuacion

            dificultadSeleccionada = instance.text #contiene el string del boton
            print(instance.text)
            if dificultadSeleccionada == "Fácil":
                dificultad = "F"
                RangoMin = 0
                RangoMax = 9
                MultiPuntuacion = 1
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameS().run()
            else:
                if dificultadSeleccionada == "Normal":
                    dificultad = "N"
                    RangoMin = 10
                    RangoMax = 99
                    MultiPuntuacion = 2
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGameS().run()
                else:
                    dificultad = "D"
                    RangoMin = 100
                    RangoMax = 999
                    MultiPuntuacion = 3
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGameS().run()

        dificultadFacil = Button(text = "Fácil",background_color = (0,0.4,1,0.8))
        dificultadFacil.bind(on_press=callback)

        dificultadNormal = Button(text = "Normal",background_color = (0,0.4,1,0.8))
        dificultadNormal.bind(on_press=callback)

        dificultadDificil = Button(text = "Dificil",background_color = (0,0.4,1,0.8))
        dificultadDificil.bind(on_press=callback)

        pie.add_widget(bienvenida)
        pie.add_widget(dificultadFacil)
        pie.add_widget(dificultadNormal)
        pie.add_widget(dificultadDificil)

        #Salida por pantalla final
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo
        return superBox

#Creacion de la raiz del programa
root = MathGame()
#Llamada al constructor
root.run()
