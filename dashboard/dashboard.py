#Matheus Audibert
#Resume_AI

import streamlit as st
import PIL
import time
from formatacao_prompt import verifica_chave, ler_pdf, ler_docx, ler_txt, ler_imagem
from gerador_resumo import resumir_imagem, resumir_texto

#função principal
def main():

  st.set_page_config(page_title="Resume AI", layout="centered", initial_sidebar_state="auto", menu_items=None)

  with st.sidebar:

        st.markdown("""
        ### Bem-vindo ao **Resume AI**! ✅

        🤖 O **Resume AI** é uma ferramenta inovadora para resumir conteúdos de forma simples e eficaz.  Esta plataforma utiliza a IA generativa do Google 
        para extrair insights valiosos de imagens, documentos e textos.  Os usuários podem enviar os arquivos e obter resumos instantâneos, facilitando 
        o acesso rápido a informações importantes.

        #### Recursos:

        - 📦 **Upload Simples:** Os usuários podem enviar imagens (png, jpg ou jpeg), documentos (pdf, docx ou txt) ou até mesmo digitar seu próprio texto. 
        - 💡 **Resumos Instantâneos:** O Resume AI alidado à inteligência artificial generativa do Google permite aos usuários gerarem resumos precisos e instantâneos do conteúdo fornecido.
        - 😃 **Visualização Amigável:** Explore seu resumo de forma organizada e fácil de entender.
        - 📲 **Acesso em Qualquer Lugar:** Use a aplicação em qualquer dispositivo com acesso à internet.

        Junte-se ao **Resume AI** e libere o poder da inteligência artificial para acessar conhecimentos valiosos de forma instantânea. A revolução da informação começa aqui! 🌐🤿

        ##### Feito por: Matheus Audibert 👨‍💻
        ##### Github: [github.com/matheusaudibert](github.com/matheusaudibert) 😼
        """)

  tab_padrao, tab_for_developers = st.tabs(["Padrão", "for developers"])

  with tab_padrao:
    st.title("Resume AI ✍")

    input_method = st.radio("Selecione o método de entrada:", ('Enviar um documento (pdf, docx, txt)','Inserir uma imagem', 'Digitar texto, palavra ou termo'))
    
    upload_arquivo = None  
    upload_arquivo_texto = ""
      
    if input_method == 'Enviar um documento (pdf, docx, txt)':
      upload_arquivo = st.file_uploader("Envie um documento", type=['pdf', 'docx', 'txt'])

    if input_method == 'Inserir uma imagem':
      upload_arquivo = st.file_uploader("Envie um documento", type=['png', 'jpg', 'jpeg'])

    if input_method == 'Digitar texto, palavra ou termo':
      upload_arquivo_texto = st.text_area("Digite um texto, palavra ou termo", "")
      
          
    chave_temp = st.text_input("Digite a chave da API 🔑")
            
    st.markdown('**Não tem uma chave?** Gere uma [aqui!](https://aistudio.google.com/app/apikey)')
    
    if st.button('Resumir (clique uma vez e espere)', type="primary"):    
      with st.spinner('🔎 Verificando sua chave...'):
        time.sleep(1.5)
      if verifica_chave(chave_temp) is True:
        with st.spinner('🚀 Conectando-se aos servidores do Google...'):
          time.sleep(1.5)
        if upload_arquivo is not None:
          if upload_arquivo.type == 'application/pdf':
            with st.spinner('👀 Lendo o PDF...'):
              time.sleep(1.5)
              output_arquivo = ler_pdf(upload_arquivo)
            
          if upload_arquivo.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            with st.spinner('👀 Lendo o DOCX...'):
              time.sleep(1.5)
              output_arquivo = ler_docx(upload_arquivo)

          if upload_arquivo.type == 'text/plain':
            with st.spinner('👀 Lendo o TXT...'):
              time.sleep(1.5)
              output_arquivo = ler_txt(upload_arquivo)

          if upload_arquivo.type == 'image/png' or upload_arquivo.type == 'image/jpeg':
            with st.spinner('👀 Lendo a imagem...'):
              time.sleep(1.5)
              output_arquivo = ler_imagem(upload_arquivo)
          
        elif upload_arquivo_texto != "":
          with st.spinner('👀 Lendo o texto...'):
            time.sleep(1.5)
            output_arquivo = upload_arquivo_texto
        else:
          st.write("✋ Calma aí! Envie-me algo para resumir.")
          
        
        if upload_arquivo is not None:
          if upload_arquivo.type == 'image/png' or upload_arquivo.type == 'image/jpeg':
            with st.spinner('📝 Resumindo...'):
              time.sleep(1.5)
              resposta = resumir_imagem(output_arquivo)
              st.toast('Resumo gerado com sucesso!', icon="✅")
              st.divider()
              st.write(resposta)
              st.write("Imagem:")
              st.image(output_arquivo, width=300)
              st.divider()

          if output_arquivo != "":
            if upload_arquivo.type != 'image/png' and upload_arquivo.type != 'image/jpeg':
              with st.spinner('📝 Resumindo...'):
                time.sleep(1.5)
                resposta = resumir_texto(output_arquivo)
                st.toast('Resumo gerado com sucesso!', icon="✅")
                st.divider()
                st.write(resposta)
                st.divider()
            
        if upload_arquivo_texto != "":
          with st.spinner('📝 Resumindo...'):
            time.sleep(1.5)
            resposta = resumir_texto(output_arquivo)
            st.toast('Resumo gerado com sucesso!', icon="✅")
            st.divider()
            st.write(resposta)
            st.divider()
        
      else:
        st.markdown("❌ Vish, deu ruim! parece que sua chave não funcionou.")

    on = st.toggle("Mostrar parâmetros da IA.")

    if on:
      st.caption("Temperatura")
      st.slider("", 0.0, 1.0, 1.0, disabled=True)
      st.caption("Top P")
      st.slider("", 0, 1, 1, disabled=True)
      st.caption("Top K")
      st.slider("", 0, 50, 0, disabled=True)
      st.markdown("Para saber como os parâmetros funcionam, clique [aqui!](https://cloud.google.com/vertex-ai/generative-ai/docs/text/test-text-prompts?hl=pt-br#generative-ai-test-text-prompt-python_vertex_ai_sdk)")

    st.caption("Versão: 0.7")
    st.markdown("""Repositório do projeto no [Github.](github.com/matheusaudibert/resume_ai)""")

  with tab_for_developers:

    st.title("Resume AI 👩‍💻 :red[*for developers*]")
    st.write("Estará disponpivel na versão 1.0!")

    if st.button("🤿 Clique aqui!", type='primary'):
      with st.spinner('🔨 Este módulo ainda está em construção...'):
        time.sleep(5)
      with st.spinner('📚 Importando bibliotecas necessárias...'):
        time.sleep(5)
      with st.spinner('👀 Lendo documentações...'):
        time.sleep(5)
      with st.spinner('🧩 Definindo as funções...'):
         time.sleep(5)
      with st.spinner('👥 Reaproveitando códigos...'):
        time.sleep(5)
      with st.spinner('👨‍💻 Programando...'):
        time.sleep(5)
      with st.spinner('☕ Tomando um  cafézinho...'):
        time.sleep(5)
      with st.spinner('🤨 Você ainda está aqui?'):
         time.sleep(60)
      
if __name__ == "__main__":
    main()
