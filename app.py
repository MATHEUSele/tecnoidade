from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tecnoidade_mvp_secret_key'

# Banco de dados simulado em memória
MOCK_USERS = {
    "maria@teste.com": {"senha": "123", "tipo": "idoso", "nome": "Maria das Graças", "telefone": "(83) 99999-9999", "idade": 67, "codigo": "12345"},
    "ana@teste.com": {"senha": "123", "tipo": "cuidador", "nome": "Ana Paula", "telefone": "(83) 98888-8888", "idade": 35, "vinculados": []}
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
            
            return redirect(url_for('termos_uso'))
        else:
            erro = "Dados incorretos. Por favor, tente novamente."
            
    return render_template('entrar.html', erro=erro, tipo=tipo_esperado)


@app.route('/login_google')
def login_google():
    return render_template('cadastro_google.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    tipo = request.args.get('tipo', 'idoso')
    if request.method == 'POST':
        nome = request.form.get('nome', 'Novo Usuário')
        email = request.form.get('email', 'novo@teste.com')
        senha = request.form.get('senha', '123')
        
        # Mocking creation in dict to allow login
        MOCK_USERS[email.lower()] = {"senha": senha, "tipo": tipo, "nome": nome}
        
        session['email'] = email.lower()
        session['nome'] = nome
        session['tipo'] = tipo
        
        return redirect(url_for('termos_uso'))
            
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
    email = session.get('email', 'maria@teste.com')
    user = MOCK_USERS.get(email, {"nome": "Usuário", "idade": 60})
    return render_template('tela_inicial.html', user=user)

@app.route('/editar_perfil')
def editar_perfil():
    email = session.get('email', 'maria@teste.com')
    user = MOCK_USERS.get(email, {"nome": "Usuário", "telefone": ""})
    return render_template('editar_perfil.html', user=user, email=email)

@app.route('/editar_perfil_idoso_action', methods=['POST'])
def editar_perfil_idoso_action():
    old_email = session.get('email')
    
    nome = request.form.get('nome', '').strip()
    novo_email = request.form.get('email', '').strip().lower()
    senha = request.form.get('senha', '').strip()
    telefone = request.form.get('telefone', '').strip()
    
    if not old_email or old_email not in MOCK_USERS:
        return redirect(url_for('boas_vindas'))
    
    user_data = MOCK_USERS[old_email]
    
    if nome:
        user_data['nome'] = nome
        session['nome'] = nome
    if telefone:
        user_data['telefone'] = telefone
    if senha and len(senha) >= 6:
        user_data['senha'] = senha
        
    # Se mudou de email, precisamos atualizar a chave do dicionario e a sessao
    if novo_email and novo_email != old_email:
        MOCK_USERS[novo_email] = user_data
        del MOCK_USERS[old_email]
        session['email'] = novo_email
        
    flash("Perfil atualizado com sucesso!")
    return redirect(url_for('perfil'))

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
    curso = request.args.get('curso', '')
    return render_template('curso_concluido.html', curso=curso)

# -------------------------------------------------------------
# FLUXO DO CUIDADOR
# -------------------------------------------------------------
@app.route('/familiar_vincular')
def familiar_vincular():
    return render_template('familiar_vincular.html')

@app.route('/familiar_dashboard')
def familiar_dashboard():
    email = session.get('email', 'ana@teste.com')
    cuidador = MOCK_USERS.get(email, {"nome": "Familiar", "vinculados": []})
    
    idoso_vinculado = None
    if cuidador.get('vinculados'):
        idoso_email = cuidador['vinculados'][0]
        idoso_vinculado = MOCK_USERS.get(idoso_email)
        
    return render_template('familiar_dashboard.html', cuidador=cuidador, idoso=idoso_vinculado)

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
    codigo = request.form.get('codigo_completo', '').strip()
    email_cuidador = session.get('email')
    
    if not email_cuidador or email_cuidador not in MOCK_USERS:
        return redirect(url_for('boas_vindas'))
        
    cuidador = MOCK_USERS[email_cuidador]
    
    # Buscar idoso com esse codigo
    idoso_encontrado = None
    for email_idoso, dados in MOCK_USERS.items():
        if dados.get('tipo') == 'idoso' and dados.get('codigo') == codigo:
            idoso_encontrado = email_idoso
            break
            
    if idoso_encontrado:
        if 'vinculados' not in cuidador:
            cuidador['vinculados'] = []
        if idoso_encontrado not in cuidador['vinculados']:
            cuidador['vinculados'].append(idoso_encontrado)
        flash("Vínculo efetuado com sucesso")
        return redirect(url_for('familiar_dashboard'))
    else:
        flash("Código não encontrado. Verifique com o idoso.")
        return redirect(url_for('familiar_vincular'))

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

@app.route('/politica_privacidade', methods=['GET', 'POST'])
def politica_privacidade():
    if request.method == 'POST':
        acao = request.form.get('acao')
        if acao == 'recusar':
            session.clear()
            return redirect(url_for('entrar'))
        
        tipo = session.get('tipo', 'idoso')
        email = session.get('email')
        if not email:
            return redirect(url_for('boas_vindas'))
            
        user = MOCK_USERS.get(email, {})
        if tipo == 'idoso':
            return redirect(url_for('home'))
        else:
            if not user.get('vinculados'):
                return redirect(url_for('familiar_vincular'))
            return redirect(url_for('familiar_dashboard'))
            
    return render_template('politica_privacidade.html')

@app.route('/tela_2_boas_vindas')
def tela_2_boas_vindas():
    return render_template('tela_2_boas_vindas.html')

@app.route('/tela_3')
def tela_3():
    return render_template('tela_3.html')

@app.route('/termos_uso', methods=['GET', 'POST'])
def termos_uso():
    if request.method == 'POST':
        acao = request.form.get('acao')
        if acao == 'recusar':
            session.clear()
            return redirect(url_for('entrar'))
        return redirect(url_for('politica_privacidade'))
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
def cgiturso_compras_aula1():
    return render_template('curso_compras_aula1.html')

@app.route('/curso_compras_aula2')
def curso_compras_aula2():
    return render_template('curso_compras_aula2.html')

@app.route('/curso_compras_aula3')
def curso_compras_aula3():
    return render_template('curso_compras_aula3.html')

import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
    