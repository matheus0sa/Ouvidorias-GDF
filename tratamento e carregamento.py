import pandas as pd
import numpy as np
import shutil
import os
from extracao import baixar_csv
from datetime import datetime, date


def converter_data(data):
    data = data[:10]
    data = data.replace('/', '')
    data = datetime(int(data[4:]), int(data[:2]), int(data[2:4]))
    return data


hoje = pd.to_datetime(date(datetime.today()))

df = pd.read_csv('dados.csv', sep='|')
df['Abertura'] = df['Abertura'].apply(converter_data)
df_hoje = df.query('Abertura == @hoje')

if df_hoje.shape[1] < 1:
    os.remove('dados.csv')
    arquivo = baixar_csv()
    shutil.move("C:\\Users\\mathe\\Downloads\\" + arquivo, '.\\')
    os.rename(arquivo, 'dados.csv')
