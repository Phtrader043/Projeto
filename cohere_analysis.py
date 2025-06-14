
import cohere
from config import API_COHERE

co = cohere.Client(5dzTGoR9jOnUcKrfOujxklCCwEtZuEVc4cBpJmQb)

def analisar_tendencia(dados, modo):
    prompt = f"Analise estes dados {dados} e gere um sinal altamente preciso no modo {modo}. Retorne formato: Ativo, Tipo, Entrada, Saída, Tendência%"
    response = co.generate(model='command', prompt=prompt, max_tokens=100)
    texto = response.generations[0].text
    linhas = texto.strip().split("\n")
    resultado = [linha.split(",") for linha in linhas if linha]
    return resultado
