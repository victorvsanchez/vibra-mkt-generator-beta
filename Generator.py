import streamlit as st

st.set_page_config(page_title="Vibra - Gerador de Emails de Campanha", layout="centered", initial_sidebar_state="auto", menu_items=None)

#Text about the campaign strategy
filtering_strategy = st.text_input("Explique a estratégia de filtro de clientes usada:", "")

#Marketing campaign focus dropdown
options1 = ["Maximizar abertura de e-mails", 
            "Maximizar compras no app", 
            "Maximizar compras locais",
            "Maximizar resgate de pontos"]
focus = st.selectbox("Selecione o foco da campanha:", option1)

#Language type dropdown
options2 = ["Formal", "Informal"]
formality = st.selectbox("Selecione o tipo de linguagem a ser usado:", options)

# Button to trigger the action
if st.button("Gerar campanha"):
    # Perform some action with the entered information and selected option
    st.success(f"Crie uma campanha de marketing para a seguinte base de clientes: {filtering_strategy}. O foco da campanha é {focus}, e a linguagem usada deve ser {formality}")