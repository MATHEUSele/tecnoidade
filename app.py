from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/tela1')
def tela1():
    return render_template('tela1.html')

@app.route('/tela2')
def tela2():
    return render_template('tela2.html')

@app.route('/tela3')
def tela3():
    return render_template('tela3.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        return redirect(url_for('entrar'))
    return render_template('cadastro.html')

@app.route('/', methods=['GET', 'POST'])
def entrar():
    erro = None
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        senha = request.form.get('senha', '').strip().lower()
        
        # Verificando se é admin (aceitando também a digitação adim/admim)
        if email in ['admin', 'adim', 'admim'] and senha in ['admin', 'adim', 'admim']:
            return redirect(url_for('home', nome='Admin'))
        else:
            erro = "Dados incorretos. Por favor, coloque o nome de novo."
            
    return render_template('entrar.html', erro=erro)

@app.route('/home')
def home():
    nome = request.args.get('nome', 'Maria')
    return render_template('home.html', nome=nome)

if __name__ == '__main__':
    print("Iniciando o servidor TecnoIdade...")
    print("Abra no seu navegador: http://127.0.0.1:5000/tela1")
    app.run(debug=True, port=5000)
