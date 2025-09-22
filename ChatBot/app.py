# titulo
# input do chat
# a cada mensagem enviada:
    # mostra a mensagem que o ususario enviou no chat
    # envia essa mensagem para a IA responder
    # reposta na tela
    
# streamlit -front e -backend


import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="CHAVE_API")

st.write("# Papo com a IA") #markdown

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []
    
# session_state = ["lista_mensagens"].append(mensagem)
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Digite aqui sua mensagem")

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)
    
    resposta_modelo = modelo.chat.completions.create(
       messages=st.session_state["lista_mensagens"],
       model ="gpt-4o"
    )
    print(resposta_modelo)
    resposta_ia = resposta_modelo.choices[0].message.content
    
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
    
    


