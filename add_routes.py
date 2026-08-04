import os
import re

app_path = r"c:\Users\mathe\Desktop\tecnoidade\app.py"
template_dir = r"c:\Users\mathe\Desktop\tecnoidade\templates"

with open(app_path, 'r', encoding='utf-8') as f:
    app_content = f.read()

# Find existing routes
# matches @app.route('/<route_name>') or similar
existing_routes = set()
for match in re.finditer(r"def\s+([a-zA-Z0-9_]+)\s*\(", app_content):
    existing_routes.add(match.group(1))

# Special mappings that don't match the template name
existing_routes.add('boas_vindas') # uses tela1.html
existing_routes.add('escolha_perfil') # uses tela2.html
existing_routes.add('entrar') # uses entrar.html
existing_routes.add('cadastro') # uses cadastro.html
existing_routes.add('preferencias') # uses tela3.html

templates = [f[:-5] for f in os.listdir(template_dir) if f.endswith('.html')]

missing_routes = []
for t in templates:
    # If the template basename isn't an existing function in app.py
    if t not in existing_routes and t not in ['tela1', 'tela2', 'tela3', 'entrar', 'cadastro', 'home', 'aprender', 'buscar', 'progresso', 'curso_whatsapp', 'curso_whatsapp_conhecendo', 'curso_whatsapp_mensagem', 'curso_whatsapp_fotos', 'curso_whatsapp_video', 'curso_pix', 'curso_compras_online', 'curso_banco_digital', 'curso_seguranca_digital', 'curso_celular_basico', 'curso_gov', 'curso_concluido', 'familiar_vincular', 'familiar_dashboard', 'familiar_lista', 'familiar_perfil', 'familiar_editar_perfil', 'familiar_configuracoes', 'familiar_excluir_conta', 'tela_inicial']:
        missing_routes.append(t)

if missing_routes:
    # Insert before if __name__ == '__main__':
    insertion_point = app_content.find("if __name__ == '__main__':")
    
    new_routes_str = "\n# --- Rotas Dinamicas Adicionadas Automaticamente ---\n"
    for r in missing_routes:
        new_routes_str += f"@app.route('/{r}')\ndef {r}():\n    return render_template('{r}.html')\n\n"
    
    new_app_content = app_content[:insertion_point] + new_routes_str + app_content[insertion_point:]
    
    with open(app_path, 'w', encoding='utf-8') as f:
        f.write(new_app_content)
    
    print(f"Added {len(missing_routes)} missing routes.")
else:
    print("No missing routes.")
