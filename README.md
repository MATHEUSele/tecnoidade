# TecnoIdade

Um aplicativo web desenvolvido em Flask voltado para a inclusão digital, com foco no público idoso e seus cuidadores/familiares. 

## 🚀 Link de Produção

O projeto está hospedado e pode ser acessado diretamente pelo Render através do link abaixo:

🔗 **[Acessar TecnoIdade no Render](https://tecnoidade.onrender.com)**

---

## 💻 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o projeto na sua máquina para testes ou desenvolvimento:

### Pré-requisitos
- Ter o [Python](https://www.python.org/downloads/) (versão 3.x) instalado na sua máquina.

### Passo a Passo

1. **Clone ou acesse a pasta do projeto:**
   Navegue até o diretório raiz do projeto no seu terminal.

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   
   # Para ativar no Windows:
   venv\Scripts\activate
   
   # Para ativar no Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   Com o terminal aberto na pasta do projeto, instale as bibliotecas necessárias listadas no `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   Inicie o servidor local do Flask executando:
   ```bash
   python app.py
   ```
   *Alternativamente, você pode usar o comando `flask run` se o `app.py` estiver configurado corretamente.*

5. **Acesse no navegador:**
   Abra o seu navegador de preferência e acesse o endereço local:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🛠️ Tecnologias Utilizadas
- **Python / Flask** (Backend)
- **HTML / CSS / JavaScript** (Frontend - Templates)
- **Gunicorn** (Servidor WSGI para produção no Render)
