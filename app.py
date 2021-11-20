import streamlit as st 
import pandas as pd 
from functions.fluxodecaixa import importaContas

st.sidebar.write('Shopfarma Analyser')
option = st.sidebar.selectbox('Selecione uma opção',('Fluxo de Caixa', 'Calculadora de datas'))
if option == 'Fluxo de Caixa':
    periodo = st.sidebar.selectbox('Selecione o período a ser analisado:', ('Mensal', 'Trimestral', 'Anual'))
    if periodo == 'Mensal':
        ano = st.sidebar.selectbox('Escolha o ano correspondente', ('2021','2022','2023'))
        mes = st.sidebar.selectbox('Escolha o mês correspondente', ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'))
        if (mes == 'Janeiro') or (mes == 'Março') or (mes == 'Maio') or (mes == 'Julho') or (mes == 'Agosto') or (mes == 'Outubro') or (mes == 'Dezembro'):
            diasMes = 31
        elif (mes == 'Fevereiro'):
            diasMes = 28
        else:
            diasMes = 30

dfMes = pd.DataFrame()
for i in range(1,diasMes):
    dfMes[i] = i



df = importaContas()

st.write(dfMes)