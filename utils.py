
import pandas as pd

def carregar_historico():
    try:
        return pd.read_csv('historico.csv')
    except:
        return pd.DataFrame(columns=['Ativo','Tipo','Entrada','Saida','Tendencia'])

def salvar_historico(sinal):
    historico = carregar_historico()
    novo = pd.DataFrame(sinal, columns=['Ativo','Tipo','Entrada','Saida','Tendencia'])
    historico = pd.concat([historico, novo])
    historico.to_csv('historico.csv', index=False)

def calcular_assertividade(historico):
    if historico.empty:
        return 0
    acertos = historico[historico['Tendencia'].astype(float) > 70]
    return round((len(acertos) / len(historico)) * 100, 2)
