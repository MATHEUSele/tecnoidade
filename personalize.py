import os
import re

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
        3: {"title": "Principais Serviços", "p": "Veja como acessar seus documentos digitais, como CNH e carteira de vacinação.", "s1": "Buscar serviços", "s2": "Acessar documentos"},
    },
    'pix': {
        1: {"title": "O que é PIX?", "p": "Entenda como funciona esse meio de pagamento instantâneo.", "s1": "História e vantagens", "s2": "Tempo de transferência"},
        2: {"title": "Cadastrar Chave", "p": "Aprenda a cadastrar seu CPF, e-mail ou telefone como chave.", "s1": "Acessar área PIX", "s2": "Escolher tipo de chave"},
        3: {"title": "Como Enviar PIX", "p": "Veja o passo a passo para transferir dinheiro usando a chave de alguém.", "s1": "Digitar a chave", "s2": "Confirmar valor"},
        4: {"title": "Como Receber PIX", "p": "Saiba como compartilhar sua chave e gerar QR Codes.", "s1": "Mostrar chave", "s2": "Gerar QR Code"},
        5: {"title": "Cuidados e Segurança", "p": "Dicas essenciais para não cair em golpes.", "s1": "Checar nome do recebedor", "s2": "Desconfiar de urgência"},
    },
    'seguranca': {
        1: {"title": "Senhas Fortes", "p": "Aprenda a criar senhas seguras e fáceis de memorizar.", "s1": "Uso de números e letras", "s2": "Não repetir senhas"},
        2: {"title": "Cuidado com Links", "p": "Saiba por que você não deve clicar em links suspeitos.", "s1": "Identificar links falsos", "s2": "Checar o remetente"},
        3: {"title": "Golpes no WhatsApp", "p": "Como agir quando alguém pedir dinheiro em nome de um parente.", "s1": "Ligar para a pessoa", "s2": "Não transferir na hora"},
        4: {"title": "Atualizações", "p": "A importância de manter seu celular e aplicativos atualizados.", "s1": "Atualizar sistema", "s2": "Evitar falhas de segurança"},
        5: {"title": "Uso de Antivírus", "p": "Entenda se você precisa de um antivírus no celular.", "s1": "Verificar loja oficial", "s2": "Limpar o aparelho"},
        6: {"title": "Wi-Fi Público", "p": "Os riscos de usar a internet da praça, padaria ou aeroporto.", "s1": "Não usar app do banco", "s2": "Conexões inseguras"},
        7: {"title": "Autenticação em 2 Fatores", "p": "O que é o PIN do WhatsApp e por que ativá-lo.", "s1": "Criar o PIN", "s2": "Recuperação por email"},
        8: {"title": "Fui Hackeado?", "p": "O que fazer se o seu celular ou WhatsApp forem invadidos.", "s1": "Avisar familiares", "s2": "Bloquear cartão"},
    }
}

template_dir = r"c:\Users\mathe\Desktop\tecnoidade\templates"

for prefix, content_dict in DATA.items():
    for i, data in content_dict.items():
        filepath = os.path.join(template_dir, f"curso_{prefix}_aula{i}.html")
        if not os.path.exists(filepath):
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Update h2
        html = re.sub(r'<h2>.*?</h2>', f'<h2>Aula {i}: {data["title"]}</h2>', html, count=1)
        
        # Update paragraph starting with "Nesta aula"
        html = re.sub(r'<p>Nesta aula.*?</p>', f'<p>Nesta aula: {data["p"]} Assista o vídeo para continuar.</p>', html)
        
        # Update ul
        new_ul = f"""<ul style="margin-left: 20px; margin-bottom: 30px; color: #555; font-size: 14px;">
                <li style="margin-bottom: 5px;">Passo 1: {data['s1']}</li>
                <li style="margin-bottom: 5px;">Passo 2: {data['s2']}</li>
                <li style="margin-bottom: 5px;">Passo 3: Colocando em prática</li>
            </ul>"""
        html = re.sub(r'<ul.*?>.*?</ul>', new_ul, html, flags=re.DOTALL)
        
        btn_match = re.search(r'<a href="([^"]+)" class="btn-primary"[^>]*>.*?</a>', html)
        if btn_match:
            btn_html = btn_match.group(0)
            html = html.replace(btn_html, '')
            
            # Remove inline styles from button and add a class or inline style that forces top margin
            new_btn_html = btn_html
            if 'style=' in new_btn_html:
                new_btn_html = re.sub(r'style="[^"]+"', 'style="display: block; width: 100%; padding: 15px; background: #1A368F; color: white; text-align: center; border-radius: 15px; text-decoration: none; font-weight: bold; margin-top: 30px;"', new_btn_html)
            else:
                new_btn_html = new_btn_html.replace('class="btn-primary"', 'class="btn-primary" style="margin-top: 30px;"')
                
            html = html.replace('</ul>', f'</ul>\n            {new_btn_html}')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

print("Telas personalizadas e botão reajustado com sucesso!")
