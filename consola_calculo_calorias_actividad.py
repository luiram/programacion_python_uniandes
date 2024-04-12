# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:14:36 2024

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
        
def mostrar_actividad_semanal() -> float:
    while True:
        print("Seleccione el número del tipo de actividad que realiza semanalmente la persona:")
        print("1. poco o ningún ejercicio")
        print("2. ejercicio ligero (1 a 3 días a la semana)")
        print("3. ejercicio moderado (3 a 5 días a la semana)")
        print("4. deportista (6 -7 días a la semana)")
        print("5. atleta (entrenamientos mañana y tarde")
        actividad = input("Actividad que realiza semanalmente: ")
        if actividad in ["1", "2", "3", "4", "5"]:
            return float(valor_actividad_por_tipo(int(actividad)))
        
def valor_actividad_por_tipo(actividad: int)->float:
    if actividad == 1:
        return 1.2
    elif actividad == 2:
        return 1.375
    elif actividad == 3:
        return 1.55
    elif actividad == 4:
        return 1.72
    else:
        return 1.9

def ejecutar_consumo_calorias() -> None:
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura = float(input("Ingrese la altura de la persona (en centimetros): "))
    edad = int(input("Ingrese la edad de la persona (en años): "))
    genero = mostrar_menu_genero()
    valor_genero = 5 if genero == 1 else -161
    valor_actividad = mostrar_actividad_semanal()
    
    TMB_af = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print(f"La persona tiene un consumo de calorria semanal de {TMB_af:.2f}")
    
ejecutar_consumo_calorias()
