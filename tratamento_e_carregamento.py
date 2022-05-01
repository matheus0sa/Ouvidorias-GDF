import pandas as pd
import pyodbc
import os
from extracao import baixar_csv


def tc():
    print('Baixando novo dataset')
    arquivo = baixar_csv()
    print('Download concluido')
    os.remove('dados.csv')
    os.rename(arquivo, 'dados.csv')
    df = pd.read_csv('dados.csv', sep='|')
    print('inserindo novos dados')
    server = 'LAPTOP-H9VSD33T\SQLEXPRESS'
    database = 'ouvidorias'
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server Native Client 11.0};Server=localhost\SQLEXPRESS;Database=ouvidorias;Trusted_Connection=yes;')

    cursor = cnxn.cursor()

    cursor.execute('DELETE FROM [tb_ouvidorias]')
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO tb_ouvidorias ("
                       "Abertura,Identificada,Situação,"
                       "Classificação,Assunto,Região_Administrativa,"
                       "Unidade,Orgao,Tipo_Entrada) "
                       "values (?,?,?,?,?,?,?,?,?)"
                       , row['Abertura'], row['Identificada'], row['Situação'],
                       row['Classificação'], row['Assunto'], row['Região_Administrativa'],
                       row['Unidade'], row['Orgao'], row['Tipo_Entrada'])
    cnxn.commit()
    cursor.close()


if __name__ == '__main__':
    tc()