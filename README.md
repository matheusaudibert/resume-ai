# Resume AI ✍️: Resumos Automáticos com Inteligência Artificial (Google AI Studio)

O Resume AI é uma ferramenta que utiliza a API do Google e a inteligência artificial para gerar resumos automáticos a partir de textos e documentos.

![Logo](docs/resume_ai_interface.png)

## Recursos:

-  📦 **Upload Simples:** Os usuários podem enviar arquivos (PDFs).
  
- 💡 **Resumos Instantâneos:** A IA do Google Generative permite gerar resumos precisos e rápidos do conteúdo fornecido.
  
- 😃 **Visualização Amigável**: Explore seus resumos de forma organizada e fácil de entender.
  
- 📲 **Acesso em Qualquer Lugar**: Use o **Resume AI** aplicação em qualquer dispositivo com acesso à internet.

## Benefícios

- ⌚️ **Economia de Tempo:** Ao utilizar o Resume AI para gerar resumos instantâneos, você economiza tempo valioso que pode ser direcionado para outras tarefas prioritárias.
  
- 🧱 **Aumento da Produtividade:** Tome decisões mais rápidas e eficazes com base nos resumos claros e concisos gerados pelo Resume AI, impulsionando a produtividade do seu trabalho.

## Índice

1. [Instalação](#instalação)

2. [Utilização Remota](#utilização-remota)

3. [Utilização Local](#utilização-local)

4. [Como funciona](#como-funciona)

5. [Observações](#observaçõess)

6. [Contato](#contato)

## Instalação

**Pré-requisitos**:

- Python 3.11 ou superior

- Pip

- Conta no Goole AI Studio

**Passos**:

1. **Clone o repositório**:

```bash
https://github.com/matheusaudibert/resume_ai.git
```

2. **Instale as dependências:**

```bash
cd dashboard
python -m pip install -r requirements.txt
```

**Observações**:

## Utilização Remota

1. **Acesse o local em que a ferramente está hospedada**

**Resume AI** - [https://resumeia.streamlit.app](https://resumeia.streamlit.app)

2. **Cole sua API KEY**

Você deve inserir sua chave da API do Google AI studio para se conectar.
**Não tem chave?** [Gere] uma [aqui!](https://aistudio.google.com/app/apikey)

## Utilização Local

1. **Execute o script usnado o streamlit**:

```bash
streamlit run .\dashboard.py
```

2. **URL Local**:
```bash
A execução do código acima irá retonar a URL Local (localhost:XXXX). Cole-a no em seu navegador.
```

## Como funciona

1. **O Resume AI recebe o prompt do usuário**: O usuário entra com algum conteúdo que deseja receber o resumo. Documento PDF ou texto.

3. **Recebe a API KEY do usuário**: Desta maneira o **Resume AI** consegue se conectar com o Google AI Studio.

4. **A Inteligência Artificial gera o resumo**: A IA, que foi previamente alimentada com prompts técnicos, entrega o resumo do arquivo que o usuário envio para resumir. 

## Observações

- O **Resume AI** está em processo de desenvolvimento. Futuramente sugirão novas possibilidades, como, entrada de **imagens**, **vídeos**, **áudios**, **planilhas**, **códigos**, entre outros.
  
- Se encontrar algum bug, por favor, envie um relatório de bug no repositório do GitHub.
  
- A documentação do código será feita em breve.

## Contato

Para obter mais informações sobre o Resumi AI ou me conhecer, você pode entrar em contato comigo através dos seguintes canais:

- **LinkedIn:** [Matheus Audibert](https://www.linkedin.com/in/matheusaudibert/)
- **Email:** matheusaudibert2019@outlook.com
- **Discord:** hvmex