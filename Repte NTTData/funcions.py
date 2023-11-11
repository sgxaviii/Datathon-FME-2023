import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

"""
Pre: fitxer està a la mateixa carpeta i té un nom vàlid (excel)
Post: taula amb els valors del fitxer (pandas)
Brief: Agafa un fitxer i et dona la taula de pandas
"""
def dades():
    df = pd.read_excel('consumo_material_clean.xlsx')
    df['CATEGORIA'] = df['CODIGO'].str[0]
    df.loc[df['CATEGORIA'] == 'E', 'CATEGORIA'] = 1
    df.loc[df['CATEGORIA'] == 'B', 'CATEGORIA'] = 2
    df.loc[df['CATEGORIA'] == 'F', 'CATEGORIA'] = 3
    df.loc[df['CATEGORIA'] == 'C', 'CATEGORIA'] = 4
    df['CAJA'] = df['CANTIDADCOMPRA']/df['UNIDADESCONSUMOCONTENIDAS']
    df['ORIGEN'] = df['ORIGEN'].str.split('-')
    df['REGIO_ORIGEN'] = df['ORIGEN'].str[0]
    df['HOSPITAL_ORIGEN'] = df['ORIGEN'].str[1]
    df['DEPARTAMENT_ORIGEN'] = df['ORIGEN'].str[2]
    df['TGL'].loc[df['TGL'] == 'TRANSITO'] = 1
    df['TGL'].loc[df['TGL'] == 'ALMACENABLE'] = 0
    df['TIPOCOMPRA'].loc[df['TIPOCOMPRA'] == 'Compra menor'] = 1
    df['TIPOCOMPRA'].loc[df['TIPOCOMPRA'] == 'Concurso'] = 0
    df['CODIGO'] = df['CODIGO'].str[1::]
    df['NUMERO'] = df['NUMERO'].str.split('/')
    df['NUMERO'] = df['NUMERO'].str[0]
    df['MES'] = pd.to_datetime(df['FECHAPEDIDO']).dt.month
    df['ANY'] = pd.to_datetime(df['FECHAPEDIDO']).dt.year
    df.drop(columns=['PRODUCTO', 'IMPORTELINEA', 'REFERENCIA', 'ORIGEN', 'FECHAPEDIDO', 'CANTIDADCOMPRA', 'UNIDADESCONSUMOCONTENIDAS'], inplace=True)
    return df

"""
Pre: rebem un dataframe i un codi de producte
Post: s'imprimeix per la terminal el gràfic amb les compres totals del producte cada mes
Brief: Agafa les dades i un codi de producte i retorna un gràfic amb les compres totals cada mes d'aquest producte
"""
def graficar(df, codi):

    df = df.where(df['CATEGORIA']==codi)
    df = df[['CAJA', 'MES', 'ANY']]
    df = df.groupby(['ANY','MES'])['CAJA'].sum()
    df = df.to_frame()

    return df