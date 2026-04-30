from flask import Flask, render_template, request
from src.infrastructure.persist import TxtLivroRepository
from src.app.service import LivroService

app = Flask(__name__, template_folder='src/presentation/templates')

repo = TxtLivroRepository("livros.txt", "promocoes.txt")
service = LivroService(repo)

@app.route('/')
def index():

    categoria = request.args.get('categoria')
    busca = request.args.get('q')
    

    livros = service.listar_livros_com_notas(categoria, busca)
    

    banner = service.obter_banner()
    
    return render_template(
        'index.html', 
        livros=livros, 
        banner=banner, 
        categoria_atual=categoria, 
        busca=busca
    )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)