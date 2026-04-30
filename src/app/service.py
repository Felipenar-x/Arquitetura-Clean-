from src.infrastructure.persist import repo_obter_todos_livros

def service_listar_livros_filtrados(categoria=None, nome=None):
    dados = repo_obter_todos_livros()
    
    # Filtro por Categoria
    if categoria:
        dados = [l for l in dados if l["categoria"].lower() == categoria.lower()]
    
    # Filtro por Nome (Nova Feature)
    if nome:
        dados = [l for l in dados if nome.lower() in l["titulo"].lower()]
        
    return dados

from datetime import datetime
from src.infrastructure.persist import repo_obter_promocoes_ativas

def service_obter_banner_sazonal():
    mes_atual = datetime.now().month
    promocoes = repo_obter_promocoes_ativas()
    
    for promo in promocoes:
        if promo["mes"] == mes_atual:
            return promo
    return None 