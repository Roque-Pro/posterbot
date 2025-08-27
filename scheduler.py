from apscheduler.schedulers.background import BackgroundScheduler
import random
import requests
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente
load_dotenv()

# Função para gerar conteúdo (pode ser substituída por um gerador real)
def gerar_conteudo():
    dicas = [
        "Dica do dia: Aprenda como fazer um CRUD em Python com Flask! #FullstackPython #Desenvolvimento",
        "Tutorial: Como analisar dados usando Pandas no Python! #DataScience #Python",
        "Fullstack Python: Como integrar Frontend com Backend com Django e React! #WebDev #Python",
        "Análise de Dados: Como criar visualizações interativas com Matplotlib! #DataScience #Python"
    ]
    
    conteudo = random.choice(dicas)  # Pega uma dica aleatória
    return conteudo

# Função para postar no LinkedIn
def postar_linkedin(conteudo):
    # Usar o Access Token aqui
    access_token = os.getenv("ACCESS_TOKEN")  # Adicione sua variável de ambiente com o token
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }

    data = {
        "author": "urn:li:person:SEU_PERSON_ID",  # Substitua pelo seu ID do LinkedIn
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": conteudo
                },
                "shareMediaCategory": "IMAGE",
                "media": [
                    {
                        "status": "READY",
                        "media": "SEU_IMAGE_URL",  # Insira o URL da imagem gerada
                        "title": {"text": "Imagem do conteúdo"}
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Postagem realizada com sucesso!")
    else:
        print(f"Erro ao realizar a postagem: {response.json()}")

# Função para agendar a postagem diária
def agendar_postagens():
    scheduler = BackgroundScheduler()

    # Agendar para rodar uma vez por dia (exemplo: todo dia às 9h)
    scheduler.add_job(lambda: postar_linkedin(gerar_conteudo()), 'interval', days=1, start_date='2025-08-28 09:00:00')

    scheduler.start()

if __name__ == "__main__":
    agendar_postagens()
