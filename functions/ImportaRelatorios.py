import pandas as pd  


def VendasPorDatas():
    df = pd.read_excel('dados/venda_mensal.xlsx', header=0, usecols='B,E,L,M,N,O').set_index('DATA')
    df = df[:-3]
    df['TOTAL ACUMULADO'] = df['TOTAL VENDAS'].cumsum()
    return df 