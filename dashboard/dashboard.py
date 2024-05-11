import streamlit as st
import google.generativeai as genai
import settings
import PyPDF2


@st.cache_data

def resume_texto (texto: str):
   
    generation_config = {
    "temperature": 0.2,
    "top_p": 1,
    "top_k": 0,
    "max_output_tokens": 100000,
    }
    system_instruction = "Você é um ferramenta focada na construção de resumos. Sua função é fazer resumos conciso e claros, de diversos conteúdos."
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=settings.safety_settings)
    
    convo = model.start_chat(history=[
                    {
                    "role": "user",
                    "parts": ["""Você é uma ferramenta de resumos de textos palavras ou termos. Determine do que se trata o documento geral e resuma-o.\n
                                Sintetize as informações em um resumo bem formatado e fácil de ler, estruturado como um ensaio que as resuma de forma coesa.\n
                                Não simplesmente repita o texto fornecido. Não copie a estrutura do texto fornecido.\n
                                Evite repetições. Conecte todas as ideias entre si.\n
                                Antes do resumo, escreva uma lista curta e em formato de tópicos dos principais pontos a serem lembrados.\n
                                O texto deve ser dividido em parágrafos. Os parágrafos devem ser indentados.\n\n
                                Exemplo:\n\n
                                A Guerra do Japão é um termo amplo que pode se referir a várias guerras nas quais o Japão esteve envolvido ao longo de sua história. No contexto moderno, a Guerra do Japão geralmente se refere às guerras que o Japão travou durante o século XX, especialmente durante a Segunda Guerra Mundial. Abaixo, vou gerar um texto detalhado sobre esse período da história japonesa:\n\n
                                A história militar do Japão durante o século XX é marcada por uma série de conflitos significativos, sendo a Segunda Guerra Mundial um dos períodos mais intensos e controversos. O Japão emergiu como uma potência imperial no início do século XX, ansioso por expandir seu domínio na Ásia e no Pacífico. Essa expansão resultou em conflitos militares brutais que deixaram um legado duradouro.\n\n
                                Uma das primeiras campanhas militares importantes foi a Guerra Russo-Japonesa de 1904-1905, onde o Japão emergiu vitorioso, demonstrando sua capacidade militar modernizada ao derrotar a Rússia imperial. Isso solidificou o Japão como uma potência regional e teve implicações significativas no cenário internacional.\n\n
                                Durante a Segunda Guerra Mundial, o Japão se envolveu em uma série de conflitos em várias frentes. A invasão da Manchúria em 1931 marcou o início da expansão agressiva japonesa na Ásia. Em 1937, a invasão em grande escala da China pelo Japão desencadeou a Segunda Guerra Sino-Japonesa, um conflito prolongado e brutal que deixou milhões de mortos e contribuiu para o desenrolar da Segunda Guerra Mundial na região do Pacífico.\n\n
                                O ataque surpresa à base naval dos Estados Unidos em Pearl Harbor, no Havaí, em 7 de dezembro de 1941, marcou a entrada do Japão na Segunda Guerra Mundial. Isso levou os Estados Unidos e seus aliados a retaliarem contra o Japão em uma série de batalhas épicas no teatro do Pacífico, incluindo as batalhas de Midway, Guadalcanal, Iwo Jima e Okinawa.\n\n
                                A guerra no Pacífico foi caracterizada por uma ferocidade extrema de ambos os lados, com combates brutais na terra, no mar e no ar. O Japão empregou táticas de guerra inovadoras, incluindo o uso de kamikazes (pilotos suicidas) e defesas fortificadas em ilhas. No entanto, a crescente superioridade militar e industrial dos Aliados, especialmente dos Estados Unidos, eventualmente levou ao colapso do Japão.\n\n
                                O conflito chegou ao fim em agosto de 1945, com os bombardeios atômicos de Hiroshima e Nagasaki pelos Estados Unidos, que causaram um grande número de mortes e levaram à rendição incondicional do Japão em setembro de 1945, marcando o fim da Segunda Guerra Mundial.\n\n
                                A Guerra do Japão deixou um legado complexo e doloroso para o país. Além das perdas humanas e da devastação material, o Japão enfrentou um período de ocupação pelos Aliados liderados pelos Estados Unidos, seguido por um processo de reconstrução e transformação que moldou a sociedade japonesa moderna.\n\n


                                """]
                    },
                    {
                    "role": "model",
                    "parts": ["""Principais pontos a serem lembrados:\n\n
                                Expansão Imperial: O Japão emergiu como uma potência imperial no início do século XX, buscando expandir seu domínio na Ásia e no Pacífico.\n\n
                                Conflitos Significativos: A história militar do Japão no século XX é marcada por conflitos importantes, incluindo a Guerra Russo-Japonesa e a Segunda Guerra Mundial.\n\n
                                Segunda Guerra Mundial: O Japão participou em várias frentes da Segunda Guerra Mundial, incluindo a invasão da Manchúria, a Segunda Guerra Sino-Japonesa e o ataque a Pearl Harbor.\n\n
                                Batalhas no Teatro do Pacífico: A guerra no Pacífico foi caracterizada por batalhas épicas como Midway, Guadalcanal, Iwo Jima e Okinawa, com táticas inovadoras empregadas pelo Japão.\n\n
                                Desfecho: O conflito culminou com os bombardeios atômicos de Hiroshima e Nagasaki e a rendição do Japão em setembro de 1945.\n\n
                                Legado: A Guerra do Japão deixou um legado complexo, incluindo ocupação pelos Aliados e um processo de reconstrução e transformação.\n\n
                                A história militar do Japão no século XX é uma narrativa marcada por conflitos e ambições imperiais. Durante esse período, o Japão emergiu como uma potência regional ansiosa por expandir seu domínio na Ásia e no Pacífico. Esta expansão resultou em uma série de guerras que deixaram um legado duradouro e complexo para o país.\n\n
                                Uma das primeiras campanhas militares importantes foi a Guerra Russo-Japonesa de 1904-1905, na qual o Japão demonstrou sua capacidade militar modernizada ao derrotar a Rússia imperial, solidificando sua posição como uma potência regional.\n\n
                                Durante a Segunda Guerra Mundial, o Japão se envolveu em conflitos em várias frentes, iniciando com a invasão da Manchúria em 1931 e posteriormente com a Segunda Guerra Sino-Japonesa em 1937. O ataque a Pearl Harbor em 1941 marcou a entrada do Japão no conflito global, desencadeando uma série de batalhas no teatro do Pacífico, incluindo confrontos decisivos em Midway, Guadalcanal, Iwo Jima e Okinawa.\n\n
                                A guerra no Pacífico foi caracterizada por uma intensidade extrema, com o Japão empregando táticas inovadoras como kamikazes e defesas fortificadas em ilhas. No entanto, a crescente superioridade militar e industrial dos Aliados, especialmente dos Estados Unidos, eventualmente levou ao colapso do Japão.\n\n
                                O desfecho desse período sombrio veio com os devastadores bombardeios atômicos de Hiroshima e Nagasaki em agosto de 1945, seguidos pela rendição incondicional do Japão em setembro do mesmo ano. Após a guerra, o Japão enfrentou um período de ocupação pelos Aliados liderados pelos Estados Unidos, que moldou a sociedade japonesa moderna por meio de um processo de reconstrução e transformação.\n\n
                                A Guerra do Japão, portanto, deixou um legado marcado por perdas humanas, devastação material e transformações sociais, que continuam a influenciar o Japão até os dias de hoje."""]
                    },
                    {
                    "role": "user",
                    "parts": [""""Quando há entradas sem muito contexto, como por exemplo, Gripe Espanhola, você deve redigir um Resumo sobre o conteúdo, seguindo as regras ditas."""]
                    },
                    {
                    "role": "model",
                    "parts": [""""Principais pontos a serem lembrados:\n\n
                                Origem e Propagação: A Gripe Espanhola foi uma pandemia de gripe que ocorreu em 1918-1919, durante o final da Primeira Guerra Mundial.\n\n
                                Gravidade e Mortalidade: Foi uma das pandemias mais mortais da história, causando milhões de mortes em todo o mundo.\n\n
                                Características: A gripe se espalhou rapidamente devido às condições da guerra e à movimentação de tropas.\n\n
                                Impacto Global: Afetou indiscriminadamente pessoas em todas as faixas etárias e regiões do mundo.\n\n
                                Desfecho: A pandemia eventualmente diminuiu após algumas ondas e deixou um impacto duradouro na saúde pública e na consciência global.\n\n
                                A Gripe Espanhola foi uma pandemia de gripe que ocorreu entre 1918 e 1919, coincidindo com o final da Primeira Guerra Mundial. Originou-se em circunstâncias ainda não totalmente compreendidas, mas se espalhou rapidamente em um mundo abalado pela guerra e por grandes movimentações populacionais.\n\n
                                Essa pandemia foi uma das mais devastadoras da história moderna, causando um número estimado de 50 a 100 milhões de mortes em todo o mundo. O vírus era altamente contagioso e mortal, afetando gravemente pessoas em todas as faixas etárias e em todas as regiões do globo.\n\n
                                Um dos aspectos mais notáveis da Gripe Espanhola foi sua severidade e velocidade de propagação. A pandemia foi exacerbada pelas condições da guerra, com a mobilização de tropas e grandes aglomerações facilitando a disseminação do vírus.\n\n
                                Apesar de seu nome, a Gripe Espanhola não se originou na Espanha. No entanto, o país foi um dos primeiros a relatar abertamente os casos, já que não estava envolvido diretamente na guerra e, portanto, não censurou informações como outras nações. Isso levou a uma falsa impressão de que a gripe havia começado na Espanha.\n\n
                                A pandemia teve múltiplas ondas ao longo de 1918 e 1919, diminuindo gradualmente à medida que o vírus se adaptava e a imunidade da população aumentava. A Gripe Espanhola deixou um legado significativo na saúde pública e na consciência global sobre os riscos das pandemias, influenciando diretamente as políticas de saúde pública e os sistemas de vigilância epidemiológica que conhecemos hoje.\n\n"""]
                    }
                    ]           
                            )
    
    convo.send_message(f"""Faça um resumo, sobre: \n\n{texto}. Incie com um título, informando que se trata de um resumo.""")

    resposta_texto = convo.last.text

    return resposta_texto


def resume_pdf (conteudo:str):
  generation_config = {
  "temperature": 0.2,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 100000,
  }
   
  system_instruction = "Você é um ferramenta focada na construção de resumos. Sua função é fazer resumos conciso e claros de PDFs."
  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=settings.safety_settings)
   
  convo = model.start_chat(history=[
                    {
                    "role": "user",
                    "parts": ["""Você irá fazer resumos de textos NÃO formatados. Por isso deve ler os textos e extrair resumos fortadados, claros e concisos. Você deve funcionar da seguinte maneira. \n
                                Usuário entra um texto não formatado:"\n
                                A Alura é uma plataforma brasileira de ensino online que oferece uma ampla variedade de  
                                cursos nas áreas de tecnologia, programação, design, negócios e desenvolvimento pessoal.  
                                Fundada em 2011, a Alura tem como objetivo principal proporcionar aprendizado prático e de  
                                qualidade, alinhado com as demandas do mercado de trabalho atual.
                                Os cursos da Alura são desenvolvidos por especialistas e proﬁssionais experientes em suas  
                                respectivas áreas, garantindo conteúdo atualizado e relevante. A plataforma oferece uma  
                                abordagem prática de aprendizado, com aulas interativas, exercícios desaﬁadores e projetos  
                                práticos que permitem aos alunos aplicar imediatamente o conhecimento adquirido."""]
                    },
                    {
                    "role": "model",
                    "parts": ["""Principais Pontos a Serem Lembrados:\n\n
                                A Alura é uma plataforma brasileira de ensino online fundada em 2011.\n
                                Oferece uma variedade de cursos em tecnologia, programação, design, negócios e desenvolvimento pessoal.\n
                                Os cursos são criados por especialistas e profissionais experientes.\n
                                A abordagem de aprendizado é prática, com aulas interativas, exercícios desafiadores e projetos práticos.\n
                                A Alura é uma renomada plataforma brasileira de ensino online, fundada em 2011 com o propósito de proporcionar aprendizado prático e de qualidade alinhado às exigências do mercado atual. Seu catálogo diversificado abrange cursos nas áreas de tecnologia, programação, design, negócios e desenvolvimento pessoal.\n\n
                                Os cursos oferecidos pela Alura são meticulosamente elaborados por especialistas e profissionais experientes em cada respectiva área, assegurando conteúdo atualizado e relevante para os alunos. O diferencial da plataforma reside na abordagem prática de aprendizado, destacando-se por aulas interativas que incentivam a participação ativa dos alunos, exercícios desafiadores que promovem o aprofundamento dos conhecimentos adquiridos e projetos práticos que possibilitam a aplicação imediata das habilidades aprendidas em cenários reais.\n\n
                                Em resumo, a Alura se destaca como uma plataforma de ensino online que não apenas oferece cursos abrangentes em diversas áreas essenciais para o mercado contemporâneo, mas também se compromete em proporcionar uma experiência de aprendizado dinâmica e envolvente."""]
                    },
                    ]
                            )
    
  convo.send_message(f"""Faça um resumo sobre este texto: {conteudo}""")

  resposta_pdf = convo.last.text

  return resposta_pdf


def ler_pdf(pdf):
  leitor_pdf = PyPDF2.PdfReader(pdf)
  num_pages = len(leitor_pdf.pages)
  conteudo = ""
  for page_num in range(num_pages):
    conteudo += leitor_pdf.pages[page_num].extract_text()
  return conteudo



def main():
    st.title("Resume AI ✍️")

    input_method = st.radio("Selecione o método de entrada:", ('Enviar um documento (PDF)', 'Digitar texto, palavra ou termo'))

    pdf = None
    texto = None
    
    if input_method == 'Enviar um documento (PDF)':
      pdf = st.file_uploader("Envie um documento", type=['pdf'])


    if input_method == 'Digitar texto, palavra ou termo':
        texto = st.text_area("Digite um texto, palavra ou termo", "")
        if texto:
            resposta_texto = resume_texto(texto = texto)
            st.divider()
            st.write(resposta_texto)

    if pdf is not None:
        conteudo = ler_pdf(pdf)
        conteudo = resume_pdf(conteudo=conteudo)
        st.divider()
        st.write(conteudo)

    API_KEY = st.text_input("Digite a chave da API 🔑")
    genai.configure(api_key=API_KEY)
    

    if st.button("Salvar chave", type="secondary"):
        if len(API_KEY) > 35:
            if len(API_KEY) < 42:
                st.write("✅ Tudo certo! Chave validada.")
            else:
                st.write("❌ Erro! Chave não localizada.")
        else:
            st.write("❌ Erro! Chave não localizada.")

    st.markdown('[Gere sua chave aqui!](https://aistudio.google.com/app/apikey)')

      
    st.button('Resumir (clique uma vez e espere)', type="primary")
  
    with st.sidebar:
        st.markdown("""
        ### Bem-vindo ao **Resume AI**! ✅

        🤖 O **Resume AI** é uma ferramenta inovadora para resumir conteúdos de forma simples e eficaz.  Esta plataforma utiliza a IA do Google Generative 
        para extrair insights valiosos de textos e documentos em PDF.  Os usuários podem enviar os arquivos e obter resumos instantâneos, facilitando 
        o acesso rápido a informações importantes.

        #### Recursos:

        - 📦 **Upload Simples** Os usuários podem enviar arquivos (PDFs) e gerarem resumos instataneamente. 
        - 💡 **Resumos Instantâneos:** A IA do Google Generative permite gerar resumos precisos e rápidos do conteúdo fornecido.
        - 😃 **Visualização Amigável**: Explore seus resumos de forma organizada e fácil de entender.
        - 📲 **Acesso em Qualquer Lugar**: Use o **Resume AI** aplicação em qualquer dispositivo com acesso à internet.

        Junte-se ao **Resume AI** e libere o poder da inteligência artifical para acessar conhecimentos valiosos de forma instantânea. A revolução da informação começa aqui! 🌐🤿

        ##### Feito por: Matheus Audibert 👨‍💻
        ##### LinkedIn: [linkedin.com/in/matheusaudibert/](linkedin.com/in/matheusaudibert/) 
        ##### Github: [github.com/matheusaudibert](github.com/matheusaudibert)
        """)

if __name__ == "__main__":
    main()
