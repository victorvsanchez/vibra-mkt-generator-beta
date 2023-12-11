import streamlit as st
from google.cloud import aiplatform
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

    PROJECT_ID = "vibra-dtan-prd"
    aiplatform.init(
        project=PROJECT_ID
    )
    llm = VertexAI(model_name="text-unicorn", max_output_tokens=1000, temperature=0.80)

    #Text about the campaign strategy
    filtering_strategy = st.text_input("Explique a estratégia de filtro de clientes usada:", "")

    #Marketing campaign focus dropdown
    options1 = ["Maximizar compras pelo app", 
                "Maximizar compras em postos Petrobrás",
                "Maximizar resgate de pontos"]
    focus = st.selectbox("Selecione o foco da campanha:", options1)

    #Language type dropdown
    options2 = ["Formal", "Informal"]
    formality = st.selectbox("Selecione o tipo de linguagem a ser usado:", options2)

    #Text about the campaign strategy
    keywords = st.text_input("Escreva palavras-chaves separadas por vírgula para serem usadas no e-mail:", "")

    # Button to trigger the action
    if st.button("Gerar campanha"):

        if formality == "Informal":
            formality_prompt = "Utilize de linguagem informal, usando abreviações e emojis. Fale como fosse uma pessoa no WhatsApp"
        else:
            formality_prompt = "Utilize de linguagem formal, concisa e direta"

        prompt = f"""Você é um assistente cuja função é escrever templates de e-mail da empresa Premmia.
         
        A Premmia é uma empresa onde você faz compras e ganha pontos. Você pode ganhar pontos Premmia de diversas formas: Abastecendo 
        seu carro em postos Petrobras, fazendo pagamentos pelo aplicativo (app) Premmia ou digitando seu CPF na máquina de cartão. Você 
        pode resgatar seus pontos Premmia de diversas formas: pelo site do programa (www.premmia.com.br), pelo aplicativo do programa 
        (disponível para Android e iOS) e nas lojas físicas dos parceiros do programa.
        
        A Premmia está  com uma promoção chamada 'Caminhão do Huck', que será válida até 29/12/23. Seu funcionamento é: a 
        cada 100 reais em compras feitas em postos Petrobrás, você recebe 1 ticket de roleta virtual. Nessa roleta você deve clicar no 
        botão "girar" e o aplicativo informará caso você tenha sido premiado. Os prêmios são vale-premmia, até 10000 pontos Premmia e 
        voucher de 2000 milhas. Você também recebe um número da sorte para concorrer a 10 anos de combustível grátis.
        
        Escreva um template de e-mail para ser enviado à seguinte base de clientes: {filtering_strategy}. O objetivo desse e-mail é 
        {focus}. A mensagem deve ter por volta de 700 caracteres, e deverá ser em formato de e-mail. {formality_prompt}. 
        Utilize as seguintes palavras-chave no e-mail: {keywords}.
        Seja pessoal e se dirija individualmente ao cliente, escrevendo '[nome do cliente]' no local onde o nome deve ficar, 
        e não utilize termos como "galera", "clientes" ou "vocês". Seja educado e não use palavrões.
        """

        llm_answer = llm(prompt)
        st.success(llm_answer)