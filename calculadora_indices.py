# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 22:01:52 2024

@author: luiram
"""

def calcular_IMC(peso:float, altura:float)->float:
    """ Calcula el ídice de masa corporal de una persona a partir de la información recibida.
    Parámetros:
        peso (float) peso de la persona, en kilogramos.
        altura (float) altura de la persona, en metros.
    Retorna:
        float: El índice de masa corporal de la persona en kg/m^2
    """
    IMC = peso / (altura**2)
    
    return round(IMC,2)

def calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float)->float:
    """ Calcula el porcentaje de grasa de una persona a partir de la información recibida.
        Parámetros:
            peso (float) peso de la persona, en kilogramos.
            altura (float) altura de la persona, en metros.
            edad (int) edad de la persona en años.
            valor_genero (float) Valor que varía según el género de la persona: 
                en caso de ser masculino debe ser 10.8 y 
                en caso de ser femenino debe ser 0.
        Retorna:
            float: El porcentaje de grasa que tiene el cuerpo de la persona.
    """
    IMC = calcular_IMC(peso, altura)
    PGC = 1.2 * IMC + (0.23*edad) - 5.4 - valor_genero
    
    return PGC

def calcular_calorias_en_reposo(peso:float, altura:float, edad:int, valor_genero:float)->float:
    """ Calcula la cantidad de calorías que una persona quema estando en reposo
        (esto es, su tasa metabólica basal) a partir de la información recibida.
        Parámetros:
            peso (float) peso de la persona, en kilogramos.
            altura (float) altura de la persona, en centímetros.
            edad (int) edad de la persona en años.
            valor_genero (float) Valor que varía según el género de la persona: 
                en caso de ser masculino debe ser 5 y 
                en caso de ser femenino debe ser -161.
        Retorna:
            float: La cantidad de calorías que la persona quema en reposo.
    """
    TMB = (10*peso) + (6.25*altura) - (5*edad) + valor_genero
    return TMB

def calcular_calorias_en_actividad(peso:float, altura:float, edad:int, valor_genero:float, valor_actividad:float)->float:
    """ Calcula la cantidad de calorías que una persona quema al realizar algún tipo
        de actividad física (esto es, su tasa metabólica basal según actividad física).
        Parámetros:
            peso (float) peso de la persona, en kilogramos.
            altura (float) altura de la persona, en centímetros.
            edad (int) edad de la persona en años.
            valor_genero (float) Valor que varía según el género de la persona: 
                en caso de ser masculino debe ser 5 y 
                en caso de ser femenino debe ser -161.
           valor_actividad:
               Valor que depende de la actividad física semanal:
                • 1.2: poco o ningún ejercicio
                • 1.375: ejercicio ligero (1 a 3 días a la semana)
                • 1.55: ejercicio moderado (3 a 5 días a la semana)
                • 1.725: deportista (6 -7 días a la semana)
                • 1.9: atleta (entrenamientos mañana y tarde)
        Retorna:
            float: La cantidad de calorías que la persona quema en reposo.
    """
    TMB = calcular_calorias_en_reposo(peso,altura,edad,valor_genero)
    TMCaf = TMB * valor_actividad
    return TMCaf

def consumo_calorias_recomendado_para_adelgazar(peso:float, altura:float, edad:int, valor_genero:float)->str:
    """ Calcula el rango de calorías recomendado, que debe consumir una persona
        diariamente en caso de que desee adelgazar, a partir de la información recibida.
        Parámetros:
            peso (float) peso de la persona, en kilogramos.
            altura (float) altura de la persona, en centímetros.
            edad (int) edad de la persona en años.
            valor_genero (float) Valor que varía según el género de la persona: 
                en caso de ser masculino debe ser 5 y 
                en caso de ser femenino debe ser -161.
        Retorna:
            str: La cantidad de calorías que la persona debe consumir si desea adelgazar.
    """
    TMB = calcular_calorias_en_reposo(peso,altura,edad,valor_genero)
    XXX = round(TMB - TMB*0.20)
    ZZZ = round(TMB - TMB*0.15)
    return print("Para adelgazar es recomendado que consumas entre ",XXX," y ",ZZZ," calorías al día")