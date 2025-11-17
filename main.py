from fastapi import FastAPI
from services.restaurante_service import RestauranteService

app = FastAPI()

# ---- 1. Listar todos os restaurantes ----
@app.get('/api/restaurantes/')
def listar_restaurantes():
    dados = RestauranteService.buscar_dados()
    return {'restaurantes': dados}

# ---- 2. Pegar cardápio de um restaurante específico ----
@app.get('/api/restaurantes/{nome}')
def cardapio_restaurante(nome: str):
    cardapio = RestauranteService.filtrar_restaurante(nome)

    if not cardapio:
        return {'erro': f'O restaurante "{nome}" não foi encontrado.'}
    
    return {
        'restaurante': nome,
        'cardapio': cardapio
    }

# ---- 3. Enviar avaliação (POST) ----
@app.get('/api/restaurantes/{nome}/avaliar')
def avaliar_restaurante(nome: str, nota: float, comentario: str):
    RestauranteService.salvar_avaliacao(nome, nota, comentario)

    return {
        'mensagem': f'Avaliação registrada com sucesso para {nome}',
        'nota': nota,
        'comentario': comentario
    }

# ---- 4. Ver avaliações de um restaurante ----
@app.get('/api/restaurantes/{nome}/avaliacoes')
def listar_avaliacoes(nome: str):
    avaliacoes = RestauranteService.buscar_avaliacoes(nome)

    return {
        'restaurante': nome,
        'avaliacoes': avaliacoes
    }
