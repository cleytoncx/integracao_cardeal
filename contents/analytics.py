import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
from streamlit_extras import metric_cards
import os

def run():

    def formatar_numero(valor):
        if valor >= 1000000:
            return '{:.1f} MM'.format(valor / 1000000)
        elif valor >= 1000:
            return '{:.1f} Mil'.format(valor / 1000)
        else:
            return '{:,.0f}'.format(valor)

    colored_header(
        label="Análise de dados",
        description="",
        color_name="violet-70"
    )

    # Definindo o caminho da imagem de forma dinâmica
    current_dir = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(current_dir, 'analises.xlsx')

    df = pd.read_excel(excel_path)

    nomes_colunas = ['ID', "CONTINENT", 'PAIS', 'TIPO PRODUTO', 'CANAL VENDA','PRIORIDADE','PEDIDO','ID PEDIDO', 'DATA ENVIO', 'UNIDADE','PRECO UNIT', 'CUSTO UNIT', 'VENDA TOTAL','CUSTO TOTAL']
    
    df.columns = nomes_colunas

    with st.expander("Base de dados"):
        st.dataframe(df,use_container_width=True,hide_index=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    quantidade_linhas = len(df)

    paieses_unicos = df['PAIS'].unique()
    qtd_paises = len(paieses_unicos)

    canais_vendas = df['CANAL VENDA'].unique()
    qtd_tipos_vendas = len(canais_vendas)

    continentes = df['CONTINENT'].unique()
    qtd_continentes = len(continentes)

    produtos_unicos = df['TIPO PRODUTO'].unique()
    quantidade_produtos = len(produtos_unicos)

    with col1:
        st.metric("Total de linhas", value=quantidade_linhas)

    with col2:
        st.metric('Total de colunas', value=qtd_paises)

    with col3:
        st.metric('Total de tipos de Vendas', value=qtd_tipos_vendas)
    
    with col4:
        st.metric('Total de continentes', value=qtd_continentes)

    with col5:
        st.metric('Quantidade de Produtos', value=quantidade_produtos)


    col6, col7, col8, col9 = st.columns(4)

    venda_total = formatar_numero(round(df['VENDA TOTAL'].sum(), 2))
    media_venda = formatar_numero(round(df['VENDA TOTAL'].median(), 2))
    custo_total = formatar_numero(round(df['CUSTO TOTAL'].sum(), 2))
    media_custo = formatar_numero(round(df['CUSTO TOTAL'].median(), 2))


    with col6:
        st.metric('Venda total', value=venda_total)

    with col7:
        st.metric('Média total', value=media_venda)

    with col8:
        st.metric('Custo total', value=custo_total)

    with col9:
        st.metric('Média custo', value=media_custo)

    st.divider()

    st.subheader("Pivot table")

    coluf_1, coluf_2, coluf3 = st.columns(3)

    with coluf_1:
        resumo_canal_vendas = pd.pivot_table(df,['CUSTO TOTAL'],['PRIORIDADE'],['CANAL VENDA'],aggfunc='sum')

        st.write(resumo_canal_vendas)

    st.divider()









    # ANALISE DE FILTRO



    st.subheader("Análise com Filtro")
    filtro_canal_vendas = st.selectbox(label='Canal de vendas', options=canais_vendas)


    df_filtrada = df[df['CANAL VENDA'] == filtro_canal_vendas]

    with st.expander("Base de Dados filtradas"):
        st.dataframe(df_filtrada,use_container_width=True,hide_index=True)




    venda_total_filtrada = formatar_numero(round(df_filtrada['VENDA TOTAL'].sum(), 2))
    st.metric('Valor de venda filtrada', value=venda_total_filtrada)

    

    metric_cards.style_metric_cards()