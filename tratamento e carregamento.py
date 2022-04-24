import pandas as pd
import numpy as np
import pyodbc
import shutil
import os
from extracao import baixar_csv
from datetime import datetime


def converter_data(data):
    data = data[:10]
    data = data.replace('/', '')
    data = datetime(int(data[4:]), int(data[:2]), int(data[2:4]))
    return data


hoje = pd.to_datetime(datetime.date(datetime.today()))

df = pd.read_csv('dados.csv', sep='|')
df['Abertura'] = df['Abertura'].apply(converter_data)
df_hoje = df.query('Abertura == @hoje')

if df_hoje.shape[1] < 1:
    os.remove('dados.csv')
    arquivo = baixar_csv()
    shutil.move("C:\\Users\\mathe\\Downloads\\" + arquivo, '.\\')
    os.rename(arquivo, 'dados.csv')

server = 'LAPTOP-H9VSD33T\SQLEXPRESS'
database = 'ouvidorias'
cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};Server=localhost\SQLEXPRESS;Database=ouvidorias;Trusted_Connection=yes;')

cursor = cnxn.cursor()

cursor.execute('DELETE FROM [tb_ouvidorias]')
for index, row in df.iterrows():
     cursor.execute("INSERT INTO tb_ouvidorias ("
                    "Abertura,Identificada,Situação,"
                    "Classificação,Assunto,Região_Administrativa,"
                    "Unidade,Orgao,Tipo_Entrada) "
                    "values (?,?,?,?,?,?,?,?,?)"
                    , row['Abertura'],row['Identificada'],row['Situação'],
                    row['Classificação'],row['Assunto'],row['Região_Administrativa'],
                    row['Unidade'],row['Orgao'],row['Tipo_Entrada'])
cnxn.commit()
cursor.close()
