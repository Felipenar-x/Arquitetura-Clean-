from flask import Flask, render_template, request
from src.presentation.controller import livro_controller_index

app = Flask(__name__, template_folder='src/presentation/templates')

@app.route('/')
def index():
    categoria = request.args.get('categoria')
    busca = request.args.get('q')
    

    dados = livro_controller_index(categoria, busca)

    return render_template('index.html', 
                           livros=dados["livros"], 
                           categoria_atual=dados["categoria_atual"],
                           busca=dados["busca"],
                           banner=dados.get("banner")) 

if __name__ == '__main__':
    app.run(debug=True)