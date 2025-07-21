import streamlit as st
import random
import string

st.title("Gerador de senhas Random")

tamanho = st.number_input('Quantidade de dígitos:', min_value=4, max_value=32, value=10)
usar_letras = st.checkbox('Letras', value=True)
usar_digitos = st.checkbox('Dígitos', value=True)
usar_simbolos = st.checkbox('Símbolos', value=True)


def gerar_senha(tamanho, usar_letras, usar_digitos, usar_simbolos):
    caracteres = ''
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_digitos:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Selecione pelo menos uma opção para gerar a senha."

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Inicializa a senha gerada na session_state
if 'senha_gerada' not in st.session_state:
    st.session_state['senha_gerada'] = ''

# Botão para gerar senha
if st.button('Gerar Senha'):
    st.session_state['senha_gerada'] = gerar_senha(tamanho, usar_letras, usar_digitos, usar_simbolos)
    st.success(f'{st.session_state["senha_gerada"]}')

# Exibe a senha gerada (sempre)
st.text_input('Senha', value=st.session_state['senha_gerada'], key='senha_field', disabled=True)

# Botão para limpar
if st.button('Limpar'):
    st.session_state['senha_gerada'] = ''
    st.success('Campos limpos!')




