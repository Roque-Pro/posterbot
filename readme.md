# Poster Bot

Este é um bot para **LinkedIn** que publica automaticamente conteúdo diário relacionado a **Fullstack Python** e **Análise de Dados**.

## Funcionalidade

- Gera postagens diárias com texto e imagens sobre temas como:
  - Desenvolvimento Fullstack com Python
  - Dicas e tutoriais sobre Análise de Dados
- Publica automaticamente no **LinkedIn** uma vez por dia.

## Tecnologias

- **Flask**: Para criar a aplicação web que irá lidar com a autenticação OAuth 2.0.
- **APScheduler**: Para agendar as postagens diárias.
- **requests**: Para interagir com a API do LinkedIn.

## Como Rodar Localmente

1. **Clone o repositório**:

```bash
git clone https://github.com/seu-usuario/poster-bot.git
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

env
Copiar código
CLIENT_ID=seu_client_id
CLIENT_SECRET=seu_client_secret
REDIRECT_URI=http://localhost:5000/callback
Execute o bot:

bash
Copiar código
python app.py
Acesse http://localhost:5000/ no navegador para autorizar o bot.

Deploy
Para hospedar a aplicação, siga os seguintes passos:

Crie um repositório no Render.

Faça o deploy a partir deste repositório no Render.

Defina as variáveis de ambiente no painel do Render para CLIENT_ID, CLIENT_SECRET, e REDIRECT_URI.

Licença
Este projeto é de código aberto sob a licença MIT.

yaml
Copiar código

---

### **Passo 4: Subir o README para o GitHub**

1. Após criar o arquivo `README.md`, faça o **commit** e o **push** novamente:

```bash
git add README.md
git commit -m "Adicionado README básico"
git push