import os
import re

template_dir = r"c:\Users\mathe\Desktop\tecnoidade\templates"

courses = {
    'curso_pix_aula': 5,
    'curso_banco_aula': 8,
    'curso_seguranca_aula': 8
}

pattern = re.compile(r'href="\{\{\s*url_for\(\'curso_concluido\'\)\s*\}\}"')

for prefix, max_lessons in courses.items():
    for i in range(1, max_lessons + 1):
        filename = f"{prefix}{i}.html"
        filepath = os.path.join(template_dir, filename)
        
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Determine the target endpoint for the "Próxima Aula" button
        if i < max_lessons:
            next_route = f"{prefix}{i+1}"
        else:
            next_route = "curso_concluido"
            
        # Replace the url_for('curso_concluido') with the correct one
        # Note: the original HTML might have had "curso_concluido.html" which was replaced by update_links.py to url_for('curso_concluido')
        new_content = pattern.sub(f'href="{{{{ url_for(\'{next_route}\') }}}}"', content)
        
        # In case the update_links.py didn't touch it because it was not exactly "curso_concluido.html"
        # We also replace any literal href="curso_concluido.html"
        new_content = re.sub(r'href="curso_concluido\.html"', f'href="{{{{ url_for(\'{next_route}\') }}}}"', new_content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename} to point to {next_route}")
        else:
            print(f"No changes for {filename}")

print("Done linking courses")
