# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:14:21 2024

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
    altura = float(input("Ingrese la altura de la persona (en centimetros): "))
    edad = int(input("Ingrese la edad de la persona (en años): "))
    genero = mostrar_menu_genero()
    valor_genero = 5 if genero == 1 else -161
    TMB = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print(f"La persona tiene una tasa metabólica basal de {TMB}")
    
ejecutar_porcentaje_grasa()