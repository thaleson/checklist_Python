import streamlit as st
from utils.helpers import load_convidados
import pandas as pd

def list_guests_page():
    st.title("Lista de Convidados Autorizados")
    
    # Carrega a lista de convidados autorizados
    convidados = load_convidados()
    
    # Exibe a lista na interface
    st.write(convidados)
    
    # Adiciona o botão de reset
    if st.button("Reseta Lista de Convidados"):
        # Reseta todos os valores da coluna 'autorizado' para 'Não'
        convidados['autorizado'] = "Não"
        convidados.to_csv("data/convidados.csv", index=False)
        
        # Atualiza a exibição da lista
        st.success("Lista de convidados resetada com sucesso!")
        st.write(convidados)  # Mostra a lista resetada

# Executa a página de listagem de convidados
if __name__ == "__main__":
    list_guests_page()
