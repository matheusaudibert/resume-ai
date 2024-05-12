#Matheus Audibert
#Resume_AI

import streamlit as st #Importa a biblioteca do STREAMLIT
import google.generativeai as genai #Importa a biblioteca da GOOGLE.GENERATIVEAI
import PyPDF2 #Importa a biblioteca do PYPDF2
import time #Importa a biblioteca TIME
import settings #Importa o aqruivo settings.py

@st.cache_data

#função que gera o resumo do texto.
def resume_texto (texto:str):
   
  #parâmetros do IA do Google
  generation_config = {
  "temperature": 0.2,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 100000,
  }

  #instrução principal para a ia
  system_instruction = ["""
                        Você é uma ferramenta de resumos de textos palavras ou termos. Determine do que se trata o texto, a palavra ou o termo e resuma-o.\n\n
                        Sintetize as informações em um resumo bem formatado e fácil de ler, estruturado como um ensaio que as resuma de forma coesa.\n\n
                        Não simplesmente repita o texto fornecido. Não copie a estrutura do texto fornecido.\n\n
                        Evite repetições. Conecte todas as ideias entre si.\n\n
                        O texto deve ser dividido em parágrafos. Os parágrafos devem ser indentados.\n\n
                        Antes do resumo, escreva uma lista curta e em formato de tópicos dos principais pontos a serem lembrados.\n\n
                        Faça um título desta maneira: Resumo (conteúdo)"""]
  
  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                system_instruction=system_instruction,
                                safety_settings=settings.safety_settings)
    
  #início da conversa com a ia
  convo = model.start_chat(history=[
                    {
                    #treinameto da ia com few-shots prompting
                    "role": "user",
                    "parts": ["""
                              O surgimento e evolução da inteligência artificial (IA) ao longo das décadas representam uma das mais fascinantes e impactantes jornadas na história da ciência e da tecnologia. Desde suas origens teóricas até os avanços práticos dos dias atuais, a IA transformou-se em uma força poderosa que molda diversos aspectos da nossa sociedade.\n\n
                              Raízes da Inteligência Artificial:\n
                              Os primeiros conceitos relacionados à IA surgiram no século XX, quando pioneiros como Alan Turing e John McCarthy começaram a explorar a possibilidade de máquinas realizarem tarefas que requerem inteligência humana. Em 1950, Turing propôs o famoso "Teste de Turing", uma abordagem para avaliar a capacidade de uma máquina em exibir comportamento inteligente indistinguível do de um humano.\n\n
                              Décadas de Pesquisa Teórica:\n
                              Durante as décadas de 1950 e 1960, houve um crescimento no interesse pela IA, com pesquisadores explorando técnicas como redes neurais artificiais e programação lógica. Surgiram também os primeiros sistemas de IA específicos, como o "Logic Theorist" de Allen Newell e Herbert Simon, capaz de provar teoremas matemáticos.\n\n
                              Era da Inteligência Simbólica e Limitações:\n
                              Nos anos 1970 e 1980, a IA passou por uma fase conhecida como "era da inteligência simbólica", em que predominavam abordagens baseadas em regras e representação do conhecimento. No entanto, esses sistemas enfrentaram limitações em lidar com a complexidade e imprecisão do mundo real.\n\n
                              Revolução do Aprendizado de Máquina:\n
                              A virada veio nos anos 1980 e 1990 com o ressurgimento do interesse em algoritmos de aprendizado de máquina, como redes neurais artificiais e algoritmos genéticos. Avanços na capacidade computacional e na disponibilidade de dados permitiram o desenvolvimento de sistemas capazes de aprender padrões complexos a partir de grandes conjuntos de dados.n\n
                              Boom da Inteligência Artificial:\n
                              No início do século XXI, testemunhamos um verdadeiro boom na IA. O deep learning, uma forma de aprendizado de máquina baseada em redes neurais profundas, revolucionou o campo, permitindo avanços notáveis em reconhecimento de voz, visão computacional, tradução automática e muito mais. Empresas como Google, Facebook, Amazon e Microsoft investiram pesadamente em IA para melhorar seus produtos e serviços.\n\n
                              IA na Vida Cotidiana:\n
                              Atualmente, a IA está presente em muitos aspectos de nossas vidas, desde assistentes virtuais em nossos smartphones até algoritmos que impulsionam recomendações de filmes e músicas. Carros autônomos estão sendo desenvolvidos com base em tecnologias de IA avançadas. Setores como saúde, finanças e manufatura estão adotando sistemas de IA para automatizar tarefas e tomar decisões mais precisas.\n\n
                              Desafios e Futuro da IA:\n
                              Apesar de todos os avanços, a IA enfrenta desafios significativos, como viés algorítmico, questões éticas relacionadas à privacidade e ao uso de dados, além de preocupações sobre o impacto no mercado de trabalho. O futuro da IA provavelmente incluirá avanços em direção à IA geral (AGI), que seria capaz de realizar qualquer tarefa cognitiva que um humano possa fazer.\n\n
                              Em resumo, o surgimento da IA é uma história de criatividade humana, experimentação científica e avanços tecnológicos contínuos. À medida que continuamos a explorar os limites da inteligência artificial, é fundamental considerar não apenas o potencial transformador, mas também as implicações éticas e sociais, garantindo que a IA seja desenvolvida e aplicada de maneira ética e responsável para o benefício de toda a humanidade.
                              """]
                    },
                    
                    #resposta que a ia deveria gerar para o propmt de treinanmento
                    {
                    "role": "model",
                    "parts": ["""
                              Principais Pontos:\n\n
                              A inteligência artificial (IA) tem uma história rica desde o século XX até os dias atuais.\n
                              Alan Turing e John McCarthy foram figuras-chave no desenvolvimento inicial da IA.\n
                              Surgiram primeiros avanços teóricos e sistemas práticos na década de 1950.\n
                              A "era da inteligência simbólica" trouxe sistemas baseados em regras, mas com limitações.\n
                              O ressurgimento da IA nas décadas de 1980 e 1990 foi impulsionado pelo aprendizado de máquina.\n
                              O boom da IA no início do século XXI foi marcado pelo deep learning e pela disponibilidade de grandes conjuntos de dados.\n\n
                              A IA está presente em muitos aspectos da vida cotidiana, como assistentes virtuais e carros autônomos.\n\n
                              Desafios atuais incluem viés algorítmico, ética e impacto no mercado de trabalho.\n
                              O futuro da IA pode envolver o desenvolvimento de IA geral (AGI).\n\n
                              Resumo: A Jornada da Inteligência Artificial\n\n
                              A história da inteligência artificial (IA) é uma narrativa de descobertas científicas e avanços tecnológicos que remontam ao século XX e se estendem até os dias de hoje. O surgimento inicial da IA foi impulsionado por mentes visionárias como Alan Turing e John McCarthy, que exploraram a ideia de máquinas capazes de demonstrar inteligência comparável à humana.\n\n
                              Na década de 1950, surgiram os primeiros avanços teóricos e práticos em IA, com destaque para o desenvolvimento do "Teste de Turing" por Turing e o conceito de programas de computador capazes de aprender, proposto por McCarthy. No entanto, a IA enfrentou desafios durante a "era da inteligência simbólica", quando sistemas baseados em regras mostraram limitações em lidar com a complexidade do mundo real.\n\n
                              O ressurgimento da IA ocorreu nas décadas de 1980 e 1990, impulsionado pelo desenvolvimento de técnicas de aprendizado de máquina, como redes neurais artificiais e algoritmos genéticos. Esse período viu a capacidade dos sistemas de IA de aprender a partir de grandes conjuntos de dados, marcando o início do que viria a ser conhecido como o boom da IA no século XXI.\n\n
                              No início do século XXI, o avanço do deep learning e a disponibilidade de dados em escala massiva aceleraram ainda mais o desenvolvimento da IA. Atualmente, a IA está integrada em diversas facetas da vida cotidiana, desde assistentes virtuais em smartphones até sistemas de carros autônomos.\n\n
                              Apesar dos avanços impressionantes, a IA enfrenta desafios éticos e sociais significativos, incluindo questões de viés algorítmico e o impacto no mercado de trabalho devido à automação. O futuro da IA pode incluir o desenvolvimento de IA geral (AGI), uma forma de inteligência artificial capaz de realizar qualquer tarefa cognitiva humana, apresentando novos desafios e considerações sobre o papel da tecnologia na sociedade moderna.
                              """]
                    },
                    
                    #treinameto da ia com few-shots prompting
                    {
                    "role": "user",
                    "parts": ["""Escola Alura"""]
                    },
                    
                    #resposta que a ia deveria gerar para o propmt de treinanmento
                    {
                    "role": "model",
                    "parts": ["""
                              Resumo: Escola Alura\n\n
                              A Alura é uma plataforma brasileira de ensino online que oferece cursos nas áreas de tecnologia, negócios e criatividade. Fundada em 2011, a Alura é reconhecida por sua ampla variedade de cursos práticos e atualizados, ministrados por instrutores especializados e experientes no mercado.\n\n
                              Os cursos da Alura abrangem uma gama diversificada de tópicos, desde programação e desenvolvimento web até marketing digital, design e gestão de projetos. A plataforma oferece uma abordagem flexível de aprendizado, permitindo que os alunos estudem no seu próprio ritmo e de acordo com suas necessidades individuais.\n\n
                              Um dos destaques da Alura é o foco na aplicação prática do conhecimento. Os cursos são estruturados para proporcionar aos alunos habilidades práticas que podem ser imediatamente aplicadas no mercado de trabalho. Isso é complementado por projetos práticos e exercícios que permitem aos alunos consolidar o que aprenderam.\n\n
                              Além disso, a Alura mantém seus cursos atualizados para refletir as tendências e tecnologias emergentes em cada área de estudo. Isso garante que os alunos tenham acesso ao conhecimento mais recente e relevante, preparando-os para os desafios do mercado atual.\n\n
                              A plataforma da Alura também oferece recursos adicionais, como trilhas de aprendizado personalizadas, certificados de conclusão de curso e uma comunidade ativa de estudantes e profissionais. Esses recursos complementam a experiência de aprendizado, promovendo o desenvolvimento contínuo e a colaboração entre os membros da comunidade.\n\n
                              Em resumo, a Alura é uma escola online abrangente e inovadora, que se destaca pela qualidade de seus cursos, enfoque prático e compromisso em manter seus conteúdos atualizados. É uma opção popular para aqueles que buscam desenvolver habilidades em tecnologia, negócios e criatividade de forma flexível e acessível.
                              """]
                    },

                    #treinameto da ia com few-shots prompting
                    {
                    "role": "user",
                    "parts": ["""Python"""]
                    },
                    
                    #resposta que a ia deveria gerar para o propmt de treinanmento
                    {
                    "role": "model",
                    "parts": ["""
                              Resumo: Python\n\n
                              Python é uma linguagem de programação de alto nível, amplamente utilizada e conhecida por sua simplicidade e legibilidade. Criada por Guido van Rossum e lançada em 1991, Python foi projetada para ser fácil de aprender e utilizar, com uma sintaxe clara e intuitiva que favorece a escrita de código conciso e eficiente.\n\n
                              Uma das características distintivas do Python é sua abordagem orientada a objetos, que permite aos desenvolvedores organizar e reutilizar código de maneira eficaz. Além disso, Python suporta múltiplos paradigmas de programação, incluindo programação imperativa, funcional e procedural, oferecendo flexibilidade aos programadores.\n\n
                              Python é uma escolha popular para uma variedade de aplicações, desde desenvolvimento web e análise de dados até automação de tarefas e inteligência artificial. A vasta gama de bibliotecas e frameworks disponíveis para Python, como Django para web e TensorFlow para machine learning, contribui para sua versatilidade e adoção generalizada.\n\n
                              A comunidade Python é outro aspecto essencial do sucesso da linguagem. Com uma base de usuários ativa e engajada, Python beneficia-se de contribuições constantes para melhorias e desenvolvimento de novas funcionalidades. A documentação abrangente e os recursos de aprendizado, como tutoriais e cursos online, tornam Python acessível mesmo para iniciantes.\n\n
                              Em resumo, Python é uma linguagem de programação poderosa e flexível, valorizada por sua simplicidade, legibilidade e ampla aplicabilidade em diversos domínios. Seja para iniciantes em programação ou para profissionais experientes, Python continua a ser uma escolha popular devido à sua eficiência e comunidade vibrante.
                              """]
                    },

                    #treinameto da ia com few-shots prompting
                    {
                    "role": "user",
                    "parts": ["""Revolução Francesa"""]
                    },
                    
                    #resposta que a ia deveria gerar para o propmt de treinanmento
                    {
                    "role": "model",
                    "parts": ["""
                              Resumo: Revolução Francesa\n\n
                              A Revolução Francesa foi um evento crucial na história moderna que ocorreu entre 1789 e 1799 na França. Foi um período de intensa agitação política, social e econômica que resultou na queda da monarquia absoluta e na ascensão da República Francesa.\n\n
                              A Revolução foi desencadeada por uma combinação de fatores, incluindo a crise financeira do Estado francês, a insatisfação generalizada com o regime monárquico e a influência de ideias iluministas que promoviam a igualdade, liberdade e fraternidade. A convocação dos Estados Gerais em 1789 marcou o início oficial da Revolução.\n\n
                              Os eventos significativos da Revolução incluíram a Tomada da Bastilha em 14 de julho de 1789, que simbolizou o início da luta contra o Antigo Regime, e a Declaração dos Direitos do Homem e do Cidadão, proclamada em agosto de 1789, que afirmava os princípios fundamentais da Revolução.\n\n
                              Durante o período conhecido como Terror (1793-1794), liderado pelo Comitê de Salvação Pública e Robespierre, houve um período de repressão política e execuções em massa. No entanto, a fase mais radical da Revolução deu lugar ao Diretório em 1795, um governo mais moderado.\n\n
                              A Revolução Francesa teve impactos duradouros não apenas na França, mas em toda a Europa e além. Ela inspirou movimentos políticos e sociais em todo o mundo, promovendo ideais de democracia, direitos individuais e igualdade. Além disso, os eventos da Revolução levaram ao surgimento do nacionalismo e influenciaram os desenvolvimentos políticos do século XIX.\n\n
                              Em resumo, a Revolução Francesa foi um período transformador que moldou a história moderna, marcando o fim do Antigo Regime na França e o surgimento de princípios revolucionários que ecoaram ao redor do mundo. Seus legados continuam a ressoar nos sistemas políticos e sociais contemporâneos.
                              """]
                    },

                    {
                    "role": "user",
                    "parts": ["""Seu jorge"""]
                    },
                    
                    #resposta que a ia deveria gerar para o propmt de treinanmento
                    {
                    "role": "model",
                    "parts": ["""
                              Resumo: Seu Jorge\n\n
                              Seu Jorge é um renomado cantor, compositor e ator brasileiro, nascido em 1970 no Rio de Janeiro. Ele se tornou conhecido por sua música única que combina elementos de samba, MPB (Música Popular Brasileira), funk e rock.\n\n
                              Inicialmente, Seu Jorge ganhou destaque como integrante do grupo Farofa Carioca nos anos 1990. No entanto, sua carreira solo decolou com o lançamento do álbum "Samba Esporte Fino" em 2001, que apresenta uma fusão de samba tradicional com influências modernas.\n\n
                              Uma das características distintivas de Seu Jorge é sua voz profunda e emotiva, que transmite uma rica expressão emocional em suas interpretações. Ele é conhecido por suas letras poéticas que abordam temas sociais, amor, identidade e vida nas comunidades brasileiras.\n\n
                              Além de sua carreira musical, Seu Jorge também teve sucesso como ator, aparecendo em filmes aclamados como "Cidade de Deus" (2002), dirigido por Fernando Meirelles, e "A Vida Marinha com Steve Zissou" (2004), dirigido por Wes Anderson.\n\n
                              Entre os álbuns mais notáveis de Seu Jorge estão "Cru" (2005), "América Brasil" (2007) e "Músicas para Churrasco, Vol. 1" (2011). Ele continuou a explorar novos estilos e colaborações ao longo de sua carreira, mantendo uma base de fãs fiel e ganhando reconhecimento internacional.\n\n
                              Em resumo, Seu Jorge é uma figura icônica da música brasileira, conhecido por sua voz distintiva e estilo eclético que combina tradição e inovação. Sua influência na música e no cinema brasileiros continua a ser celebrada, solidificando seu lugar como um dos artistas mais talentosos e versáteis do Brasil.
                              """]
                    }
                    ]           
                          )
    
  #construção do prompt para o usuário, contatenando o texto
  convo.send_message(f"""Faça um resumo, seguindos ox exemplos, sobre: \n\n{texto}.""")

  #resposta da IA para o prompt do usuário
  resposta_texto = convo.last.text

  #retorna a respota para a main
  return resposta_texto


#função que gera o resumo do PDF.
def resume_pdf (conteudo:str):

  #parâmetros do IA do Google
  generation_config = {
  "temperature": 0.2,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 100000,
  }
   
  #instrução principal para a ia
  system_instruction = ["""
                        Você é uma ferramenta de documentos PDFs. O texto que você receberá contém formatações incompletas. Sua função formatar o texto e resumi-lo.\n\n
                        Sintetize as informações em um resumo bem formatado e fácil de ler, estruturado como um ensaio que as resuma de forma coesa.\n\n
                        Não simplesmente repita o texto fornecido. Não copie a estrutura do texto fornecido.\n\n
                        Evite repetições. Conecte todas as ideias entre si.\n\n
                        O texto deve ser dividido em parágrafos. Os parágrafos devem ser indentados.\n\n
                        Antes do resumo você deve escreva uma lista curta e em formato de tópicos dos principais pontos a serem lembrados.\n\n
                        Faça um título para o resumo desta maneira: Resumo (conteúdo)
                        """]
  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                system_instruction=system_instruction,
                                safety_settings=settings.safety_settings)
   
  #início da conversa com a ia
  convo = model.start_chat(history=[
                    {
                    #treinameto da ia com few-shots prompting
                    "role": "user",
                    "parts": ["""
                              O surgimento e evolução da inteligência artificial (IA) ao longo das décadas representam uma das mais fascinantes e impactantes jornadas na história da ciência e da tecnologia. Desde suas origens teóricas até os avanços práticos dos dias atuais, a IA transformou-se em uma força poderosa que molda diversos aspectos da nossa sociedade.\n\n
                              Raízes da Inteligência Artificial:\n
                              Os primeiros conceitos relacionados à IA surgiram no século XX, quando pioneiros como Alan Turing e John McCarthy começaram a explorar a possibilidade de máquinas realizarem tarefas que requerem inteligência humana. Em 1950, Turing propôs o famoso "Teste de Turing", uma abordagem para avaliar a capacidade de uma máquina em exibir comportamento inteligente indistinguível do de um humano.\n\n
                              Décadas de Pesquisa Teórica:\n
                              Durante as décadas de 1950 e 1960, houve um crescimento no interesse pela IA, com pesquisadores explorando técnicas como redes neurais artificiais e programação lógica. Surgiram também os primeiros sistemas de IA específicos, como o "Logic Theorist" de Allen Newell e Herbert Simon, capaz de provar teoremas matemáticos.\n\n
                              Era da Inteligência Simbólica e Limitações:\n
                              Nos anos 1970 e 1980, a IA passou por uma fase conhecida como "era da inteligência simbólica", em que predominavam abordagens baseadas em regras e representação do conhecimento. No entanto, esses sistemas enfrentaram limitações em lidar com a complexidade e imprecisão do mundo real.\n\n
                              Revolução do Aprendizado de Máquina:\n
                              A virada veio nos anos 1980 e 1990 com o ressurgimento do interesse em algoritmos de aprendizado de máquina, como redes neurais artificiais e algoritmos genéticos. Avanços na capacidade computacional e na disponibilidade de dados permitiram o desenvolvimento de sistemas capazes de aprender padrões complexos a partir de grandes conjuntos de dados.n\n
                              Boom da Inteligência Artificial:\n
                              No início do século XXI, testemunhamos um verdadeiro boom na IA. O deep learning, uma forma de aprendizado de máquina baseada em redes neurais profundas, revolucionou o campo, permitindo avanços notáveis em reconhecimento de voz, visão computacional, tradução automática e muito mais. Empresas como Google, Facebook, Amazon e Microsoft investiram pesadamente em IA para melhorar seus produtos e serviços.\n\n
                              IA na Vida Cotidiana:\n
                              Atualmente, a IA está presente em muitos aspectos de nossas vidas, desde assistentes virtuais em nossos smartphones até algoritmos que impulsionam recomendações de filmes e músicas. Carros autônomos estão sendo desenvolvidos com base em tecnologias de IA avançadas. Setores como saúde, finanças e manufatura estão adotando sistemas de IA para automatizar tarefas e tomar decisões mais precisas.\n\n
                              Desafios e Futuro da IA:\n
                              Apesar de todos os avanços, a IA enfrenta desafios significativos, como viés algorítmico, questões éticas relacionadas à privacidade e ao uso de dados, além de preocupações sobre o impacto no mercado de trabalho. O futuro da IA provavelmente incluirá avanços em direção à IA geral (AGI), que seria capaz de realizar qualquer tarefa cognitiva que um humano possa fazer.\n\n
                              Em resumo, o surgimento da IA é uma história de criatividade humana, experimentação científica e avanços tecnológicos contínuos. À medida que continuamos a explorar os limites da inteligência artificial, é fundamental considerar não apenas o potencial transformador, mas também as implicações éticas e sociais, garantindo que a IA seja desenvolvida e aplicada de maneira ética e responsável para o benefício de toda a humanidade.
                              """]
                    },
                    
                    #resposta que a ia deveria gerar para o propmt de treinanmento
                    {
                    "role": "model",
                    "parts": ["""
                              Principais Pontos:\n\n
                              A inteligência artificial (IA) tem uma história rica desde o século XX até os dias atuais.\n
                              Alan Turing e John McCarthy foram figuras-chave no desenvolvimento inicial da IA.\n
                              Surgiram primeiros avanços teóricos e sistemas práticos na década de 1950.\n
                              A "era da inteligência simbólica" trouxe sistemas baseados em regras, mas com limitações.\n
                              O ressurgimento da IA nas décadas de 1980 e 1990 foi impulsionado pelo aprendizado de máquina.\n
                              O boom da IA no início do século XXI foi marcado pelo deep learning e pela disponibilidade de grandes conjuntos de dados.\n\n
                              A IA está presente em muitos aspectos da vida cotidiana, como assistentes virtuais e carros autônomos.\n\n
                              Desafios atuais incluem viés algorítmico, ética e impacto no mercado de trabalho.\n
                              O futuro da IA pode envolver o desenvolvimento de IA geral (AGI).\n\n
                              Resumo: A Jornada da Inteligência Artificial\n\n
                              A história da inteligência artificial (IA) é uma narrativa de descobertas científicas e avanços tecnológicos que remontam ao século XX e se estendem até os dias de hoje. O surgimento inicial da IA foi impulsionado por mentes visionárias como Alan Turing e John McCarthy, que exploraram a ideia de máquinas capazes de demonstrar inteligência comparável à humana.\n\n
                              Na década de 1950, surgiram os primeiros avanços teóricos e práticos em IA, com destaque para o desenvolvimento do "Teste de Turing" por Turing e o conceito de programas de computador capazes de aprender, proposto por McCarthy. No entanto, a IA enfrentou desafios durante a "era da inteligência simbólica", quando sistemas baseados em regras mostraram limitações em lidar com a complexidade do mundo real.\n\n
                              O ressurgimento da IA ocorreu nas décadas de 1980 e 1990, impulsionado pelo desenvolvimento de técnicas de aprendizado de máquina, como redes neurais artificiais e algoritmos genéticos. Esse período viu a capacidade dos sistemas de IA de aprender a partir de grandes conjuntos de dados, marcando o início do que viria a ser conhecido como o boom da IA no século XXI.\n\n
                              No início do século XXI, o avanço do deep learning e a disponibilidade de dados em escala massiva aceleraram ainda mais o desenvolvimento da IA. Atualmente, a IA está integrada em diversas facetas da vida cotidiana, desde assistentes virtuais em smartphones até sistemas de carros autônomos.\n\n
                              Apesar dos avanços impressionantes, a IA enfrenta desafios éticos e sociais significativos, incluindo questões de viés algorítmico e o impacto no mercado de trabalho devido à automação. O futuro da IA pode incluir o desenvolvimento de IA geral (AGI), uma forma de inteligência artificial capaz de realizar qualquer tarefa cognitiva humana, apresentando novos desafios e considerações sobre o papel da tecnologia na sociedade moderna.
                              """]
                    },
                    
                    #treinameto da ia com few-shots prompting
                    {
                    "role": "user",
                    "parts": ["""
MANUAL DO ALUNO FIAP
MENSAGEM À COMUNIDADE FIAP
Queridos alunos, pais e responsáveis.
Esperamos que vocês e suas famílias estejam bem. Estamos começando
nosso ano letivo. Um ano de muita esperança para todos nós. E aproveitamos para
agradecer novamente a parceria e união de vocês.
Todos nós nos reinventamos durante esse período de pandemia: enfrentamos
desafios, vivemos novas experiências, mudamos nossa forma de trabalhar. Tudo
isso foi fundamental para mantermos nossas atividades e reafirmarmos nosso
compromisso com todos os nossos alunos, professores e colaboradores.
Seguindo as recomendações das autoridades de saúde, tomamos medidas
para mitigar o impacto do vírus Covid-19 desde a chegada da pandemia do novo
coronavírus ao Brasil. As dinâmicas sofreram mudanças, incluindo os processos da
nossa escola, trazendo desafios e novas formas de interação.
O ano de 2021 começou com avanço dos casos de Covid-19, o que resultou
em mais uma atualização do Plano São Paulo. A nossa preocupação com a
Comunidade FIAP é constante e, por isso, seguimos com os esforços para mitigar a
contaminação pelo novo coronavírus e atentamos às orientações direcionadas à
Educação. Neste sentido, destacamos pontos importantes enquanto perdurar a
pandemia:
1. Novo horário de funcionamento das unidades: o atendimento presencial
está sujeito as fases e restrições estabelecidas pelo Governo de Estado e do
Município de São Paulo, quando permitido os prédios passam a funcionar de
segunda a sexta-feira, das 8h às 20h. Aos sábados, nosso campus estará fechado;
2. Atendimento Remoto: realizado on-line pelo WhatsApp: (11) 98170-0028
e/ou pelo e-mail: helpcenter@fiap.com.br;
3
3. Aulas 100% remotas: enquanto a cidade de São Paulo estiver nas Fases
Laranja ou Vermelha, nenhuma aula ou atividade poderá ser realizada
presencialmente. Assim, manteremos o modelo remoto até que haja reclassificação
da capital pelo Governo de São Paulo ou outra orientação que nos autorize retomar
o formato híbrido;
4. Rodízio dos times administrativos: seguimos com o funcionamento de
toda a estrutura administrativa da escola, fundamental para a realização de nossos
cursos. Os gestores podem avaliar a melhor forma para gerenciar a escala de suas
equipes com o objetivo de garantir a excelência dos nossos serviços;
5. Mantenha o distanciamento social. Atente à distância de 1,5 metro
durante todas as interações (sala de aula, banheiros e vestiários, área de café,
refeitórios e cantina);
6. Use máscara. Em nossas unidades, o uso é obrigatório durante toda a
permanência nos prédios, inclusive nas salas de aula;
7. Lave as mãos com frequência;
8. Use álcool gel 70% para higiene das mãos nas entradas dos prédios,
áreas de circulação e alimentação, salas de aula, banheiros e elevadores;
9. Todos os casos que ocorram dentro da escola serão devidamente
comunicados aos que tiveram contato direto com a pessoa, conforme determinam os
protocolos de saúde, sempre garantindo a confidencialidade médica do paciente.
Acompanhe as recomendações na íntegra para alunos, professores e
colaboradores. Cada detalhe visa garantir a saúde e o cuidado com todos.
Lembramos também que nossa Central de Monitoramento de Saúde está
preparado para te apoiar. Caso você apresente sintomas sugestivos de Covid-19 ou
tiver dúvidas, envie uma mensagem para (11) 94502-8361.
4
A sua atenção às recomendações é fundamental. Cuide-se!
Este Manual do Aluno foi elaborado especialmente para a Comunidade FIAP
– alunos, professores e colaboradores – com o objetivo de orientar sobre a nossa
organização, estrutura e serviços, visando proporcionar a todos um melhor
entrosamento com a vida acadêmico-administrativa da nossa instituição.
Esperamos que encontrem aqui as respostas para todas as dúvidas que
possam surgir no decorrer do ano. Recomendamos que consultem a área do aluno
onde está publicada a versão atualizada deste material.
Agradecemos por escolher o FIAP - Centro Universitário e pela confiança
depositada em nosso trabalho. Estejam certos de nossa dedicação e entusiasmo
para fazer do FIAP – Centro Universitário cada vez mais a melhor escola de
tecnologia!
Desejamos a todos um grande crescimento profissional e pessoal e um
significativo ganho de conhecimentos ao longo deste ano letivo.
Sejam muito bem-vindos!

Wagner Sanchez John Paul Lima
Diretor Acadêmico Diretor de Educação a Distância
5
A FIAP – Centro Universitário foi idealizado, planejado e construído dentro de
um projeto pedagógico e estrutural para ser a melhor escola de tecnologia do país.
Para alcançar à excelência em cursos superiores de tecnologia, a FIAP investe
em laboratórios de alta tecnologia, plataformas de ensino diferenciadas, qualificação
do corpo docente, parcerias estratégicas com grandes empresas e, principalmente,
integração com o mercado de trabalho.
Para acompanhar a velocidade das mudanças e principais tendências mundiais
da tecnologia e gestão, a FIAP estrutura seus conteúdos programáticos de maneira
flexível e com grande capacidade de adaptação, garantindo os melhores e mais
atualizados cursos de graduação, pós-graduação e cursos de curta duração (SHIFT),
presencialmente e à distância.
Assim, a FIAP – Centro Universitário combina toda a experiência de
profissionais competentes e a infraestrutura de alta qualidade com a criatividade e a
ousadia de mudar, de se adaptar às novas tendências, tecnologias e exigências do
mercado.
Os resultados são expressivos: o Ministério da Educação, os veículos de
comunicação e, acima de tudo, o sucesso profissional dos alunos confirmam a FIAP
como a melhor faculdade de tecnologia, inovação e empreendedorismo do país.
Com certeza esse sucesso também será alcançado por você!
6
1 EQUIPE....................................................................................................................7
2 INFRAESTRUTURA ................................................................................................9
2.1 Centro Tecnológico ...................................................................................................................................................9
2.2 Biblioteca .................................................................................................................................................................10
2.3 Plataforma Fiap On..................................................................................................................................................11
2.4 Fiap On App .............................................................................................................................................................12
2.5 Talent Lab ................................................................................................................................................................13
2.6 Help Center..............................................................................................................................................................14
2.7 Solicitação De Documentos....................................................................................................................................14
2.8 Modelo Acadêmico Do Fiap On..............................................................................................................................17
3 AVALIAÇÃO DO DESEMPENHO ESCOLAR .......................................................18
3.1 Critérios Para Avaliação E Aprovação.....................................................................................................................18
3.2 Encontro Presencial/Digital ....................................................................................................................................19
3.3 Avaliação À Distância (Ad).......................................................................................................................................19
3.4 Valor Das Avaliações À Distância ............................................................................................................................20
3.5 Datas De Aplicação Das Avaliações À Distância .....................................................................................................20
3.6 Reclamações De Erros Em Notas De Avaliação À Distância ..................................................................................20
3.7 Avaliações Presenciais Obrigatórias (Apo).............................................................................................................20
3.8 Provas Substitutivas ................................................................................................................................................21
3.9 Prova De Exame (Pe) ...............................................................................................................................................21
4 INFORMAÇÕES ACADÊMICAS ...........................................................................22
4.1 Informações Gerais .................................................................................................................................................22
4.2 Matrícula..................................................................................................................................................................22
4.3 Trancamento De Matrícula.....................................................................................................................................23
4.4 Transferências .........................................................................................................................................................23
4.5 Alunos Com Dependência.......................................................................................................................................24
4.6 Alunos Retidos.........................................................................................................................................................25
4.7 Aulas De Dependência E Adaptação ......................................................................................................................26
4.8 Entrega De Atestado Médico..................................................................................................................................26
4.9 Revisão De Notas.....................................................................................................................................................27
4.10 Alunas Gestantes...................................................................................................................................................27
4.11 Colação De Grau....................................................................................................................................................27
5 ESTÁGIO ...............................................................................................................28
5.1 Estágio Profissionalizante .......................................................................................................................................28
6 BOLSAS DE ESTUDO...........................................................................................28
6.1 Bolsas De Mérito Acadêmico..................................................................................................................................28
6.2 Fiap Plus...................................................................................................................................................................29
7
1 EQUIPE
DIRETOR ACADÊMICO Wagner Marcelo Sanchez
wagner@fiap.com.br
DIRETOR DE EDUCAÇÃO A DISTÂNCIA
(FIAP ON)
John Paul Lima
john.lima@fiap.com.br
Coordenadores do Curso de Gestão da
Tecnologia da Informação (FIAP ON)
Débora Richter
debora.richter@fiap.com.br
Coordenador do Curso de Jogos Digitais
(FIAP ON)
Agesandro Scarpioni
agesandro@fiap.com.br
Coordenador do Curso de Defesa Cibernética
(FIAP ON)
Alessandro Vinicius de S. Vieira
profalessandro.vieira@fiap.com.br
Henrique Ruiz Poyatos Neto
henrique.poyatos@fiap.com.br
Coordenadoras do Curso de Marketing Digital
& Data Science (FIAP ON)
Debora Richter Brolio
profdebora.richter@fiap.com.br
Isabelle Curvello
isabelle.curvelo@fiap.com
Coordenadora do Curso de Sistemas de
Informação (FIAP ON)
Patrícia Gallo
profpatricia.gallo@fiap.com.br
Coordenadora do Curso de Produção
Multimídia (FIAP ON)
Giovana Vaz
giovana.vaz@fiap.com.br
Evelyn Cid
profevelyn.cid@fiap.com.br
Coordenador do Curso de Análise e
Desenvolvimento de Sistemas (FIAP ON)
Andre de Freitas David
profandre.david@fiap.com.br
Evelyn Rodrigues Cid
profevelyn.cid@fiap.com.br
Coordenador do Curso Tecnologia em
Sistemas para Internet (FIAP ON)
Humberto Delgado de Sousa
humberto@fiap.com.br
8
Coordenador do Curso de Banco de Dados
(FIAP ON)
Agesandro Scarpioni
agesandro@fiap.com.br
Departamento de Gestão de Carreiras talentlab@fiap.com.br
BIBLIOTECA Fabiana Pavarini Morais
biblio@fiap.com.br
HELP CENTER Rodrigo Júlio Alves de Almeida
helpcenter@fiap.com.br
9
2 INFRAESTRUTURA
2.1 CENTRO TECNOLÓGICO
A FIAP – Centro Universitário possui quatro campi, 48 laboratórios, incluindo
exclusivos laboratórios de redes, de hardware física e eletrônica, de cultura maker,
de games e de automação. Com aproximadamente 2100 computadores
interconectados, são utilizados para as aulas práticas das disciplinas
profissionalizantes de seus cursos, prática profissional, cursos de extensão e
trabalhos de pesquisa científica. Essas dependências são de uso exclusivo dos
professores e alunos e estarão sob sua total responsabilidade e das respectivas
Coordenadorias de Cursos.
O Centro Tecnológico é administrado e utilizado segundo o regulamento
próprio na área do aluno – Regulamento de utilização dos “Laboratórios de
Informática”.
WOW LAB:
Inovação é WOW. Um laboratório planejado pela FIAP – Centro Universitário
para Gameplay e Play Test com parceria da Xbox. O WOW Lab foi criado para
inovar, dar vida aos novos produtos e serviços ou orientar a reformulação de
processos disruptivos.
INNOVATION LAB:
Você ligado ao que há de mais novo no mundo dos games. Desenvolvimento
de jogos, apoio a aulas de modelagem 3D e programação, com todos os
equipamentos necessários.

10
GAMEDEV LAB:
O Gamedev Lab tem 49 workstations, 17 delas de última geração, equipados
com placas de vídeo GTX1060. E uma série de softwares de apoio ao
desenvolvimento de jogos como Maya, Mudbox, Unreal e Unity.
Endereço das Unidades:
• Unidade I: Avenida Lins de Vasconcelos, 1264 - CEP: 01538-001 –
Aclimação – São Paulo.
• Unidade II: Avenida Lins de Vasconcelos, 1222 – CEP: 01538-001 –
Aclimação – São Paulo.
• Unidade Paulista: Avenida Paulista, 1106 – 6º e 7º andar – CEP: 01311-
000 - Cerqueira César – São Paulo.
• Unidade Vila Olímpia: Rua Fidêncio Ramos, 308- 7º andar – Torre A –
CEP: 04551-010 – Vila Olímpia - São Paulo.
2.2 BIBLIOTECA
O acervo virtual e físico é constituído por livros, periódicos e DVDs. Os materiais
estão à disposição para o corpo docente, discente e administrativo do FIAP – Centro
Universitário. O consulente deve fazer sua inscrição na biblioteca com os seguintes
dados:
• Nome completo
• Registro de Matrícula (R.M.)
• RG ou carteira escolar atualizada
11
A Biblioteca é regida por regulamento, procedimentos e normas definidas em
documentos que estão disponíveis para consulta na área do aluno (Portal FIAP):
Regulamento das “Bibliotecas” e Procedimentos e Normas Complementares das
“Bibliotecas”.
2.3 PLATAFORMA FIAP ON
Por meio da Plataforma FIAP ON o aluno tem acesso aos conteúdos no formato
web, em playlist de vídeos, playlist de áudio, pdf, atividades, transmissão ao vivo (live),
fórum de discussão, comunicação via e-mail e chat pelo Slack/ Teams (dependendo
do seu curso), além de visualizar calendário, receber notificações e acessar os
serviços acadêmicos e de secretaria, tais como:
• Guia acadêmico.
• Normas disciplinares.
• Conteúdo programático de cada disciplina.
• Acompanhamento de notas e faltas (boletim).
• Contato com a coordenação.
• Contato com a ouvidoria.
• Serviços de:
▪ Secretaria.
▪ Financeiro (geração de 2ª via de boleto).
▪ Biblioteca Física e Virtual.
• Visualização de avisos no mural de notícias relacionados a todas as possíveis
áreas da FIAP, como Talent Lab, avisos de palestras, de cursos, de parcerias,
comunicados da coordenação e da diretoria, entre outros.
12
• Informações gerais sobre:
▪ Parcerias.
▪ Empresa Júnior.
▪ Transporte Gratuito.
▪ Bicicletário.
Para acesso da Plataforma FIAP ON, basta o aluno ter um computador com
acesso à internet, um navegador de páginas e acessar um ou todos os formatos de
conteúdo:
• Conteúdo escrito e visualmente rico em imagens, infográficos e animações:
esse conteúdo é totalmente responsivo para ser acessado a partir de
qualquer dispositivo móvel. Nele estão disponíveis todas as atividades
obrigatórias e facultativas à distância.
• Playlist de vídeos: abordados em formato documentário, videoaulas, vídeos
animados, programas de entretenimento, entre outros.
• Playlist de áudio: abordado em formato de programas de entrevistas à
podcasts.
• Livro digital em PDF (e-book). Nesse formato, o aluno pode realizar o
download do arquivo.
2.4 FIAP ON APP
O Aplicativo FIAP ON é um app focado em conteúdo, em que o aluno tem
acesso ao material no formato web, playlist de vídeos, playlist de áudio e pdf, com
todas as características que um bom app deve ter:
• Visualização dos conteúdos no modo off-line, em que o app realiza o
download de qualquer um dos formatos e trabalha com códigos de
13
criptografia como proteção ao conteúdo. Dessa forma, o aluno visualiza o
material com segurança, bastando ter espaço de memória do seu
dispositivo.
• Os vídeos são assistidos e sequenciados de forma automática, sem a
necessidade de retornar a um menu de seleção.
• aluno consegue retomar a visualização de um vídeo a partir do ponto que
tiver parado.
• áudio pode ser escutado em segundo plano, ou seja, o aluno pode
realizar outra atividade no aparelho e ouvir o áudio em paralelo.
• A experiência na navegação, visualização, leitura e interação dos
conteúdos web e pdf ocorre de forma simples, sendo igualmente possível
a experiência pelo computador.
• aplicativo foi desenvolvido nativo nas plataformas Apple iOS e Google
Android, permitindo que apps nativos sejam utilizados integrados com o
aplicativo FIAP ON.
• Os apps nativos de Acessibilidade se integram perfeitamente com todas
as funções do aplicativo FIAP ON, permitindo o manuseio por pessoas
com deficiências visuais, auditivas ou outras, a fim de proporcionar
experiências completas para seus estudos.
2.5 TALENT LAB
Reafirmando o compromisso de oferecer um ensino de qualidade, alto padrão
acadêmico, crescimento pessoal e profissional dos alunos e egressos, a FIAP -
Centro Universitário estruturou o Talent Lab, por meio do qual os alunos e egressos
contam com:
• Preparação pessoal e profissional;
• Geração de novas oportunidades de colocação e ascensão profissional;
14
• Acompanhamento sistematizado de suas carreiras.
Acesse o nosso portal (www.fiap.com.br) e desfrute de todos os benefícios
inéditos e exclusivos que o FIAP - Centro Universitário oferece a você.
Preocupados com o bem-estar e qualidade de vida dos alunos, este
departamento tem por objetivo auxiliá-los em seu percurso acadêmico em questões
pessoais e pedagógicas que possam vir a atrapalhar o seu desempenho na IES.
Trancamentos / Cancelamentos de Matrícula.
Horário de funcionamento: 2ª a 6ª feira das 8h às 22h00
Local: Unidade II - Avenida Lins de Vasconcelos, 1222 - CEP: 01538-001 -
Aclimação - São Paulo.
2.6 HELP CENTER
O Help Center tem o objetivo de atender às necessidades dos alunos no que
tange à documentação acadêmica, assuntos financeiros em outras solicitações.
O FIAP – Centro Universitário, com foco em melhoria continua, investe na
capacitação de seus profissionais e recursos necessários para atingir este objetivo.
Atendimento Remoto: on-line pelo WhatsApp: (11) 98170-0028 e/ou pelo email: helpcenter@fiap.com.br;
Atendimento Presencial: de 2ª a 6ª feira das 8h às 21h30.
Endereço: Avenida Lins de Vasconcelos, 1264 – 2º andar. CEP: 01538-001.
2.7 SOLICITAÇÃO DE DOCUMENTOS
DECLARAÇÕES ACADÊMICAS OU FINANCEIRAS
15
Onde solicitar: no portal do aluno, acesso pelo link: http://www2.fiap.com.br
ou pessoalmente no Help Center, on-line pelo WhatsApp: (11) 98170-0028
e/ou pelo e-mail: helpcenter@fiap.com.br;
Onde retirar: documento com assinatura digital e será encaminhado por email.
Taxa: Isento
Prazo: 05 dias.
Histórico Escolar
Onde solicitar: no portal do aluno, acesso pelo link: http://www2.fiap.com.br
ou pessoalmente no Help Center, on-line pelo WhatsApp: (11) 98170-0028
e/ou pelo e-mail: helpcenter@fiap.com.br;
Onde retirar: documento com assinatura digital e será encaminhado por email.
Taxa: Primeira via para concluintes: (isento)
Taxa: Segunda via consultar no ato da solicitação.
Prazo: 20 dias.
Conteúdo Programático
Onde solicitar: no portal do aluno, acesso pelo link: http://www2.fiap.com.br
ou pessoalmente no Help Center, on-line pelo WhatsApp: (11) 98170-0028
e/ou pelo e-mail: helpcenter@fiap.com.br;
Onde retirar: pessoalmente no Help Center mediante apresentação do
documento de identidade original atualizado. Na impossibilidade de
comparecimento, é autorizada a retirada por representante munido de
procuração simples com firma reconhecida.
Taxa: R$ 40,00 por ano solicitado.
16
Prazo: 10 dias.
Certificado de Conclusão de Curso
Onde solicitar: no portal do aluno, acesso pelo link: http://www2.fiap.com.br
ou pessoalmente no Help Center, on-line pelo WhatsApp: (11) 98170-0028
e/ou pelo e-mail: helpcenter@fiap.com.br;
Onde retirar: documento com assinatura digital e será encaminhado por email.
Taxa: Primeira via para concluintes: (isento)
Taxa: Segunda via consultar no ato da solicitação.
Prazo: 10 dias úteis
OBS.: para solicitar o referido documento o aluno deve ter colado grau e não
possuir nenhuma pendência de documentos.
Diploma
Onde solicitar: no portal do aluno, acesso pelo link: http://www2.fiap.com.br
ou pessoalmente no Help Center, on-line pelo WhatsApp: (11) 98170-0028
e/ou pelo e-mail: helpcenter@fiap.com.br;
Onde retirar: pessoalmente no Help Center mediante apresentação do
documento de identidade original atualizado. Na impossibilidade de
comparecimento, é autorizada a retirada por representante munido de
procuração simples com firma reconhecida.
Primeira via para concluintes: (isento).
Prazo: 365 dias
OBS.: para solicitar o referido documento o aluno deve ter colado grau e não
possuir nenhuma pendência de documentos
17
Demais vias
Consultar regras no Help Center
Taxa: R$ 160,00
Prazo: 365 dias
2.8 MODELO ACADÊMICO DO FIAP ON
Os cursos à distância da FIAP foram elaborados em um formato conhecido
como Project Based-Learning (PBL) ou Aprendizado Orientado a Projeto. O aluno
deverá realizar atividades para o desenvolvimento de um projeto, do começo ao fim.
Os cursos são PBLs na concepção mais pura do termo. O conteúdo não está
orientado a disciplinas, e, sim, à entrega do projeto. Tudo o que é aprendido é
aplicado imediatamente. Portanto, o aluno não encontrará as divisões tradicionais
em áreas de conhecimento no conteúdo. As atividades do projeto são mapeadas
considerando as disciplinas, então a avaliação será atribuída a essas disciplinas.
Os projetos são divididos em fases, cada um deles com seu conjunto de
atividades. A fase é disponibilizada de uma só vez e as atividades devem ser
realizadas e entregues conforme calendário acadêmico. Quando a fase termina, os
conteúdos permanecem disponíveis, embora as atividades não possam mais ser
entregues.
18
3 AVALIAÇÃO DO DESEMPENHO ESCOLAR
3.1 CRITÉRIOS PARA AVALIAÇÃO E APROVAÇÃO
As notas anuais são compostas dessa forma:
• 30 pontos para a Avaliação a Distância (AD).
• 70 pontos para as Avaliações Presenciais Obrigatórias (APO).
O cálculo da Nota Final (NF) levará em consideração o somatório de todas as
avaliações de cada disciplina: NF = AD + APO.
Os critérios de aprovação baseiam-se na nota final obtida pelo aluno por
disciplina, conforme tabela abaixo:
MÉDIA FINAL (ANUAL) SITUAÇÃO
0 a 39 Reprovado
40 a 59 Exame
60 a 100 Aprovado
Caso o aluno fique de Exame, a nota necessária para a sua aprovação passa
a ser: Nota para aprovação no Exame = (120 – Nota Final).
19
3.2 ENCONTRO PRESENCIAL/DIGITAL
Nos Encontros Presenciais/Digitais obrigatórios previstos no Calendário, o
aluno vivencia o conhecimento e faz networking, tudo isso baseado no método
Experience Based Learning.
Os encontros misturam conteúdo, experiência, desafios reais e premiações. O
objetivo? Você vai colocar em prática as competências desenvolvidas durante as
disciplinas e aumentará o seu conhecimento por meio de dinâmicas com os
principais desafios de cada área.
A participação nos encontros presenciais/digitais é de caráter obrigatório para
os alunos matriculados, a agenda é previamente divulgada no calendário
acadêmico, sendo vedado o abono de faltas, exceto em casos previstos por lei.
Independentemente dos demais resultados obtidos, é considerado reprovado
na disciplina o aluno que não tiver comparecido em todos os encontros presenciais
obrigatórios.
3.3 AVALIAÇÃO À DISTÂNCIA (AD)
Avaliação à Distância (AD) são avaliações aplicadas por meio da plataforma
on-line aos alunos, permitindo que o professor acompanhe seu progresso ao longo
do ano, tanto no que diz respeito ao conhecimento específico que devem adquirir
quanto à aplicação prática desses conhecimentos.
As ADs podem ser realizadas na forma de testes de múltipla escolha ou
dissertativos, na forma de lista de exercícios teóricos ou práticos, conforme critério
estabelecido pelo professor.
20
3.4 VALOR DAS AVALIAÇÕES À DISTÂNCIA
As Avaliações à Distância valerão 1,0 (um) ou mais pontos, sejam elas
dissertativas ou feitas pelo sistema.
Não haverá reposição de Avaliações à Distância perdidas, exceto em casos
previstos pela lei, ou seja, por motivo de doença com atestado médico referente ao
dia da avaliação. Nesse caso, o aluno deverá entregar o atestado médico no Help
Center em, no máximo, 48 (quarenta e oito) horas após a liberação médica e
comunicar ao professor da disciplina.
3.5 DATAS DE APLICAÇÃO DAS AVALIAÇÕES À
DISTÂNCIA
As ADs estão disponíveis durante todo o conteúdo e são visualizadas no
calendário da plataforma on-line.
3.6 RECLAMAÇÕES DE ERROS EM NOTAS DE
AVALIAÇÃO À DISTÂNCIA
Reclamações referentes às notas das Avaliações à Distância devem ser
solicitadas diretamente ao professor em até 7 (sete) dias corridos após a divulgação
das notas.
3.7 AVALIAÇÕES PRESENCIAIS OBRIGATÓRIAS (APO)
As Avaliações Presenciais Obrigatórias (APO) podem assumir a forma de
uma prova para avaliação do conhecimento específico adquirido pelos alunos nas
diversas disciplinas do ano ou de um projeto a ser desenvolvido sob a orientação
dos professores responsáveis pelo grupo de disciplinas.
21
Reclamações referentes às notas das Avaliações Presenciais Obrigatórias
devem ser solicitadas via secretaria virtual na Plataforma FIAP ON em até 7 (sete)
dias corridos após a divulgação das notas.
Haverá oferta de prova substitutiva, as datas serão disponibilizadas no
calendário acadêmico.
Devido à pandemia de Covid-19, a Atividade Presencial Obrigatória
excepcionalmente será realizada a distância.
3.8 PROVAS SUBSTITUTIVAS
Haverá prova substitutiva para APO. Não existe prova substitutiva para
Exame.
As provas substitutivas deverão ser requisitadas por meio do serviço
disponível no portal da FIAP dentro dos prazos previamente divulgados, mediante
pagamento eletrônico da taxa de R$ 160,00 (cento e sessenta reais) por prova até a
data do vencimento.
O aluno que não fizer o pedido e o pagamento nos prazos previstos não
poderá realizar a prova substitutiva.
No caso de o aluno ter apresentado dentro do prazo o atestado médico válido
e compatível com a data da perda da prova principal, deverá entregá-lo no Help
Center, dentro dos prazos. Para os alunos que cumprirem a entrega do atestado
dentro do prazo, devem solicitar conjuntamente o abono da taxa, no período de
solicitação previsto no calendário acadêmico. Caso o aluno não entregue o atestado
médico dentro do prazo, perderá o direito ao abono e terá de pagar a taxa de R$
160,00 (cento e sessenta reais) por prova.
3.9 PROVA DE EXAME (PE)
As provas de exame são compostas de questões que abrangerão todo o
conteúdo ministrado no período letivo. Não haverá prova de exame substitutiva.
22
Será solicitada uma identificação com foto para o aluno realizar a prova de
exame.
4 INFORMAÇÕES ACADÊMICAS
4.1 INFORMAÇÕES GERAIS
Normas disciplinares: a FIAP possui um conjunto de normas disciplinares. A
cada ocorrência disciplinar cometida pelo aluno será atribuído um número de pontos
em seu prontuário. Os pontos são acumulativos. Ao acumular pontos, o aluno
perderá benefícios, tais como: bolsa de estudo, direito de participar como
representante de turma, direito de participar no PIC ou perda do projeto, direito de se
candidatar à monitoria ou perda da monitoria, direito de participar de eventos
promovidos pela faculdade, direito de usufruir dos serviços prestados pelo
departamento de TalentLab, dentre outras penalidades. Caso o aluno exceda 20
pontos, ele será convidado a se retirar da faculdade.
Avisos da coordenação e direção: diariamente, o aluno deve entrar na
plataforma FIAP ON e ler os avisos que são postados. Informações importantes para
a vida acadêmica do aluno são postadas frequentemente e deve-se estar atento.
4.2 MATRÍCULA
A matrícula do aluno é renovada anualmente, conforme contrato de prestação
de serviços, antes do início de cada período letivo, dentro dos prazos determinados
no Calendário Acadêmico. A não renovação da matrícula implica abandono de curso
e perda do vínculo do aluno com a faculdade, exceto em casos de trancamento
devidamente formalizados no Help Center.
23
RM: Registro de Matrícula é o número que você recebe no ato de sua
matrícula, é a identificação do aluno em todos os procedimentos da FIAP e que o
acompanha até o final do curso.
Carteira do Estudante (Cartão de Acesso): Além de compor a identidade
estudantil do aluno, o cartão incorpora a função de acesso presencial à instituição. O
cartão é pessoal e intransferível.
Para manter a integridade de seu cartão, ele não deve ser: perfurado,
dobrado, submetido a altas temperaturas, limpos por abrasivos, tais como álcool e
removedores.
4.3 TRANCAMENTO DE MATRÍCULA
De acordo com o regimento da faculdade, é concedido o trancamento de
matrícula para interromper temporariamente os estudos uma única vez durante o
curso, mas manter o vínculo do aluno com a faculdade é seu direito à renovação de
matrícula.
O trancamento é concedido aos alunos devidamente matriculados no ano
letivo de solicitação. É concedido um único trancamento durante o período do curso,
para não ocasionar em perda de vínculo, o aluno deverá retornar obrigatoriamente
no início do próximo ano letivo.
Obs.: O aluno arcará com as eventuais consequências de alteração de grade
curricular em seu retorno.
4.4 TRANSFERÊNCIAS
Mudança de turma ou curso: o aluno que desejar mudar de turma ou curso
deverá respeitar os prazos do Calendário Acadêmico e solicitar a transferência por
24
meio da Plataforma ON ou presencialmente no Help Center. As mudanças de turma
somente serão realizadas caso não haja desequilíbrio no número de alunos das
turmas e/ou disponibilidade de vagas, pois mesmo a educação à distância é
pontuada por quantidade de alunos, conforme regulamentação do Ministério da
Educação.
4.5 ALUNOS COM DEPENDÊNCIA
Para prosseguir com o curso, o aluno só poderá ser reprovado em uma ou
duas disciplinas, devendo cursá-las em regime de dependência.
Caso o aluno fique retido em mais de duas disciplinas, que pode também ser
consequência do acúmulo de dependências de períodos anteriores ou de
adaptações não realizadas, ou no caso de aluno no último ano do curso que ficar
retido em uma disciplina, fica obrigado a repetir o período. Neste caso, as disciplinas
devem ser cursadas em regime regular e não de dependência, e o aluno passará à
condição de “aluno retido” e não de “aluno regular”.
Alunos retidos devem cursar novamente o projeto e realizar somente as
atividades relacionadas às disciplinas retidas. As informações das atividades e sua
pontuação ficam no MAPA DE ATIVIDADES. É necessário participar do Encontro
Presencial Obrigatório.
Para os cursos de Bacharelado, o aluno só poderá cursar o último ano do
curso com apenas uma disciplina de Dependência ou Adaptação.
O aluno deverá se matricular nas disciplinas em dependência no período
seguinte da reprovação e, caso não possa ou não queira cursá-las, deverá requerer
o seu adiamento no Help Center dentro dos prazos estabelecidos no calendário
acadêmico.
25
Os critérios de aprovação para alunos de dependência e adaptação são os
mesmos para os alunos regulares.
As disciplinas de dependência podem ser pagas ou não, dependendo da
escolha do aluno.
- Plano gratuito: O aluno tem acesso aos materiais na plataforma, porém sem
a tutoria do professor, devendo realizar as provas semestrais presencialmente.
- Plano pago: Acréscimo de 15% por disciplina na mensalidade, com acesso
aos materiais na plataforma, tutoria e acompanhamento do professor durante o ano,
devendo realizar as provas semestrais presencialmente.
As disciplinas estarão disponíveis na plataforma, aparecendo separadas e
devidamente identificadas. A avaliação das disciplinas de DP é feita por meio de
uma prova por semestre, presencialmente.
4.6 ALUNOS RETIDOS
O aluno que ficar retido em uma ou mais disciplinas, ou acumular três ou mais
dependências de diferentes anos, deverá cursá-las no período seguinte, conforme
regras estabelecidas em “Alunos com dependência”.
Alunos retidos devem cursar novamente o projeto, devendo realizar somente
as atividades relacionadas às disciplinas retidas. As informações das atividades e
sua pontuação ficam no MAPA DE ATIVIDADES. É necessário participar do
Encontro Presencial Obrigatório.
Caso o aluno fique retido em mais de duas disciplinas, que pode também ser
consequência do acúmulo de dependências de períodos anteriores ou de
adaptações não realizadas, ou no caso de aluno no último ano do curso que ficar
retido em uma disciplina, fica obrigado a repetir o ano. Neste caso, as disciplinas
26
devem ser cursadas em regime regular e não de dependência, e o aluno passará à
condição de “aluno retido” e não de “aluno regular”.
Os critérios de aprovação para alunos retidos são os mesmos dos alunos
regulares.
4.7 AULAS DE DEPENDÊNCIA E ADAPTAÇÃO
As aulas de dependência e adaptação serão ministradas de acordo com
calendário específico a ser divulgado.
O aluno deverá matricular-se nas disciplinas em adaptação no ano em que
ingressar na faculdade e, caso não possa cursá-las, deverá requerer o seu
adiamento com assinatura de um termo de ciência no Help Center, nos prazos
estabelecidos no calendário escolar.
Os alunos que solicitarem o adiamento ou ficarem reprovados em uma
disciplina de adaptação terão de cursá-la em regime de dependência no ano letivo
seguinte, ou seja, perdem a gratuidade e entram nas regras de disciplinas em
dependência.
4.8 ENTREGA DE ATESTADO MÉDICO
O atestado médico deverá ser entregue em, no máximo, 48 horas após o
atendimento hospitalar e/ou alta médica para que o aluno possa se enquadrar no
Decreto-Lei nº 1.044/69. A entrega pode ser realizada por representante do aluno,
desde que seja comprovado o parentesco.
O Atestado Médico deve apresentar os seguintes requisitos:
I. Ser em via original, no qual conste o nome do paciente.
27
II. Especificação do tempo de concessão da licença.
III. Local, data, assinatura e carimbo do médico atestante, bem como número
de seu registro no Conselho Regional de Medicina (CRM).
Atestado de trabalho e licença matrimonial não abonam faltas.
4.9 REVISÃO DE NOTAS
A revisão de lançamento de notas deverá ser solicitada ao Help Center em
até 7 (sete) dias corridos após a divulgação na plataforma FIAP ON.
Não serão aceitos pedidos de revisão fora deste prazo.
4.10 ALUNAS GESTANTES
As alunas gestantes estarão amparadas pela lei nº 6.202, de 17 de abril de
1975, a partir do 8º mês de gestação, podendo ficar afastadas por um período de
noventa dias.
Para requerer o amparo legal, a aluna gestante deverá se dirigir ao Help
Center munida de atestado médico, antes do início do 8º mês de gestação.
4.11 COLAÇÃO DE GRAU
A Colação de Grau é o ato formal de conclusão de curso e, como atividade
escolar, terá suas normas baixadas em portaria da direção da faculdade (Normas
Protocolares para a “Solenidade de colação de grau dos alunos dos cursos de
graduação”). Terá direito à Colação de Grau o aluno que tiver concluído os estudos,
com aproveitamento e frequência fixados, em todas as exigências do currículo pleno
28
do curso. Além disso, também deve estar com sua documentação exigida completa
no Help Center, não apresentar pendências na Biblioteca e com pagamento em dia
no Help Center.
5 ESTÁGIO
5.1 ESTÁGIO PROFISSIONALIZANTE
O estudante universitário pode realizar estágios em empresas em qualquer
fase do curso, é destinado a alunos que queiram ingressar no mercado de trabalho e
adquirir vivência prática profissional. A FIAP possui o departamento Talent Lab a fim
de proporcionar orientações e auxílio.
As solicitações de assinaturas do Termo de Contrato de Estágio, Acordo de
Cooperação e Relatório de Atividades devem ser realizadas no Help Center, onde
são analisados enquanto às informações necessárias de acordo com a Lei nº
11.788, de 25 de setembro de 2008, que dispõe sobre o estágio de estudantes e não
há taxa para essa solicitação.
Prazo: em até 5 (cinco) dias úteis.
6 BOLSAS DE ESTUDO
6.1 BOLSAS DE MÉRITO ACADÊMICO
A FIAP incentiva seus alunos com programas de bolsas de estudo com base
em seu desempenho acadêmico.
29
Como incentivo aos melhores alunos, semestralmente a FIAP concede bolsas
parciais aos alunos com as 3 (três) maiores médias semestrais. Eles são premiados
com bolsas de 30% (primeiro lugar), 20% (segundo lugar) e 10% (terceiro lugar) nas
mensalidades do semestre seguinte à premiação, conforme: 1º semestre: março a
agosto, 2º semestre: setembro a fevereiro.
6.2 FIAP PLUS
Com base na performance acadêmica durante a graduação, o aluno pode
ganhar uma Bolsa de Estudos de 50% a 100% para um dos MBA FIAP.
Como Participar: 100% OFF em qualquer MBA FIAP para o melhor aluno de
cada curso (incluindo todos os turnos e unidades) e 50% OFF em qualquer MBA
FIAP para os 4 melhores alunos de cada curso (classificação segundo as médias
mais altas).
A relação dos MBAs disponíveis vai ser definida pelo FIAP – Centro
Universitário no momento da solicitação da Bolsa. O aluno não pode ter tido
nenhuma dependência durante o curso. Após efetuar sua matrícula em um dos
cursos de MBA, o aluno não vai poder cancelá-la nem pedir a transferência de curso
ou de unidade.
Caso realize o cancelamento ou a transferência, o aluno perde o benefício da
Bolsa. Alunos que optarem pelo plano de pagamento estendido, devem estar
adimplentes no momento da solicitação da Bolsa. Está só pode ser solicitada a partir de 18 meses após a data da colação de grau do curso, e deve ser utilizada em até 5
anos a partir daquela data. Bolsa válida para os MBAs que fizerem parte do portfólio FIAP na época da solicitação."""]
                    },
                    
                    #resposta que a ia deveria gerar para o propmt de treinanmento
                    {
                    "role": "model",
                    "parts": ["""
                              Resumo: Manual do Aluno FIAP - Centro Universitário\n
                              O Manual do Aluno da FIAP - Centro Universitário apresenta informações essenciais para a comunidade acadêmica, incluindo alunos, pais, responsáveis, professores e colaboradores. O manual destaca o compromisso da instituição com a educação de qualidade em tecnologia, inovação e empreendedorismo, mesmo durante os desafios impostos pela pandemia de Covid-19.\n\n
                              Estrutura e Serviços:\n\n
                              A FIAP oferece uma infraestrutura moderna e completa, com laboratórios de alta tecnologia, plataformas de ensino diferenciadas, biblioteca física e virtual, além de serviços de apoio ao aluno como o Talent Lab e o Help Center. A plataforma FIAP ON e o aplicativo FIAP ON proporcionam acesso a conteúdos online, ferramentas de comunicação e serviços acadêmicos.\n\n
                              Modelo Acadêmico e Avaliação:\n\n
                              O modelo acadêmico do FIAP ON é baseado no aprendizado orientado a projetos (PBL), com atividades práticas e avaliações à distância (AD) e presenciais obrigatórias (APO). O sistema de avaliação considera a participação em encontros presenciais/digitais, o desempenho nas ADs e APOs, e a realização de provas substitutivas e de exame, quando necessário.\n\n
                              Informações Acadêmicas e Bolsas de Estudo:\n\n
                              O manual detalha informações sobre matrículas, trancamento de matrícula, transferências, alunos com dependência, aulas de dependência e adaptação, entrega de atestado médico, revisão de notas, alunas gestantes e colação de grau. A FIAP oferece bolsas de mérito acadêmico e o programa FIAP Plus, que concede bolsas de estudo para cursos de MBA com base no desempenho acadêmico durante a graduação.\n\n
                              Compromisso com a Saúde e Segurança:\n\n
                              Em resposta à pandemia de Covid-19, a FIAP implementou medidas para garantir a saúde e segurança da comunidade acadêmica, incluindo novo horário de funcionamento das unidades, atendimento remoto, aulas 100% remotas, rodízio de times administrativos, distanciamento social, uso obrigatório de máscara, higienização das mãos e comunicação transparente sobre casos de Covid-19 dentro da instituição.\n\n
                              Conclusão:\n\n
                              O Manual do Aluno da FIAP - Centro Universitário demonstra o compromisso da instituição em oferecer uma experiência acadêmica completa e de alta qualidade, com foco na formação de profissionais preparados para o mercado de trabalho. A FIAP se destaca por sua estrutura moderna, modelo acadêmico inovador, serviços de apoio ao aluno e atenção à saúde e segurança da comunidade acadêmica.\n\n
                              """]
                    }
                    ]
                          )
  
  #construção do prompt para o usuário, contatenando o texto
  convo.send_message(f"""Faça um resumo sobre, seguindos os exemplos, deste texto: {conteudo}\n
                      Não esqueceça de fazer uma pequena lista com os topicos principais.""")

  #resposta da IA para o prompt do usuário
  resposta_pdf = convo.last.text

  #retorna a respota para a main
  return resposta_pdf

#funcao que faz a leitura do pdf
def ler_pdf(pdf):
  #comando que efetua o acesso ao pdf
  leitor_pdf = PyPDF2.PdfReader(pdf)
  #salva o número de páginas do pdf
  num_pages = len(leitor_pdf.pages)

  #inicializa uma string com 0, para verificação posterior
  conteudo = "0"
  #laço para rodar todas as páginas
  for page_num in range(num_pages):
    #concatena o texto de cada pagina do pdf
    conteudo += leitor_pdf.pages[page_num].extract_text()
    #retorna todo o conteudo do pdf (concatenado)
  return conteudo

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

  on = st.toggle("Mostrar parâmetros da IA.")

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
