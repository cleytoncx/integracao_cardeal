import streamlit as st 
import os

# configurações

st.set_page_config(
    page_title="Análista de Transporte",page_icon="🚚", layout="centered"
)

# Definindo o caminho da imagem de forma dinâmica
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'imagens', 'cardeal.jpg')


# SIDEBAR

with st.sidebar:
    if os.path.exists(image_path):
        st.image(image_path, width=100)
    st.title("Integração - Analista de Transporte")
    st.subheader('Cleyton Cicero')
    st.divider()
    st.write("Essa apresentação, visa apresentar um resumo do que já consegui aprender no meu processo de integração na Cardeal Distribuidora.")

st.title("🚦Análista de Transporte")
st.subheader("Cardeal Distribuídora")

st.divider()

st.subheader("Torre de Controle: Atendimento aos chamados")
st.write("A torre de controle é responsável por monitorar e gerenciar todas as operações de transporte. O objetivo é garantir uma resposta rápida e eficiente para manter as operações em movimento e resolver problemas rapidamente.")

st.divider()

st.subheader("PRESTAÇÃO DE CONTAS")
st.write("A prestação de contas na expedição envolve registrar todas as atividades relacionadas ao envio de produtos, incluindo documentação, confirmação de entrega e reconciliação de registro financeiros.")