import streamlit as st 
import os
import contents.analytics as ans



# configurações
st.set_page_config(
    page_title="Análista de Transporte",page_icon="🚚", layout="wide"
)

# Aplica formatação css da página
hide_st_style = """
                        <style>
                        header {visibility: hidden}
                        .block-container {padding:25px}
                        #MainMenu {visibility:hidden;}
                        footer {visibility:hidden;}
                        </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

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

# HEADER DA PÁGINA
st.title("🚦Análista de Transporte")
st.subheader("Cardeal Distribuídora")
st.divider()

# MENU DA PAGINA

menu = ["Torre de Controle", "Prestação de Contas", "Transbordo", "Fusio","OTIF E ONTIME", "Expedição", "Analises"]

tab_torre, tab_prestacao, tab_transbordo, tab_fusion, tab_otiff, tab_expedicao, tab_analises = st.tabs(menu)

with tab_torre:
    st.subheader("Torre de Controle: Atendimento aos chamados")
    st.write("A torre de controle é responsável por monitorar e gerenciar todas as operações de transporte. O objetivo é garantir uma resposta rápida e eficiente para manter as operações em movimento e resolver problemas rapidamente.")

with tab_prestacao:
    st.subheader("PRESTAÇÃO DE CONTAS")
    st.write("A prestação de contas na expedição envolve registrar todas as atividades relacionadas ao envio de produtos, incluindo documentação, confirmação de entrega e reconciliação de registro financeiros.")

with tab_transbordo:
    
    col1, col2 = st.columns([1, 2])

    with col1:
        image_transbordo = os.path.join(current_dir, 'imagens', 't2.jpg')
        st.image(image_transbordo)

    with col2:
        st.subheader("TRANSBORDO")
        st.write("O Transbordo é o processo de transferir carga de um veículo ou local para outro, frequentemente, a eficiência no transbordo pode reduzir custos e melhorar os tempos de entregas, Dentro desse processo, a utilização do datacanhoto que registra a data da transação na cópia retida pelo emissor o datacanhoto fortalece a segurança e a transparência das operações comerciais.")
        st.divider()
       

with tab_fusion:
    st.subheader("FUSION")
    st.write("O FUSION ele é uma ferramenta que oferece funcionalidade para geração de relatórios em tempo real, que facilita monitoramento de transporte e a comunicação com motorista e operador, e também facilita ver os status das entregas.")

with tab_otiff:
    st.subheader("EFICIENCIA: OTIF E ONTIME")
    st.success("OTIF: assegura que os produtos sejam entregues no tempo e na quantidade correta.")
    st.success("ONTIME: Foca especificamente a pontualidade das entregas, crucial para a satisfação do cliente.")

with tab_expedicao:
    st.subheader("EXPEDIÇÃO") 
    st.write("O planejamento de carga é fundamental para garantir que os produtos cheguem ao seu destino de forma eficiente e segura,  O planejamento determina as melhores rotas para o transporte, os prazos necessários para a entrega  Emitir documentos como o Conhecimento de Transporte Eletrônico (CTe)")

with tab_analises:
    ans.run()