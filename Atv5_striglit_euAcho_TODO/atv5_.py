import streamlit as st
# python -m streamlit run {caminh relativo do arquivo python}
import pandas as pd #para aditar o visual


#Titulo------------------------
st.title("Notas 3ª etapa")

#cabeçario----------------------
st.subheader("3a1")

#st.write("Ola mundo!")

#input-------------------------
nome = st.text_input("Digite seu nome")
st.write("Olá ", nome," ,bem-vinde ao COTEMIG")

#DataFrame = tabela
df = pd.DataFrame({'diciplina': ["python","Matematica","Portugues"], 'nota':[10,5,0]})
df

st.write("A Prof.Eliza está brava, estuda mais Portugues")

#criando linha de separação
st.write("-------------------------------------------------------------------------")

#criando caxa de seleçao
selecao = st.selectbox("Selecione o que estudar:",["Portugues","Matematica","Python"])
st.write("Vc selecionou: ",selecao)

contador = 0
if st.button('Clique Aqui'):
    st.write("Vc clicou, ", contador)