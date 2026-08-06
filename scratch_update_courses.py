import os
import re

TEMPLATES_DIR = r"c:\Users\mathe\Desktop\tecnoidade\templates"

def add_start_course_button():
    course_map = {
        "curso_banco_digital.html": "curso_banco_aula1",
        "curso_pix.html": "curso_pix_aula1",
        "curso_seguranca_digital.html": "curso_seguranca_aula1",
        "curso_whatsapp.html": "curso_whatsapp_conhecendo",
        "curso_celular_basico.html": "curso_concluido",
        "curso_gov.html": "curso_concluido",
        "curso_compras_online.html": "curso_concluido",
    }
    
    for file, start_route in course_map.items():
        filepath = os.path.join(TEMPLATES_DIR, file)
        if not os.path.exists(filepath): continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "Começar Agora" not in content and "Começar Curso" not in content:
            # We want to add the button just before the closing </div> of content-layer
            # But the easiest way is to add it after "bottom-actions"
            button_html = f'\n            <a href="{{{{ url_for(\'{start_route}\') }}}}" style="display:block; width:100%; padding:15px; background:#4A56E2; color:white; text-align:center; border-radius:15px; font-weight:bold; text-decoration:none; margin-top:20px; font-size: 18px;">Começar Agora</a>\n'
            
            # Find the last </div> before </body>
            # Or just replace </body> with the button + </div> + </body> ? No, it has to be inside mobile-container and content-layer
            
            if '<div class="bottom-actions">' in content:
                # Add after the end of bottom-actions
                # Wait, bottom actions closes with </div>.
                # Let's insert before </div>\n    </div>\n</body>
                content = content.replace("</div>\n    </div>\n</body>", button_html + "        </div>\n    </div>\n</body>")
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Added Começar Agora to {file}")

def link_lessons():
    # Banco
    for i in range(1, 9):
        filepath = os.path.join(TEMPLATES_DIR, f"curso_banco_aula{i}.html")
        if not os.path.exists(filepath): continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        next_route = f"curso_banco_aula{i+1}" if i < 8 else "curso_concluido"
        # If there's already a next button, replace its route
        content = re.sub(r'href="\{\{ url_for\([^)]+\) \}\}" class="btn-primary"([^>]*)>(Próxima Aula|Começar)</a>', 
                         rf'href="{{{{ url_for(\'{next_route}\') }}}}" class="btn-primary"\1>Próxima Aula</a>', content)
        # If no button at all, add one
        if 'class="btn-primary"' not in content:
            content = content.replace('</div>\n</body>', f'    <a href="{{{{ url_for(\'{next_route}\') }}}}" class="btn-primary" style="display:block; width:100%; padding:15px; background:#4A56E2; color:white; text-align:center; border-radius:15px; font-weight:bold; text-decoration:none; margin-top:20px;">Próxima Aula</a>\n    </div>\n</body>')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    # Pix
    for i in range(1, 6):
        filepath = os.path.join(TEMPLATES_DIR, f"curso_pix_aula{i}.html")
        if not os.path.exists(filepath): continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        next_route = f"curso_pix_aula{i+1}" if i < 5 else "curso_concluido"
        if 'class="btn-primary"' not in content and 'Próxima Aula' not in content:
            content = content.replace('</div>\n</body>', f'    <a href="{{{{ url_for(\'{next_route}\') }}}}" class="btn-primary" style="display:block; width:100%; padding:15px; background:#4A56E2; color:white; text-align:center; border-radius:15px; font-weight:bold; text-decoration:none; margin-top:20px;">Próxima Aula</a>\n    </div>\n</body>')
        else:
            content = re.sub(r'href="\{\{ url_for\([^)]+\) \}\}" class="btn-primary"([^>]*)>(Próxima Aula|Começar)</a>', 
                             rf'href="{{{{ url_for(\'{next_route}\') }}}}" class="btn-primary"\1>Próxima Aula</a>', content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    # Seguranca
    for i in range(1, 9):
        filepath = os.path.join(TEMPLATES_DIR, f"curso_seguranca_aula{i}.html")
        if not os.path.exists(filepath): continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        next_route = f"curso_seguranca_aula{i+1}" if i < 8 else "curso_concluido"
        if 'class="btn-primary"' not in content and 'Próxima Aula' not in content:
            content = content.replace('</div>\n</body>', f'    <a href="{{{{ url_for(\'{next_route}\') }}}}" class="btn-primary" style="display:block; width:100%; padding:15px; background:#4A56E2; color:white; text-align:center; border-radius:15px; font-weight:bold; text-decoration:none; margin-top:20px;">Próxima Aula</a>\n    </div>\n</body>')
        else:
            content = re.sub(r'href="\{\{ url_for\([^)]+\) \}\}" class="btn-primary"([^>]*)>(Próxima Aula|Começar)</a>', 
                             rf'href="{{{{ url_for(\'{next_route}\') }}}}" class="btn-primary"\1>Próxima Aula</a>', content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

def fix_comecar_agora():
    # home.html is already fixed. Let's check login_sucesso.html
    filepath = os.path.join(TEMPLATES_DIR, "login_sucesso.html")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        content = re.sub(r'href="[^"]*" class="btn-primary">\s*Começar', r'href="{{ url_for(\'aprender\') }}" class="btn-primary">\n                Começar', content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    # tela_inicial.html
    filepath = os.path.join(TEMPLATES_DIR, "tela_inicial.html")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        content = re.sub(r'href="[^"]*" class="btn-start"', r'href="{{ url_for(\'aprender\') }}" class="btn-start"', content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    # tela1.html
    filepath = os.path.join(TEMPLATES_DIR, "tela1.html")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        content = re.sub(r'href="[^"]*" class="btn-start"', r'href="{{ url_for(\'aprender\') }}" class="btn-start"', content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

add_start_course_button()
link_lessons()
fix_comecar_agora()
print("All tasks completed.")
