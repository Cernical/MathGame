#!/usr/bin/python3
#version 0.1.0

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

import time
import subprocess #Necesario para usar el sistema y sus funciones
clear = lambda: subprocess.call('cls||clear', shell=True) #Llamada al sistema

class MathGame(App):

    def build(self):

        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = "¡Bienvenido a MathGame Android Edition! v0.1.0")

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = "Seleccione dificultad:")

        def callback(instance):
            dificultadSeleccionada = instance.text #contiene el string del boton
            print(instance.text)

        dificultadFacil = Button(text = "Fácil")
        dificultadFacil.bind(on_press=callback)

        dificultadNormal = Button(text = "Normal")
        dificultadNormal.bind(on_press=callback)

        dificultadDificil = Button(text = "Dificil")
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
