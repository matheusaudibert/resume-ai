import google.generativeai as genai
import settings

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