# 🎉 Sistema de Checagem de Pulseiras 🎟️

Bem-vindo ao **Sistema de Checagem de Pulseiras**, uma aplicação desenvolvida com **Streamlit** que permite gerenciar a entrada de convidados em eventos. Com este sistema, você pode autorizar convidados e garantir que apenas aqueles com pulseiras válidas entrem na festa. 🎊

## 🚀 Funcionalidades

- **Verificação de Convidados**: Permite verificar se um convidado está autorizado com base no número da pulseira. 
- **Lista de Convidados Autorizados**: Mostra todos os convidados que foram autorizados a entrar.
- **Reset para Testes**: Possibilita resetar o status de autorização para testes, facilitando o desenvolvimento e validação da aplicação.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Streamlit**: Framework utilizado para construir a interface da web.
- **Pandas**: Biblioteca utilizada para manipulação de dados.

## 📥 Pré-requisitos

Antes de executar o projeto, você precisa ter o Python e o pip instalados na sua máquina. Você pode verificar se já os possui com os seguintes comandos:

```bash
python --version
pip --version
```

### 🖥️ Instalação

Siga os passos abaixo para instalar e executar o projeto:

1. **Clone o repositório**:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
```

2. **Crie um ambiente virtual** (opcional, mas recomendado):

```bash
# Para Linux ou macOS
python3 -m venv venv
source venv/bin/activate

# Para Windows
venv\Scripts\activate
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

## 🔧 Executando o Projeto

Para iniciar a aplicação, utilize o seguinte comando:

```bash
streamlit run main.py
```

Isso abrirá a aplicação no seu navegador padrão. Você poderá acessar as funcionalidades de checagem de pulseiras e gerenciar os convidados. 🎈

## 📊 Estrutura do Projeto

```plaintext
projeto/
│
├── main.py                   # Arquivo principal para execução
├── pages/
│   ├── nav/
│   │   ├── check_in.py       # Lógica para checagem de pulseiras
│   │   └── list_guests.py    # Listagem de convidados autorizados
│   └── home.py               # Página inicial do projeto
├── static/
│   ├── styles.css            # Estilos da aplicação
│   └── animaçoes/            # Animações em JSON
├── utils/
│   ├── helpers.py            # Funções auxiliares
└── .gitignore                # Arquivo para ignorar arquivos indesejados
```

## 🤝 Contribuições

Contribuições são bem-vindas! Se você tem ideias para melhorias ou gostaria de corrigir um bug, sinta-se à vontade para abrir um **issue** ou enviar um **pull request**. 


## 📜 Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.


