# -*- coding: utf-8 -*-
"""Dados  com Matplotlib (PETROBRAS 2023)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x9Ouoky-yho0IB3GqyTGwfsS9-66wDMR
"""

!pip install mplfinance

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import yfinance as yf
import plotly.graph_objects as go
import mplfinance as mpf
from plotly.subplots import make_subplots

dados = yf.download('Petr4.SA', start='2023-01-01', end='2023-12-31')
dados

dados.columns

dados.columns = ['Abertura', 'Maximo', 'Minimo', 'Fechamento', 'Fech_Ajust', 'Volume']
dados = dados.rename_axis('DATA')
dados

dados ['Fechamento'].plot(figsize = (10,6))
plt.title ('Variação do preço por DATA', fontsize=17)
plt.legend (['Fechamento'])

df = dados.head(60).copy()
df ['Data'] = df.index
df ['Data'] = df ['Data'].apply(mdates.date2num)
df

fig, ax = plt.subplots (figsize = (15,8))

width = 0.7

fig, ax = plt.subplots()

for i in range(len(df)):
    if df["Fechamento"].iloc[i] > df["Abertura"].iloc[i]:
        color = 'green'
    else:
        color = 'red'

    ax.plot([df['Data'].iloc[i], df['Data'].iloc[i]],
            [df['Minimo'].iloc[i], df['Maximo'].iloc[i]],
            color=color,
            linewidth=1)

    ax.add_patch(plt.Rectangle((df['Data'].iloc[i] - width/2, min(df['Abertura'].iloc[i], df['Fechamento'].iloc[i])),
                                width,
                                abs(df['Fechamento'].iloc[i] - df['Abertura'].iloc[i]),
                                facecolor=color))


df['MA7'] = df ['Fechamento'].rolling(window = 7).mean()
df['MA14'] = df ['Fechamento'].rolling(window = 14).mean()
ax.plot(df ['Data'], df ['MA7'], color = 'black', label = 'Média Móvel 7 dias')
ax.plot(df ['Data'], df ['MA14'], color = 'orange', label = 'Média Móvel 14 dias')
ax.legend ()

plt.title ('Grafico de Candlestick - PETROBRAS 2023 COM MATPLOTLIB')
plt.xlabel ('DATA')
plt.ylabel ('PREÇO')
plt.show()

dados = yf.download('Petr4.SA', start='2023-01-01', end='2023-12-31')

import mplfinance as mpf
#API

mpf.plot(dados.head(30), type='candle', figsize=(16,8), volume=True, mav=(7,14), style='yahoo')