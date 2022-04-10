import pandas as pd  


def VendasPorDatas():
    df = pd.read_excel('dados/venda_mensal.xls')
    #df = df[:-3]
    return df 