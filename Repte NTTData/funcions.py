import numpy as np 
import pandas as pd 

"""
Pre: fitxer està a la mateixa carpeta i té un nom vàlid (excel)
Post: taula amb els valors del fitxer (pandas)
Brief: Agafa un fitxer i et dona la taula de pandas
"""
def dades(fitxer="consumo_material_clean.xlsx"):

    df = pd.read_excel(fitxer)
    df.head()
    df['NUMERO'] = df['NUMERO'].str.split('/')
    df['NUMERO'] = df['NUMERO'].str[0]
    df['CATEGORIA'] = df['CODIGO'].str[0]
    df['CODIGO'] = df['CODIGO'].str[1::]
    df['ANY'] = pd.to_datetime(df['FECHAPEDIDO'], format='mixed').dt.year
    df['ORIGEN'] = df['ORIGEN'].str.split('-')
    df['REGION_ORIGEN'] = df['ORIGEN'].str[0]
    df['HOSPITAL_ORIGEN'] = df['ORIGEN'].str[1]
    df['DEPARTAMENT_ORIGEN'] = df['ORIGEN'].str[2]
    return df