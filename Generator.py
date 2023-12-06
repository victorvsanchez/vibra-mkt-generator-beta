import streamlit as st
from langchain.llms import VertexAI

import yaml
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader

st.set_page_config(page_title="Vibra - Gerador de Emails de Campanha", layout="centered", initial_sidebar_state="auto", menu_items=None)

with open('.secrets/users.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    with st.sidebar:
        authenticator.logout('Logout', 'main', key='unique_key')
        st.write(f'Bem vindo, *{st.session_state["name"]}*!')

    llm = VertexAI(model_name="code-bison", max_output_tokens=1000, temperature=0.8)

    #Text about the campaign strategy
    filtering_strategy = st.text_input("Explique a estratégia de filtro de clientes usada:", "")

    #Marketing campaign focus dropdown
    options1 = ["Maximizar abertura de e-mails", 
                "Maximizar compras no app", 
                "Maximizar compras locais",
                "Maximizar resgate de pontos"]
    focus = st.selectbox("Selecione o foco da campanha:", options1)

    #Language type dropdown
    options2 = ["Formal", "Informal"]
    formality = st.selectbox("Selecione o tipo de linguagem a ser usado:", options2)

    # Button to trigger the action
    if st.button("Gerar campanha"):
        # Perform some action with the entered information and selected option
        #llm_answer = llm(f"Crie uma campanha de marketing para a seguinte base de clientes: {filtering_strategy}. O foco da campanha é {focus}, e a linguagem usada deve ser {formality}")
        st.success(f"Crie uma campanha de marketing para a seguinte base de clientes: {filtering_strategy}. O foco da campanha é {focus}, e a linguagem usada deve ser {formality}")