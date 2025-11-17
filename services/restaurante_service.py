import json
import requests

class RestauranteService:

    URL = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    DB = 'database/avaliacoes.json'

    # ---- Consumir API Externa ----
    @classmethod
    def buscar_dados(cls):
        response = requests.get(cls.URL)

        if response.status_code == 200:
            return response.json() # converte JSON da internet → objeto Python (apenas visualização)
        else:
            return None
    
    # ---- Filtrar restaurante específico ----
    @classmethod
    def filtrar_restaurante(cls, nome):
        dados = cls.buscar_dados()

        if dados is None:
            return None
        
        cardapio = [
            {
                'item': item['Item'],
                'price': item['price'],
                'description': item['description']
            }
            for item in dados if item['Company'].lower() == nome.lower()
        ]

        return cardapio
    
    # ---- Salvar avaliação ----
    @classmethod
    def salvar_avaliacao(cls, restaurante, nota, comentario):
        with open(cls.DB, 'r') as arquivo:
            avaliacoes = json.load(arquivo) # Lê o arquivo e carrega a lista existente de avaliações
        
        nova_avaliacao = {
            'restaurante': restaurante,
            'nota': nota,
            'comentario': comentario
        }

        avaliacoes.append(nova_avaliacao)

        with open(cls.DB, 'w') as arquivo:
            json.dump(avaliacoes, arquivo, indent=4)

        return nova_avaliacao
    
    # ---- Buscar avaliações ----
    @classmethod
    def buscar_avaliacoes(cls, restaurante):
        with open(cls.DB, 'r') as arquivo:
            avaliacoes = json.load(arquivo)
        
        filtradas = [
            a for a in avaliacoes
            if a['restaurante'].lower() == restaurante.lower()
        ]

        return filtradas
