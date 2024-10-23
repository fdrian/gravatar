import hashlib
import requests
import argparse
import os

def get_gravatar_image(email, save_dir, size=200):
    # Gera o hash MD5 do e-mail em letras minúsculas e sem espaços
    email = email.strip().lower()
    hash_email = hashlib.md5(email.encode()).hexdigest()
    
    # Monta a URL do Gravatar
    gravatar_url = f"https://www.gravatar.com/avatar/{hash_email}?s={size}"
    
    # Faz a requisição para obter a imagem
    response = requests.get(gravatar_url)
    
    if response.status_code == 200:
        # Verifica se a pasta existe, caso contrário, cria
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        # Define o caminho completo do arquivo onde a imagem será salva
        file_path = os.path.join(save_dir, f'{hash_email}_gravatar.jpg')
        
        # Salva a imagem localmente
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        print(f"Imagem gravada em '{file_path}'")
    else:
        print(f"Erro ao obter a imagem. Status code: {response.status_code}")

if __name__ == "__main__":
    # Configura o argparse para lidar com argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Obter a imagem do Gravatar a partir de um e-mail.")
    parser.add_argument("email", help="E-mail do usuário para obter o Gravatar.")
    parser.add_argument("--save-dir", default="./avatars", help="Diretório onde a imagem será salva (padrão: ./pictures).")
    
    # Parseia os argumentos fornecidos
    args = parser.parse_args()
    
    # Obtém a imagem do Gravatar e salva no diretório especificado
    get_gravatar_image(args.email, args.save_dir)
