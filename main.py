import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json

# Configuração da página principal
st.set_page_config(page_title="Verificação de Pulseiras", page_icon="🎫")

# Carrega o CSS personalizado
st.markdown(
    f"""
    <style>
    {open("static/styles.css").read()}
    </style>
    """,
    unsafe_allow_html=True
)

# Carregar animação para a barra lateral
with open("animaçoes/animation4.json") as source:
    animacao_1 = json.load(source)

# Menu de navegação com animação
with st.sidebar:
    # Exibe animação
    st_lottie(animacao_1, height=200, width=270)

    # Cria o menu de navegação
    selected = option_menu("Menu", ["Home","Checar Pulseira", "Listar Convidados"],
                           icons=['house','check-circle', 'list-ul'], 
                           menu_icon="cast", default_index=0)

    # Badges de redes sociais
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between;">
            <div>
                <a href="https://github.com/thaleson" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" width="100" />
                </a>
            </div>
            <div>
                <a href="https://www.linkedin.com/in/thaleson-silva-9298a0296/" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="100" />
                </a>
            </div>
            <div>
                <a href="mailto:thaleson177@gmail.com" target="_blank">
                    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" width="80" />
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Navegação entre as páginas
if selected == "Checar Pulseira":
    from pages.nav.check_in import check_in_page
    check_in_page()
elif selected == "Listar Convidados":
    from pages.nav.list_guests import list_guests_page
    list_guests_page()

elif selected == "Home" :
    from pages.nav.home import show 
    show()
