import pytest
import sys
import os

# Adiciona o diretório raiz ao path para poder importar o app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    # Configura o aplicativo Flask para o modo de testes
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_frontend_subiu_login(client):
    """
    Testa se a página de login está carregando e respondendo com status 200 (OK),
    o que garante que o servidor front-end Flask subiu sem estourar erros graves.
    """
    resposta = client.get('/login')
    
    # 200 significa "OK - Sucesso"
    assert resposta.status_code == 200
    
def test_frontend_subiu_termos(client):
    """
    Verifica outra rota importante (Termos de Uso) para garantir que as rotas estão funcionando.
    """
    resposta = client.get('/termos_uso')
    assert resposta.status_code == 200
