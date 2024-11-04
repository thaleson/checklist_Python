import pandas as pd

def load_convidados(file_path="data/convidados.csv"):
    # Carrega o CSV e garante que a coluna seja tratada como inteiro
    convidados = pd.read_csv(file_path)
    convidados['pulseira'] = convidados['pulseira'].astype(int)
    return convidados

def check_pulseira(pulseira, convidados):
    pulseira = int(pulseira)  # Converte a entrada para inteiro
    # Verifica se a pulseira existe no CSV
    if pulseira in convidados['pulseira'].values:
        status = convidados.loc[convidados['pulseira'] == pulseira, 'autorizado'].values[0]
        if status == "Sim":
            return "Pulseira já autorizada e convidado já está na festa!"
        else:
            # Marca a pulseira como autorizada
            convidados.loc[convidados['pulseira'] == pulseira, 'autorizado'] = "Sim"
            # Salva a atualização no CSV
            convidados.to_csv("data/convidados.csv", index=False)
            return "Convidado autorizado com sucesso!"
    else:
        return "Pulseira não autorizada!"
