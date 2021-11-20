import pandas as pd 

def importaContas():
    df = pd.read_excel('imports/contas_a_pagar.xls', header=9, usecols='C,D').set_index('Data Vencimento')
    df = df[:-2]
    return df 
