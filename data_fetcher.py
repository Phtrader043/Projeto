
import requests
from config import API_TWELVE, FOREX_ATIVOS, CRIPTO_ATIVOS

def obter_dados():
    ativos = FOREX_ATIVOS + CRIPTO_ATIVOS
    dados = []
    for ativo in ativos:
        url = f"https://api.twelvedata.com/time_series?symbol={ativo}&interval=1min&apikey={API_TWELVE}"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            dados.append({ativo: data})
    return dados
