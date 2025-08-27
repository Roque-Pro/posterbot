import os
import requests
from flask import Flask, request, redirect
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do arquivo .env

app = Flask(__name__)

# Carregar variáveis do arquivo .env
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = "r_liteprofile w_member_social"  # Escopos para acessar o perfil e postar

# Geração do link de autenticação OAuth
@app.route('/')
def login():
    auth_url = f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}"
    return redirect(auth_url)

# Rota de callback para trocar o código de autorização por Access Token
@app.route('/callback')
def callback():
    # O código de autorização vindo do LinkedIn
    code = request.args.get('code')
    
    # URL para trocar o código por Access Token
    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    # Envia a requisição para pegar o Access Token
    response = requests.post(token_url, headers=headers, data=data)
    access_token = response.json().get('access_token')
    
    return f"Access Token: {access_token}"  # Aqui você verá o Access Token no navegador

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

