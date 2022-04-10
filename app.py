import streamlit as st 
#import streamlit_authenticator as stauth
import pandas as pd 
from functions.ImportaRelatorios import VendasPorDatas
from orc_lojas import HelloWorld

st.write(HelloWorld())
st.image('images\logo_shopfarma.png')




















#st.sidebar.image('images\logo_shopfarama.png')
#names = ['Emerson Soares']
#usernames = ['emerson']
#passwords = ['123']
#hashed_passwords = stauth.Hasher(passwords).generate()
#authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
#    'some_cookie_name','some_signature_key',cookie_expiry_days=30)
#name, authentication_status, username = authenticator.login('Login','sidebar')

#if authentication_status: 
    
# Menu Lateral
#st.sidebar.write('Bem-vindo *%s*' % (name)) 
#with st.sidebar.expander('Análise de dados'):
#    st.write('Evolução do número de clientes')
#    st.write('Evolução do Ticket Médio')
#    st.write('Análise de filial')
#with st.sidebar.expander('Análise de dados'):
#    st.write('Evolução do número de clientes')
#    st.write('Evolução do Ticket Médio')
#    st.write('Análise de filial')

#################################################################
# Dashboard Principal
#################################################################

# Gráfico com evolução das vendas mês a mês selecionável por loja
# Gráfico com evolução do numero de clientes mês a mês
# Gráfico de ticket médio de loja e de funcionários
# Gráfico de Laboratórios mais vendidos
# Gráfico de distribuidoras mais compradas
# Gráfico com participação do tipo de custos 
# Gráfico de saúde financeira das lojas

# Filtrar dados por loja
#loja = st.selectbox('Selecione uma loja:',('CENTRAL', 'MATRIZ', 'RIO VERMELHO', 'VARGEM', 'CENTRINHO', 'CALIL'))
#metricas = {
#    'venda_liquida':10
#}
# Lineup --- Venda Líquida - Entrada de Capital - Saída de Capital - Saldo de Capital
#met1, met2, met3, met4 = st.columns(4)
#met1.metric(label='Venda Líquida', value=metricas['venda_liquida'], delta='-0.6')
#met2.metric(label='Entrada Efetiva de Capital', value='92.4K', delta='-0.8')
#met3.metric(label='Saída Efetiva de Capital', value='-93.0K', delta='10.6')
#met4.metric(label='Saldo Efetivo de Capital', value='-0.6K', delta='-0.1')

# Gráfico com evolução das vendas mês a mês selecionável por loja
#with st.expander('Evolução das vendas mês a mês',True):
#    st.write(f'Aqui ficará o gráfico de vendas da {loja}!')
#    st.write('..................')




#st.write('Hello World!')