import requests
from requests.exceptions import ConnectionError, RequestException

def obter_lista_do_cardapio():
    try:
        resposta = requests.get("http://127.0.0.1:8000/produtos")

    except ConnectionError:
        return (f'\033[31mNão foi possível conectar à API. Verifique se o servidor está rodando.\033[m')

    except RequestException:
        return(f'\033[31mOcorreu um erro! Tente novamente\033[m')
    
    if resposta.status_code in range(200, 300):
        produtos = resposta.json()
        
        return produtos
    
    else:    
        return(f'\033[31mOcorreu um erro ao buscar os produtos!\033[m. HTTP {resposta.status_code}')

def cadastrar_produto(nome, categoria, preco):
    url_base = "http://127.0.0.1:8000"
    
    try:
    
        resposta = requests.post(
            url_base + "/produtos",
            
            json={
                "nome": nome,
                "categoria": categoria,
                "preco": preco
            }
        )
    
    except ConnectionError:
        return ('\033[31mNão foi possível conectar à API. Verifique se o servidor está rodando.\033[m')
    
    except RequestException:
        return(f'\033[31mOcorreu um erro! Tente novamente\033[m')
    
    if resposta.status_code in range(200, 300):
        return (f'\033[32mProduto cadastrado com sucesso no banco de dados! HTTP {resposta.status_code}\033[m')
    
    else:
        return (f'\033[31mOcorreu um erro. Tente novamente! HTTP {resposta.status_code}\033[m')