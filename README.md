# Resume AI ✍️: Resumos Automáticos com Inteligência Aritificial (Google AI Studio)

O **Resume AI** é uma ferramenta que utiliza a API do Google e a inteligência artificial para gerar resumos automáticos a partir de textos e documentos.

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

1. [Instalação](#instalacao)

2. [Utilização](#utilizacao)

3. [Como funciona](#como-funciona)

4. [Observações](#observacoes)

5. [Contato](#contato)

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
cd summit
python -m pip install -r requirements.txt
```

**Observações**:

## Utilização

1. **Acesse o local em que a ferramente está hospedada**

```bash
Streamlit - [https://resumeia.streamlit.app](https://resumeia.streamlit.app])
```
## Utilização Local

1. **Execute o script usnado o streamlit**:

```bash
streamlit run .\dashboard.py
```

2. **URL Local**:
```bash
A execução do código acima irá retonar a URL Local (localhost:XXXX). Cole-a no em seunavegador
```

## Como funciona

1. **O Summit acessa o Google Drive**: Busca automaticamente por arquivos de vídeo na pasta configurada no arquivo `.env`.

2. **Processamento de cada vídeo**:
- **Armazenamento local**: O vídeo é armazenado localmente no computador.

- **Extração de áudio**: Somente o áudio é extraído do vídeo para reduzir o uso de tokens da API do Ai Studio.

- **Análise do Ai Studio**: O arquivo de áudio é enviado para o Ai Studio, que gera um resumo da reunião.

- **Armazenamento do resumo**: O resumo é armazenado em uma lista.
3. **Envio de emails**:
- **Criação de emails**: Para cada resumo, um email é criado com o conteúdo do resumo e os destinatários informados.

- **Envio via API do Gmail**: Os emails são enviados para os destinatários usando a API do Gmail.

## Observações

- O Summit está em desenvolvimento e novas funcionalidades serão adicionadas em breve.

- Se você encontrar algum problema, por favor, envie um relatório de bug no repositório do GitHub.

## Contato

Para obter mais informações sobre o Summit ou para relatar problemas, você pode entrar em contato conosco através dos seguintes canais:

- **LinkedIn:** [Fellipe Machado](https://www.linkedin.com/in/fellipe-luz/)
- **Email:** fellipe.luz.machado@gmail.com

Agradecemos seu interesse no Summit!
