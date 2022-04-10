import pandas as pd  


def VendasPorDatas():
    df = pd.read_excel('dados/venda_mensal.xls', header=0, usecols='B,E,L,M,N,O', engine='openpyxl').set_index('DATA')
    df = df[:-3]
    df['TOTAL ACUMULADO'] = df['TOTAL VENDAS'].cumsum()
    return df 