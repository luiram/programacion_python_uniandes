# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:13:59 2024

@author: luiram
"""

import calculadora_indices as calc

def mostrar_menu_genero() -> int:
    while True:
        print("Seleccione el género de la persona:")
        print("1. Hombre")
        print("2. Mujer")
        genero = input("Género de la persona: ")
        if genero in ["1", "2"]:
            return int(genero)
        print("Por favor, seleccione 1 para Hombre o 2 para Mujer.")

def ejecutar_porcentaje_grasa() -> None:
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura = float(input("Ingrese la altura de la persona (en metros): "))
    edad = int(input("Ingrese la edad de la persona (en años): "))
    genero = mostrar_menu_genero()
    valor_genero = 10.8 if genero == 1 else 0
    PGC = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print(f"La persona tiene un porcentaje de grasa corporal de {PGC:.2f}%")
    
ejecutar_porcentaje_grasa()