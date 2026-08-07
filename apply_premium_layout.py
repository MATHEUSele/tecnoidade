import os

DATA = {
    'celular': {
        1: {"title": "Conhecendo os botões", "p": "Entenda para que serve cada botão físico e virtual do seu smartphone.", "s1": "Botão de ligar/desligar", "s2": "Botões de volume"},
        2: {"title": "Conectando ao WiFi", "p": "Aprenda a ligar o WiFi e colocar a senha da sua rede.", "s1": "Acessar configurações", "s2": "Selecionar a rede"},
        3: {"title": "Aumentar o Volume", "p": "Descubra como ajustar o som para mídia, chamadas e alarmes.", "s1": "Controle de mídia", "s2": "Modo silencioso"},
        4: {"title": "Instalar Aplicativos", "p": "Veja como baixar aplicativos com segurança pela loja oficial.", "s1": "Abrir a loja", "s2": "Buscar e instalar"},
    },
    'gov': {
        1: {"title": "Conhecendo Gov.br", "p": "Descubra o que é a plataforma Gov.br e por que ela é útil.", "s1": "O que é o portal", "s2": "Níveis de segurança"},
        2: {"title": "Entrar na Conta", "p": "Aprenda a fazer login com seu CPF e senha.", "s1": "Digitar o CPF", "s2": "Recuperar senha"},
        3: {"title": "Principais Serviços", "p": "Veja como acessar seus documentos digitais, como CNH e vacinação.", "s1": "Buscar serviços", "s2": "Acessar documentos"},
    },
    'pix': {
        1: {"title": "O que é PIX?", "p": "Entenda como funciona esse meio de pagamento instantâneo.", "s1": "História e vantagens", "s2": "Tempo de transferência"},
        2: {"title": "Cadastrar Chave", "p": "Aprenda a cadastrar seu CPF, e-mail ou telefone como chave.", "s1": "Acessar área PIX", "s2": "Escolher tipo de chave"},
        3: {"title": "Como Enviar PIX", "p": "Veja o passo a passo para transferir dinheiro usando a chave de alguém.", "s1": "Digitar a chave", "s2": "Confirmar valor"},
        4: {"title": "Como Receber PIX", "p": "Saiba como compartilhar sua chave e gerar QR Codes.", "s1": "Mostrar chave", "s2": "Gerar QR Code"},
        5: {"title": "Cuidados e Segurança", "p": "Dicas essenciais para não cair em golpes.", "s1": "Checar recebedor", "s2": "Desconfiar de urgência"},
    },
    'seguranca': {
        1: {"title": "Senhas Fortes", "p": "Aprenda a criar senhas seguras e fáceis de memorizar.", "s1": "Uso de números e letras", "s2": "Não repetir senhas"},
        2: {"title": "Cuidado com Links", "p": "Saiba por que você não deve clicar em links suspeitos.", "s1": "Identificar links falsos", "s2": "Checar o remetente"},
        3: {"title": "Golpes no WhatsApp", "p": "Como agir quando alguém pedir dinheiro pelo app.", "s1": "Ligar para a pessoa", "s2": "Não transferir na hora"},
        4: {"title": "Atualizações", "p": "A importância de manter seu celular e apps atualizados.", "s1": "Atualizar sistema", "s2": "Evitar falhas de segurança"},
        5: {"title": "Uso de Antivírus", "p": "Entenda se você precisa de um antivírus no celular.", "s1": "Verificar loja oficial", "s2": "Limpar o aparelho"},
        6: {"title": "Wi-Fi Público", "p": "Os riscos de usar a internet da praça ou aeroporto.", "s1": "Não usar app do banco", "s2": "Conexões inseguras"},
        7: {"title": "Autenticação Dupla", "p": "O que é o PIN do WhatsApp e por que ativá-lo.", "s1": "Criar o PIN", "s2": "Recuperação por email"},
        8: {"title": "Fui Hackeado?", "p": "O que fazer se o seu celular ou app for invadido.", "s1": "Avisar familiares", "s2": "Bloquear cartão"},
    },
    'compras': {
        1: {"title": "Lojas Seguras", "p": "Como saber se um site é confiável e não cair em sites falsos.", "s1": "Verificar cadeado", "s2": "Ler avaliações"},
        2: {"title": "Pesquisar Preços", "p": "Encontre o que você precisa e compare promoções e descontos.", "s1": "Usar o Google", "s2": "Identificar lojas"},
        3: {"title": "Pagamento Seguro", "p": "Formas de pagar sem colocar em risco os dados do seu cartão.", "s1": "Cartão Virtual", "s2": "Pagar com PIX"}
    },
    'banco': {
        1: {"title": "O que é um banco digital?", "p": "Entenda a diferença entre bancos tradicionais e digitais, e como eles funcionam.", "s1": "Sem agências físicas", "s2": "Taxas menores"},
        2: {"title": "Abrindo sua conta", "p": "O passo a passo para criar sua conta pelo celular, sem sair de casa.", "s1": "Tirar foto de documentos", "s2": "Fazer uma selfie (foto do rosto)"},
        3: {"title": "Acessando o aplicativo", "p": "Como fazer login com segurança usando sua senha, digital ou rosto.", "s1": "Digitar CPF", "s2": "Usar a digital"},
        4: {"title": "Verificando o Saldo", "p": "Aprenda onde olhar quanto dinheiro você tem disponível na conta.", "s1": "Tela inicial do app", "s2": "Ocultar o valor para segurança"},
        5: {"title": "Extrato", "p": "Veja como conferir tudo que entrou e saiu da sua conta no mês.", "s1": "Histórico de movimentações", "s2": "Baixar comprovantes"},
        6: {"title": "Pagamento de Boletos", "p": "Descubra como pagar contas de água e luz usando a câmera do celular.", "s1": "Ler código de barras", "s2": "Digitar os números"},
        7: {"title": "Transferências", "p": "Como enviar dinheiro para os seus contatos com segurança.", "s1": "Dados do recebedor", "s2": "Conferir antes de enviar"},
        8: {"title": "Cartão Virtual", "p": "Por que o cartão virtual é mais seguro para compras na internet.", "s1": "Gerar no aplicativo", "s2": "Código de segurança muda"}
    }
}

THEMES = {
    'celular': {
        'name': 'Curso Celular Básico',
        'primary': '#5a31f4',
        'dark': '#1a237e',
        'light': '#F0F4FF',
        'image': 'celular_thumbnail.png',
        'total': 4
    },
    'gov': {
        'name': 'Curso Gov.br',
        'primary': '#1351B4',
        'dark': '#0D47A1',
        'light': '#E3F2FD',
        'image': 'gov_thumbnail.png',
        'total': 3
    },
    'pix': {
        'name': 'Curso PIX',
        'primary': '#32BCAD',
        'dark': '#00695C',
        'light': '#E0F2F1',
        'image': 'pix_thumbnail.png',
        'total': 5
    },
    'seguranca': {
        'name': 'Curso Segurança Digital',
        'primary': '#F57C00',
        'dark': '#E65100',
        'light': '#FFF3E0',
        'image': 'seguranca_thumbnail.png',
        'total': 8
    },
    'compras': {
        'name': 'Compras Online',
        'primary': '#E91E63',
        'dark': '#C2185B',
        'light': '#FCE4EC',
        'image': 'seguranca_thumbnail.png',
        'total': 3
    },
    'banco': {
        'name': 'Banco Digital',
        'primary': '#1A368F',
        'dark': '#001C66',
        'light': '#E8F1FC',
        'image': 'celular_thumbnail.png',
        'total': 8
    }
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TecnoIdade - {course_name} - Aula {i}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --theme-primary: {primary_color};
            --theme-dark: {dark_color};
            --theme-light: {light_color};
            --btn-green: #388E3C;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }}
        body {{ background-color: #f5f5f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; overflow-x: hidden; }}
        
        .mobile-container {{
            width: 100%;
            max-width: 414px;
            min-height: 100vh;
            height: 100%;
            margin: 0 auto;
            background-color: #FFFFFF;
            position: relative;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            overflow-x: hidden;
        }}

        .header-top {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 25px 20px 10px 20px;
        }}

        .btn-back {{
            background-color: #E0E0E0;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #333;
            text-decoration: none;
        }}

        .header-center {{
            text-align: center;
            flex-grow: 1;
            padding: 0 10px;
        }}
        
        .header-center h1 {{
            color: var(--theme-primary);
            font-size: 20px;
            font-weight: 900;
        }}

        .sound-icon {{
            color: var(--theme-primary);
        }}

        .title-section {{
            text-align: center;
            padding: 5px 20px 15px 20px;
        }}

        .title-section .lesson-count {{
            font-size: 14px;
            font-weight: 800;
            color: #000;
            display: block;
            margin-bottom: 5px;
        }}

        .title-section .lesson-title {{
            font-size: 22px;
            font-weight: 900;
            color: var(--theme-dark);
        }}

        .video-wrapper {{
            padding: 0 20px;
            margin-bottom: 20px;
        }}

        .video-container {{
            width: 100%;
            border-radius: 20px;
            overflow: hidden;
            position: relative;
            background-color: #000;
            aspect-ratio: 4/3;
        }}

        .video-container img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.9;
        }}

        .play-overlay {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 60px;
            height: 60px;
            border: 2px solid rgba(255,255,255,0.8);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            background: rgba(0,0,0,0.4);
        }}

        .video-controls {{
            position: absolute;
            bottom: 15px;
            left: 15px;
            right: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
            color: white;
            font-size: 12px;
            font-weight: 700;
        }}

        .video-bar {{
            flex-grow: 1;
            height: 4px;
            background-color: rgba(255,255,255,0.4);
            border-radius: 2px;
            position: relative;
        }}

        .video-bar-fill {{
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 30%;
            background-color: #FFF;
            border-radius: 2px;
        }}

        .desc-text {{
            padding: 0 20px;
            font-size: 15px;
            font-weight: 600;
            color: #333;
            line-height: 1.5;
            margin-bottom: 20px;
            display: flex;
            align-items: flex-start;
            gap: 10px;
        }}

        .desc-icon {{
            color: var(--theme-primary);
            flex-shrink: 0;
            margin-top: 3px;
        }}

        .learning-card {{
            margin: 0 20px 25px 20px;
            background-color: var(--theme-light);
            border-radius: 15px;
            padding: 20px;
        }}

        .learning-card-title {{
            display: flex;
            align-items: center;
            gap: 10px;
            color: var(--theme-primary);
            font-size: 16px;
            font-weight: 900;
            margin-bottom: 15px;
        }}

        .check-list {{
            list-style: none;
        }}

        .check-list li {{
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 15px;
            font-weight: 700;
            color: #444;
            margin-bottom: 12px;
        }}

        .check-list li:last-child {{
            margin-bottom: 0;
        }}

        .check-icon {{
            color: var(--theme-primary);
            background-color: rgba(255,255,255,0.5);
            border-radius: 50%;
        }}

        .activities-title {{
            padding: 0 20px;
            color: var(--theme-primary);
            font-size: 16px;
            font-weight: 900;
            margin-bottom: 15px;
        }}

        .action-box {{
            margin: 0 20px 30px 20px;
            background-color: #E0E0E0;
            border-radius: 20px;
            padding: 15px 20px;
            display: flex;
            align-items: center;
            gap: 15px;
        }}

        .action-box-icon {{
            color: var(--theme-dark);
        }}

        .action-box-text h4 {{
            font-size: 15px;
            font-weight: 900;
            color: #000;
            margin-bottom: 3px;
        }}

        .action-box-text p {{
            font-size: 11px;
            font-weight: 700;
            color: #333;
        }}

        .btn-next {{
            margin: auto 20px 30px 20px;
            display: block;
            background-color: var(--btn-green);
            color: white;
            text-align: center;
            padding: 20px;
            border-radius: 30px;
            font-size: 22px;
            font-weight: 800;
            text-decoration: none;
            box-shadow: 0 4px 15px rgba(56, 142, 60, 0.4);
            transition: transform 0.2s;
        }}
        
        .btn-next:active {{
            transform: scale(0.95);
        }}
    </style>
</head>
<body>
    <div class="mobile-container">
        
        <div class="header-top">
            <a href="{{{{ url_for('aprender') }}}}" class="btn-back">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" width="20" height="20">
                    <polyline points="15 18 9 12 15 6"></polyline>
                </svg>
            </a>
            <div class="header-center">
                <h1>{course_name}</h1>
            </div>
            <div class="sound-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" width="24" height="24">
                    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                    <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
                    <path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path>
                </svg>
            </div>
        </div>

        <div class="title-section">
            <span class="lesson-count">Aula {i} de {total}</span>
            <h2 class="lesson-title">{title}</h2>
        </div>

        <div class="video-wrapper">
            <div class="video-container">
                <img src="{{{{ url_for('static', filename='images/{image_name}') }}}}" alt="Video thumbnail">
                <div class="play-overlay">
                    <svg viewBox="0 0 24 24" fill="currentColor" width="28" height="28" style="margin-left:4px;">
                        <polygon points="5 3 19 12 5 21 5 3"></polygon>
                    </svg>
                </div>
                <div class="video-controls">
                    <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                    <span>0:00/2:45</span>
                    <div class="video-bar">
                        <div class="video-bar-fill"></div>
                    </div>
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg>
                </div>
            </div>
        </div>

        <div class="desc-text">
            <div class="desc-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" width="22" height="22">
                    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                    <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
                </svg>
            </div>
            <p>Nesta aula: {p}</p>
        </div>

        <div class="learning-card">
            <div class="learning-card-title">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="20" height="20">
                    <path d="M9 18h6m-3-15a5.5 5.5 0 0 0-5.5 5.5c0 2.2 1.3 4 3 5V15a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-1.5c1.7-1 3-2.8 3-5A5.5 5.5 0 0 0 12 3Z"></path>
                </svg>
                <span>Você vai aprender:</span>
            </div>
            <ul class="check-list">
                <li>
                    <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" width="20" height="20" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10" stroke="none" fill="rgba(255,255,255,0.8)"></circle>
                        <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                    {s1}
                </li>
                <li>
                    <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" width="20" height="20" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10" stroke="none" fill="rgba(255,255,255,0.8)"></circle>
                        <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                    {s2}
                </li>
                <li>
                    <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" width="20" height="20" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10" stroke="none" fill="rgba(255,255,255,0.8)"></circle>
                        <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                    Colocando em prática
                </li>
            </ul>
        </div>

        <h3 class="activities-title">Atividades desta aula</h3>

        <div class="action-box">
            <div class="action-box-icon">
                <svg viewBox="0 0 24 24" fill="currentColor" width="32" height="32">
                    <polygon points="5 3 19 12 5 21 5 3"></polygon>
                </svg>
            </div>
            <div class="action-box-text">
                <h4>Assistir ao Vídeo</h4>
                <p>Assista ao vídeo completo<br>para continuar</p>
            </div>
        </div>

        <a href="{{{{ url_for('{next_route}') }}}}" class="btn-next">Próxima aula</a>

    </div>
</body>
</html>
"""

template_dir = r"c:\Users\mathe\Desktop\tecnoidade\templates"
static_img_dir = r"c:\Users\mathe\Desktop\tecnoidade\static\images"

for prefix, content_dict in DATA.items():
    theme = THEMES[prefix]
    
    for i, data in content_dict.items():
        filepath = os.path.join(template_dir, f"curso_{prefix}_aula{i}.html")
        
        next_route = f"curso_{prefix}_aula{i+1}" if i < theme['total'] else "curso_concluido"
        
        # Check if dynamic image exists
        dynamic_image_name = f"curso_{prefix}_aula{i}.png"
        dynamic_image_path = os.path.join(static_img_dir, dynamic_image_name)
        
        if os.path.exists(dynamic_image_path):
            image_to_use = dynamic_image_name
        else:
            image_to_use = theme['image']
            
        final_html = HTML_TEMPLATE.format(
            primary_color=theme['primary'],
            dark_color=theme['dark'],
            light_color=theme['light'],
            course_name=theme['name'],
            i=i,
            total=theme['total'],
            title=data['title'],
            image_name=image_to_use,
            p=data['p'],
            s1=data['s1'],
            s2=data['s2'],
            next_route=next_route
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_html)

print("Imagens individuais aplicadas com sucesso (fallback utilizado onde o limite da IA estourou)!")
