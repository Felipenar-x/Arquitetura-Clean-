from src.app.service import service_listar_livros_filtrados

def livro_controller_index(categoria_solicitada, nome_pesquisado):
    livros = service_listar_livros_filtrados(categoria_solicitada, nome_pesquisado)
    
    return {
        "livros": livros,
        "categoria_atual": categoria_solicitada,
        "busca": nome_pesquisado
    }

from src.app.service import service_listar_livros_filtrados, service_obter_banner_sazonal

def livro_controller_index(categoria, nome):
    livros = service_listar_livros_filtrados(categoria, nome)
    banner = service_obter_banner_sazonal() 
    
    return {
        "livros": livros,
        "banner": banner,
        "categoria_atual": categoria,
        "busca": nome
    }