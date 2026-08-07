from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tecnoidade_mvp_secret_key'

# Banco de dados simulado em memória
MOCK_USERS = {
    "maria@teste.com": {"senha": "123", "tipo": "idoso", "nome": "Maria das Graças"},
    "ana@teste.com": {"senha": "123", "tipo": "cuidador", "nome": "Ana Paula"}
}

# -------------------------------------------------------------
# FLUXO INICIAL
# -------------------------------------------------------------
@app.route('/')
def splash():
    # Tela inicial que redireciona para a tela de boas vindas
    return redirect(url_for('boas_vindas'))

@app.route('/boas_vindas')
def boas_vindas():
    return render_template('tela1.html')

@app.route('/escolha_perfil')
def escolha_perfil():
    return render_template('tela2.html')

# -------------------------------------------------------------
# AUTENTICAÇÃO
# -------------------------------------------------------------
@app.route('/entrar', methods=['GET', 'POST'])
def entrar():
    erro = None
    tipo_esperado = request.args.get('tipo', 'idoso')
    
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        senha = request.form.get('senha', '').strip().lower()
        
        # Verificar credenciais mockadas
        if email in MOCK_USERS and MOCK_USERS[email]['senha'] == senha:
            user = MOCK_USERS[email]
            session['email'] = email
            session['nome'] = user['nome']
            session['tipo'] = user['tipo']
            
            if user['tipo'] == 'idoso':
                return redirect(url_for('home'))
            else:
                return redirect(url_for('familiar_dashboard'))
        else:
            erro = "Dados incorretos. Por favor, tente novamente."
            
    return render_template('entrar.html', erro=erro, tipo=tipo_esperado)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    tipo = request.args.get('tipo', 'idoso')
    if request.method == 'POST':
        nome = request.form.get('nome', 'Novo Usuário')
        email = request.form.get('email', 'novo@teste.com')
        senha = request.form.get('senha', '123')
        
        # Mocking creation in dict to allow login
        MOCK_USERS[email.lower()] = {"senha": senha, "tipo": tipo, "nome": nome}
        
        flash("Cadastro realizado com sucesso")
        return redirect(url_for('entrar', tipo=tipo))
            
    return render_template('cadastro.html', tipo=tipo)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('boas_vindas'))

# -------------------------------------------------------------
# FLUXO DO IDOSO
# -------------------------------------------------------------
@app.route('/preferencias')
def preferencias():
    return render_template('tela3.html')

@app.route('/home')
def home():
    nome = session.get('nome', 'Maria')
    return render_template('home.html', nome=nome)

@app.route('/aprender')
def aprender():
    return render_template('aprender.html')

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/perfil')
def perfil():
    return render_template('tela_inicial.html')

@app.route('/progresso')
def progresso():
    return render_template('progresso.html')

# -- Cursos Idoso --
@app.route('/curso_whatsapp')
def curso_whatsapp():
    return render_template('curso_whatsapp.html')

@app.route('/curso_whatsapp/conhecendo')
def curso_whatsapp_conhecendo():
    return render_template('curso_whatsapp_conhecendo.html')

@app.route('/curso_whatsapp/mensagem')
def curso_whatsapp_mensagem():
    return render_template('curso_whatsapp_mensagem.html')

@app.route('/curso_whatsapp/fotos')
def curso_whatsapp_fotos():
    return render_template('curso_whatsapp_fotos.html')

@app.route('/curso_whatsapp/video')
def curso_whatsapp_video():
    return render_template('curso_whatsapp_video.html')

@app.route('/curso_pix')
def curso_pix():
    return render_template('curso_pix.html')

@app.route('/curso_compras_online')
def curso_compras_online():
    # Se nao tiver, usa a tela de construcao
    return render_template('curso_compras_online.html')

@app.route('/curso_banco_digital')
def curso_banco_digital():
    return render_template('curso_banco_digital.html')

@app.route('/curso_seguranca_digital')
def curso_seguranca_digital():
    return render_template('curso_seguranca_digital.html')

@app.route('/curso_celular_basico')
def curso_celular_basico():
    return render_template('curso_celular_basico.html')

@app.route('/curso_gov')
def curso_gov():
    return render_template('curso_gov.html')

@app.route('/curso_concluido')
def curso_concluido():
    return render_template('curso_concluido.html')

# -------------------------------------------------------------
# FLUXO DO CUIDADOR
# -------------------------------------------------------------
@app.route('/familiar_vincular')
def familiar_vincular():
    return render_template('familiar_vincular.html')

@app.route('/familiar_dashboard')
def familiar_dashboard():
    nome = session.get('nome', 'Ana Paula')
    return render_template('familiar_dashboard.html', nome=nome)

@app.route('/familiar_lista')
def familiar_lista():
    return render_template('familiar_lista.html')

@app.route('/familiar_perfil')
def familiar_perfil():
    return render_template('familiar_perfil.html')

@app.route('/familiar_editar_perfil')
def familiar_editar_perfil():
    return render_template('familiar_editar_perfil.html')

@app.route('/familiar_configuracoes')
def familiar_configuracoes():
    return render_template('familiar_configuracoes.html')

@app.route('/familiar_excluir_conta')
def familiar_excluir_conta():
    return render_template('familiar_excluir_conta.html')


# --- Rotas Dinamicas Adicionadas Automaticamente ---
@app.route('/cadastro_alternativo_1')
def cadastro_alternativo_1():
    return render_template('cadastro_alternativo_1.html')

@app.route('/cadastro_erro')
def cadastro_erro():
    return render_template('cadastro_erro.html')

@app.route('/cadastro_google')
def cadastro_google():
    return render_template('cadastro_google.html')

@app.route('/cadastro_passo_1')
def cadastro_passo_1():
    return render_template('cadastro_passo_1.html')

@app.route('/cadastro_passo_2')
def cadastro_passo_2():
    return render_template('cadastro_passo_2.html')

@app.route('/curso_banco_aula1')
def curso_banco_aula1():
    return render_template('curso_banco_aula1.html')

@app.route('/curso_banco_aula2')
def curso_banco_aula2():
    return render_template('curso_banco_aula2.html')

@app.route('/curso_banco_aula3')
def curso_banco_aula3():
    return render_template('curso_banco_aula3.html')

@app.route('/curso_banco_aula4')
def curso_banco_aula4():
    return render_template('curso_banco_aula4.html')

@app.route('/curso_banco_aula5')
def curso_banco_aula5():
    return render_template('curso_banco_aula5.html')

@app.route('/curso_banco_aula6')
def curso_banco_aula6():
    return render_template('curso_banco_aula6.html')

@app.route('/curso_banco_aula7')
def curso_banco_aula7():
    return render_template('curso_banco_aula7.html')

@app.route('/curso_banco_aula8')
def curso_banco_aula8():
    return render_template('curso_banco_aula8.html')

@app.route('/curso_pix_aula1')
def curso_pix_aula1():
    return render_template('curso_pix_aula1.html')

@app.route('/curso_pix_aula2')
def curso_pix_aula2():
    return render_template('curso_pix_aula2.html')

@app.route('/curso_pix_aula3')
def curso_pix_aula3():
    return render_template('curso_pix_aula3.html')

@app.route('/curso_pix_aula4')
def curso_pix_aula4():
    return render_template('curso_pix_aula4.html')

@app.route('/curso_pix_aula5')
def curso_pix_aula5():
    return render_template('curso_pix_aula5.html')

@app.route('/curso_seguranca_aula1')
def curso_seguranca_aula1():
    return render_template('curso_seguranca_aula1.html')

@app.route('/curso_seguranca_aula2')
def curso_seguranca_aula2():
    return render_template('curso_seguranca_aula2.html')

@app.route('/curso_seguranca_aula3')
def curso_seguranca_aula3():
    return render_template('curso_seguranca_aula3.html')

@app.route('/curso_seguranca_aula4')
def curso_seguranca_aula4():
    return render_template('curso_seguranca_aula4.html')

@app.route('/curso_seguranca_aula5')
def curso_seguranca_aula5():
    return render_template('curso_seguranca_aula5.html')

@app.route('/curso_seguranca_aula6')
def curso_seguranca_aula6():
    return render_template('curso_seguranca_aula6.html')

@app.route('/curso_seguranca_aula7')
def curso_seguranca_aula7():
    return render_template('curso_seguranca_aula7.html')

@app.route('/curso_seguranca_aula8')
def curso_seguranca_aula8():
    return render_template('curso_seguranca_aula8.html')

@app.route('/familiar_atividade_concluida')
def familiar_atividade_concluida():
    return render_template('familiar_atividade_concluida.html')

@app.route('/familiar_onboarding')
def familiar_onboarding():
    return render_template('familiar_onboarding.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_biometria')
def login_biometria():
    return render_template('login_biometria.html')

@app.route('/login_biometria_action', methods=['POST'])
def login_biometria_action():
    # Simulando o sucesso da biometria
    user = MOCK_USERS["maria@teste.com"]
    session['email'] = "maria@teste.com"
    session['nome'] = user['nome']
    session['tipo'] = user['tipo']
    return redirect(url_for('home'))

@app.route('/vincular_conta_action', methods=['POST'])
def vincular_conta_action():
    flash("Vínculo efetuado com sucesso")
    return redirect(url_for('familiar_dashboard'))

@app.route('/excluir_conta_action', methods=['POST'])
def excluir_conta_action():
    session.clear()
    return redirect(url_for('splash'))

@app.route('/editar_perfil_action', methods=['POST'])
def editar_perfil_action():
    email = request.form.get('email', '').strip()
    if not email or '@' not in email:
        flash("Preencha todos os campos obrigatórios com formato válido", "error")
        return redirect(request.referrer or url_for('familiar_editar_perfil'))
    
    flash("Alteração realizada com sucesso", "success")
    return redirect(request.referrer or url_for('familiar_editar_perfil'))

@app.route('/login_erro')
def login_erro():
    return render_template('login_erro.html')

@app.route('/login_sucesso')
def login_sucesso():
    return render_template('login_sucesso.html')

@app.route('/politica_privacidade')
def politica_privacidade():
    return render_template('politica_privacidade.html')

@app.route('/tela_2_boas_vindas')
def tela_2_boas_vindas():
    return render_template('tela_2_boas_vindas.html')

@app.route('/tela_3')
def tela_3():
    return render_template('tela_3.html')

@app.route('/termos_uso')
def termos_uso():
    return render_template('termos_uso.html')

@app.route('/curso_celular_aula1')
def curso_celular_aula1():
    return render_template('curso_celular_aula1.html')

@app.route('/curso_celular_aula2')
def curso_celular_aula2():
    return render_template('curso_celular_aula2.html')

@app.route('/curso_celular_aula3')
def curso_celular_aula3():
    return render_template('curso_celular_aula3.html')

@app.route('/curso_celular_aula4')
def curso_celular_aula4():
    return render_template('curso_celular_aula4.html')

@app.route('/curso_gov_aula1')
def curso_gov_aula1():
    return render_template('curso_gov_aula1.html')

@app.route('/curso_gov_aula2')
def curso_gov_aula2():
    return render_template('curso_gov_aula2.html')

@app.route('/curso_gov_aula3')
def curso_gov_aula3():
    return render_template('curso_gov_aula3.html')

@app.route('/curso_compras_aula1')
def curso_compras_aula1():
    return render_template('curso_compras_aula1.html')

@app.route('/curso_compras_aula2')
def curso_compras_aula2():
    return render_template('curso_compras_aula2.html')

@app.route('/curso_compras_aula3')
def curso_compras_aula3():
    return render_template('curso_compras_aula3.html')

if __name__ == '__main__':
    print("Iniciando o MVP TecnoIdade...")
    print("Abra no seu navegador: http://127.0.0.1:5000/")
    app.run(debug=True, port=5000)
