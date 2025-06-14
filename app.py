
import streamlit as st
from signal_engine import gerar_sinal
from utils import carregar_historico, salvar_historico, calcular_assertividade

st.set_page_config(page_title="Indicador GPT - Cripto & Forex", layout="wide")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://i.imgur.com/waxVImv.png");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Indicador GPT - Cripto & Forex')

modo = st.sidebar.radio("Escolha o Modo:", ["Conservador", "Agressivo"])

if st.button('🚀 Ativar IA'):
    with st.spinner('Buscando sinais...'):
        sinal = gerar_sinal(modo)
        if sinal:
            st.success('✅ Sinal Gerado com Sucesso!')
            st.subheader('🔔 Sinal Atual')
            st.table(sinal)

            salvar_historico(sinal)
        else:
            st.warning('⚠️ Nenhum sinal confiável encontrado no momento.')

st.subheader('📜 Histórico de Sinais')
historico = carregar_historico()
st.dataframe(historico)

st.subheader('📈 Índice de Assertividade')
assertividade = calcular_assertividade(historico)
st.metric(label="Assertividade (%)", value=f"{assertividade}%")
