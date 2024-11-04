import json
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_animation(file_path):
    """Carrega a animação Lottie a partir do arquivo JSON."""
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado: {file_path}")
        return None
    except json.JSONDecodeError:
        st.error(f"Erro ao decodificar o arquivo JSON: {file_path}")
        return None

def show():
    # Configura o título da página
    st.title("Bem-vindo ao Sistema de Checagem de Pulseiras! 🎉")

    # Adiciona subtítulo
    st.subheader("Controle de convidados para uma festa segura e exclusiva 👋")

    # Carrega animações
    animation_1 = load_lottie_animation("animaçoes/animation3.json")
    animation_2 = load_lottie_animation("animaçoes/animation5.json")

    if animation_1 and animation_2:
        # Configura layout em colunas
        col1, col2 = st.columns(2)

        # Conteúdo da coluna 1
        with col1:
            st_lottie(animation_1, height=350, width=350, key="animation1")
            st.markdown(
                """
                <div style='margin-top: 10px;'>
                    <h5 style='text-align: justify;'>Este sistema permite verificar se um convidado possui uma pulseira válida para entrada no evento. Evite entradas não autorizadas e garanta que apenas convidados registrados possam participar da festa.</h5>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Conteúdo da coluna 2
        with col2:
            st.markdown(
                """
                <div style='margin-top: 10px;'>
                    <h5 style='text-align: justify;'>Faça o check-in de convidados e verifique o status da pulseira para garantir a segurança e exclusividade do evento.</h5>
                </div>
                """,
                unsafe_allow_html=True
            )
            st_lottie(animation_2, height=350, width=350, key="animation2")

        # Adiciona um aviso
        st.markdown(
            """
            <div style='background-color: #d4edda; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #155724;'>Aviso:</h4>
                <p style='color: #155724;'>Este sistema é uma ferramenta de controle para eventos privados. Certifique-se de que todos os convidados tenham pulseiras válidas para evitar inconvenientes.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Não foi possível carregar as animações.")

if __name__ == "__main__":
    show()
