import pandas as pd  


def VendasPorDatas():
    df = pd.read_excel('dados/vendas_mensal.xls')#, header=0, usecols='B,E,L,M,N,O').set_index('DATA')
    df = df[:-3]
    return df 