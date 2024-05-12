#Matheus Audibert
#Resume_AI

import streamlit as st #Importa a biblioteca do STREAMLIT
import google.generativeai as genai #Importa a biblioteca da GOOGLE.GENERATIVEAI
import PyPDF2 #Importa a biblioteca do PYPDF2
import time #Importa a biblioteca TIME
import settings #Importa o aqruivo settings.py
from pdf_functions import ler_pdf, resume_pdf
from texto_functions import resume_texto

# @st.cache_data

#função principal
def main():

  st.set_page_config(page_title="Resume AI", layout="centered", initial_sidebar_state="auto", menu_items=None)

  with st.sidebar:

        st.markdown("""
        ### Bem-vindo ao **Resume AI**! ✅

        🤖 O **Resume AI** é uma ferramenta inovadora para resumir conteúdos de forma simples e eficaz.  Esta plataforma utiliza a IA generativa do Google 
        para extrair insights valiosos de textos e documentos em PDF.  Os usuários podem enviar os arquivos e obter resumos instantâneos, facilitando 
        o acesso rápido a informações importantes.

        #### Recursos:

        - 📦 **Upload Simples** Os usuários podem enviar arquivos (PDF) ou textos para análise. 
        - 💡 **Resumos Instantâneos:** O **Resume AI** alidado à IA generativa do Google permite aos usuários gerarem resumos precisos e quase instaneamente do conteúdo fornecido.
        - 😃 **Visualização Amigável**: Explore seus resumos de forma organizada e fácil de entender.
        - 📲 **Acesso em Qualquer Lugar**: Use nossa aplicação em qualquer dispositivo com acesso à internet.

        Junte-se ao **Resume AI** e libere o poder da inteligência para acessar conhecimentos valiosos de forma instantânea. A revolução da informação começa aqui! 🌐🤿

        ##### Feito por: Matheus Audibert 👨‍💻
        ##### Github: [github.com/matheusaudibert](github.com/matheusaudibert) 😼
        """)

  st.title("Resume AI ✍")

  input_method = st.radio("Selecione o método de entrada:", ('Enviar um documento', 'Digitar texto, palavra ou termo'))

  pdf = None
  texto = None
  
    
  if input_method == 'Enviar um documento':
    pdf = st.file_uploader("Envie um documento", type=['pdf'])


  if input_method == 'Digitar texto, palavra ou termo':
    texto = st.text_area("Digite um texto, palavra ou termo", "")
        
  chave_temp = st.text_input("Digite a chave da API 🔑")
          
  st.markdown('**Não tem uma chave?** Gere uma [aqui!](https://aistudio.google.com/app/apikey)')
  
  if st.button('Resumir (clique uma vez e espere)', type="primary"):
    
    with st.spinner('Verificando sua chave...'):
      time.sleep(1.5)
    if len(chave_temp) == 39:
      API_KEY = chave_temp
      genai.configure(api_key=API_KEY)
      with st.spinner('Conectando-se aos servidores do Google...'):
        time.sleep(1.5)
      if pdf == texto:
        st.write("✋ Calma aí! Me envie algo para resumir.")
      else:
        if pdf is not None:
          with st.spinner('Lendo o PDF...'):
            time.sleep(1.5)
          conteudo = ler_pdf(pdf)
          col1, col2, col3, col4 = st.columns(4)  
          col1.write("📄 Número de páginas:")
          col2.write(len(PyPDF2.PdfReader(pdf).pages))
          if conteudo == "0":
            st.toast('Erro ao gerar resumo!', icon="❌")
            st.write("🔌 Não consegui ler este PDF. Certifique-se de que o documento contenha textos.")
          else:
            with st.spinner('Anotando os pontos principais...'):
              time.sleep(1.5)
            with st.spinner('Resumindo...'):
              if len(PyPDF2.PdfReader(pdf).pages) > 5:
                st.toast('Lembre-se, PDFs com conteúdos extensos levam mais tempos para serem resumidos!', icon='⚠️')
              conteudo = resume_pdf(conteudo=conteudo)
              st.divider()
              st.write(conteudo)
              st.divider()
              st.toast('Resumo gerado!', icon="✅")

        if texto is not None:
          with st.spinner('Lendo o texo...'):
            time.sleep(1.5)
          with st.spinner('Anotando os pontos principais...'):
            time.sleep(2)
          with st.spinner('Resumindo...'):
            st.toast('Lembre-se, textos extensos levam mais tempos para serem resumidos!', icon='⚠️')
            resposta_texto = resume_texto(texto = texto)
          st.divider()
          st.write(resposta_texto)
          st.divider()
    else:
      st.markdown("❌ Vish, deu ruim! parece que sua chave não funcionou.")

  on = st.toggle("Mostrar parâmetros da IA. (Personalizável no futuro)")

  if on:
    st.caption("Temperatura")
    st.slider("", 0.0, 1.0, 0.2, disabled=True)
    st.caption("Top P")
    st.slider("", 0.0, 1.0, 1.0, disabled=True)
    st.caption("Top K")
    st.slider("", 0.0, 50.0, 0.0, disabled=True)
    st.markdown("Para saber mais sobre parâmetros de IA, acesse [aqui!](https://cloud.google.com/vertex-ai/generative-ai/docs/text/test-text-prompts?hl=pt-br#generative-ai-test-text-prompt-python_vertex_ai_sdk)")

  st.caption("Versão: 0.3")
      
if __name__ == "__main__":
    main()
