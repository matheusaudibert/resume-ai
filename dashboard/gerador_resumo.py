import google.generativeai as genai #Importa a biblioteca GOOGLE.GENERATIVEAI
import settings

def resumir_imagem(output_arquivo):

  generation_config = {
  "temperature": 1.0,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 100000,
  }
  
  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                safety_settings=settings.safety_settings)
    
  resposta = model.generate_content(["""
   Você é uma ferramenta que gera resumo ou explicações de imagens.\n
   Ao identificar uma imagem, gere um resumo preciso e detlhado, porém fácil de ler, sobre conteúdo daquela imagem.\n
   Use tópicos pontuando os pontos principais e se possível gere insights.\n
   Se for incapaz de se interpreta, responda que não foi possível interpretar a imagem.\n\n
   Ao final, gere uma nota, dizendo que a interpretações de imagens é subjetiva.\n
   A partir disso, faça um resumo detalhado sobre o conteúdo desta imagem:""", output_arquivo])

  return resposta.text

def resumir_texto(output_arquivo):

  generation_config = {
  "temperature": 1.0,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 100000,
  }
  
  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                safety_settings=settings.safety_settings)
    
  resposta = model.generate_content(["""
   Leia todos o conteúdo do texto fornecido.\n
   Determine qual é o assunto geral do documento e resuma-o.\n
   Sintetize as informações em uma sinopse bem formatada e fácil de ler, estruturada como um ensaio que as resume de forma coesa.\n
   Não simplesmente parafraseie o texto fornecido.\n
   Não copie a estrutura do texto fornecido.\n
   Evite repetições.\n
   Conecte todas as ideias entre si.\n
   Antes da sinopse, escreva uma lista sucinta em formato de tópicos das principais conclusões.\n
   O texto deve ser dividido em parágrafos.\n
   Os parágrafos devem ser indentados.\n\n
   Se o conteúdo fornecido não for um texto, e sim uma palavra, um nome, um termo, um fato histórico, etc. Você deve fornecer uma explicação este conteúdo inserido pelo usuário.\n
   Caso o conteúdo fornecido pelo usuário for incapaz de ser interpreta, solicite ao usuário que entre com mais informações.\n\n
   A partir disso, faça um resumo sobre o conteúdo deste texto:""", output_arquivo])

  return resposta.text
  