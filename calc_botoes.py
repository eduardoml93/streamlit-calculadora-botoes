import streamlit as st

# Função para adicionar dígitos e operações à expressão
def add_to_expression(symbol):
    if st.session_state['expression'] == '0':
        st.session_state['expression'] = symbol
    else:
        st.session_state['expression'] += symbol

# Função para calcular a expressão
def calculate_expression():
    try:
        result = eval(st.session_state['expression'])
        st.session_state['expression'] = str(result)
    except:
        st.session_state['expression'] = 'Error'

# Função para limpar a expressão
def clear_expression():
    st.session_state['expression'] = '0'

# Inicializando a expressão na sessão do Streamlit
if 'expression' not in st.session_state:
    st.session_state['expression'] = '0'

st.title("Calculadora Simples com Botões")

# Display da expressão atual
st.text_input("Expressão", st.session_state['expression'], key="expression_display")

# Botões da calculadora
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button('7', on_click=add_to_expression, args=('7',)):
        pass
    if st.button('4', on_click=add_to_expression, args=('4',)):
        pass
    if st.button('1', on_click=add_to_expression, args=('1',)):
        pass
    if st.button('0', on_click=add_to_expression, args=('0',)):
        pass

with col2:
    if st.button('8', on_click=add_to_expression, args=('8',)):
        pass
    if st.button('5', on_click=add_to_expression, args=('5',)):
        pass
    if st.button('2', on_click=add_to_expression, args=('2',)):
        pass
    if st.button('.', on_click=add_to_expression, args=('.',)):
        pass

with col3:
    if st.button('9', on_click=add_to_expression, args=('9',)):
        pass
    if st.button('6', on_click=add_to_expression, args=('6',)):
        pass
    if st.button('3', on_click=add_to_expression, args=('3',)):
        pass
    if st.button('=', on_click=calculate_expression):
        pass

with col4:
    if st.button('SOMA', on_click=add_to_expression, args=('+',)):
        pass
    if st.button('SUBTRAÇÃO', on_click=add_to_expression, args=('-',)):
        pass
    if st.button('MULTIPLICAÇÃO', on_click=add_to_expression, args=('*',)):
        pass
    if st.button('DIVISÃO', on_click=add_to_expression, args=('/',)):
        pass

if st.button('CLEAR', on_click=clear_expression):
    pass
