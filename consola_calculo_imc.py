# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:12:57 2024

@author: luiram
"""

import calculadora_indices as calc

def ejecutar_calculo_imc()->None:
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura = float(input("Ingrese la altura de la persona (en metros): "))
    imc = calc.calcular_IMC(peso, altura)
    return imc
    
def categoria_imc(imc)->str:
    if imc < 16:
        categoria = "Delgadez severa"
    elif 16 <= imc < 17:
        categoria = "Delgadez moderada"
    elif 17 <= imc < 18.5:
        categoria = "Delgadez aceptable"
    elif 18.5 <= imc < 25:
        categoria = "Peso normal"
    elif 25 <= imc < 30:
        categoria = "Sobrepeso"
    elif 30 <= imc < 35:
        categoria = "Obesidad tipo I"
    elif 35 <= imc < 40:
        categoria = "Obesidad tipo II"
    elif 40 <= imc < 50:
        categoria = "Obesidad tipo III o mórbida"
    elif imc >= 50:
        categoria = "Obesidad tipo IV o extrema"
    else:
        categoria = "Valor de IMC no válido"
    
    return categoria

def iniciar_aplicacion()->None:
    imc= ejecutar_calculo_imc()
    categoria = categoria_imc(imc)
    print(f"La persona tiene un índice de masa corporal (IMC) de {round(imc,2)}, que la ubica en la categoría: {categoria}")
    

iniciar_aplicacion()