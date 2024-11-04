import streamlit as st
from utils.helpers import load_convidados, check_pulseira

def check_in_page():
    st.title("Checar Pulseira")

    # Carrega a lista de convidados
    convidados = load_convidados()

    # Input para o número da pulseira
    pulseira = st.text_input("Digite o número da pulseira:")

    # Verificação da pulseira ao clicar no botão
    if st.button("Verificar"):
        if pulseira.isdigit():
            resultado = check_pulseira(pulseira, convidados)
            st.success(resultado) if "sucesso" in resultado else st.warning(resultado)
        else:
            st.error("Por favor, digite um número válido para a pulseira.")
