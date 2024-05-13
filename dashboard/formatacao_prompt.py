import streamlit as st
import google.generativeai as genai
import PyPDF2
import PIL
import docx2txt
 

def verifica_chave(chave_temp):
    if len(chave_temp) == 39:
      API_KEY = chave_temp
      genai.configure(api_key=API_KEY)
      return True
    else:
      return False

def ler_pdf(upload_arquivo):
  output_arquivo = ""

  for page_num in range(len(PyPDF2.PdfReader(upload_arquivo).pages)):
    output_arquivo += PyPDF2.PdfReader(upload_arquivo).pages[page_num].extract_text()

  if len(PyPDF2.PdfReader(upload_arquivo).pages) >= 20:
    st.toast('Lembre-se, PDFs com conteúdos extensos levam mais tempos para serem resumidos!', icon='⚠️')

  if output_arquivo == "":
    st.toast('Erro ao gerar resumo!', icon="❌")
    st.write("🔌 Não consegui ler este PDF. Certifique-se de que o documento contenha textos.")
  
  return output_arquivo

def ler_docx(upload_arquivo):
  output_arquivo = docx2txt.process(upload_arquivo)
  
  if output_arquivo == "":
    st.toast('Erro ao gerar resumo!', icon="❌")
    st.write("🔌 Não consegui ler este DOCX. Certifique-se de que o documento contenha textos.")

  return output_arquivo

def ler_txt(upload_arquivo):
  output_arquivo = str(upload_arquivo.read(), "utf-8")

  if output_arquivo == "":
    st.toast('Erro ao gerar resumo!', icon="❌")
    st.write("🔌 Não consegui ler este TXT. Certifique-se de que o documento contenha textos.")

  return output_arquivo

def ler_imagem(upload_arquivo):
  output_arquivo = PIL.Image.open(upload_arquivo)

  return output_arquivo