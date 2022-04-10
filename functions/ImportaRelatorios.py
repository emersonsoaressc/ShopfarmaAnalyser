import pandas as pd  


def VendasPorDatas():
    df = pd.read_excel('dados/vendas_mensal.xls')
    #df = df[:-3]
    return df 