import os
import re

TEMPLATES_DIR = r"c:\Users\mathe\Desktop\tecnoidade\templates"

def get_video_block(image_filename, primary_color="#1A368F"):
    return f"""            <div class="video-container" style="width: 100%; border-radius: 15px; overflow: hidden; position: relative; margin-bottom: 15px; background-color: #000; aspect-ratio: 16/9;">
                <img src="{{{{ url_for('static', filename='images/{image_filename}') }}}}" alt="Video thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8;">
                <div class="play-overlay" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 50px; height: 50px; background-color: rgba(0,0,0,0.6); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white;">
                    <svg viewBox="0 0 24 24" style="width: 24px; height: 24px; fill: currentColor; margin-left: 3px;">
                        <polygon points="5 3 19 12 5 21 5 3"></polygon>
                    </svg>
                </div>
                <div class="video-controls" style="position: absolute; bottom: 10px; left: 10px; right: 10px; display: flex; align-items: center; gap: 10px; color: white; font-size: 10px; font-weight: 700;">
                    <svg viewBox="0 0 24 24" fill="currentColor" width="12" height="12"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                    <span>0:00/2:45</span>
                    <div class="video-bar" style="flex-grow: 1; height: 4px; background-color: rgba(255,255,255,0.4); border-radius: 2px; position: relative;">
                        <div class="video-bar-fill" style="position: absolute; left: 0; top: 0; height: 100%; width: 30%; background-color: {primary_color}; border-radius: 2px;"></div>
                    </div>
                </div>
            </div>"""

def replace_placeholders():
    # Pix
    for i in range(1, 6):
        filepath = os.path.join(TEMPLATES_DIR, f"curso_pix_aula{i}.html")
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            block = get_video_block("pix_thumbnail.png", "#1A368F")
            content = content.replace('<div class="video-placeholder">Vídeo / Simulador da Aula</div>', block)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

    # Seguranca
    for i in range(1, 9):
        filepath = os.path.join(TEMPLATES_DIR, f"curso_seguranca_aula{i}.html")
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            block = get_video_block("seguranca_thumbnail.png", "#1A368F")
            content = content.replace('<div class="video-placeholder">Vídeo / Simulador da Aula</div>', block)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

def create_missing_screens():
    # We use curso_pix_aula1.html as a base template for these simple screens
    base_filepath = os.path.join(TEMPLATES_DIR, "curso_pix_aula1.html")
    with open(base_filepath, "r", encoding="utf-8") as f:
        base_content = f.read()
        
    # Celular
    for i in range(1, 5):
        filepath = os.path.join(TEMPLATES_DIR, f"curso_celular_aula{i}.html")
        content = base_content.replace("Curso Pix", "Meu Celular").replace("O que é PIX?", f"Meu Celular - Aula {i}")
        content = content.replace("Nesta aula você aprenderá sobre O que é PIX?", "Nesta aula você aprenderá funções essenciais do seu celular")
        # Replace the video block (which is already replaced in base if we run replace_placeholders first)
        # Actually base_content might have the pix_thumbnail. Let's force replace it with celular_thumbnail
        content = re.sub(r'<div class="video-container".*?</div>\s*</div>\s*</div>', get_video_block("celular_thumbnail.png", "#4A56E2"), content, flags=re.DOTALL)
        
        # We need to make sure the next route is correct
        next_route = f"curso_celular_aula{i+1}" if i < 4 else "curso_concluido"
        # Find the btn-primary href and replace it
        content = re.sub(r'href="\{\{ url_for\([^)]+\) \}\}" class="btn-primary"', f'href="{{{{ url_for(\'{next_route}\') }}}}" class="btn-primary"', content)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    # Gov
    for i in range(1, 4):
        filepath = os.path.join(TEMPLATES_DIR, f"curso_gov_aula{i}.html")
        content = base_content.replace("Curso Pix", "Gov").replace("O que é PIX?", f"Gov - Aula {i}")
        content = content.replace("Nesta aula você aprenderá sobre O que é PIX?", "Nesta aula você aprenderá sobre o portal Gov")
        content = re.sub(r'<div class="video-container".*?</div>\s*</div>\s*</div>', get_video_block("gov_thumbnail.png", "#4A56E2"), content, flags=re.DOTALL)
        
        next_route = f"curso_gov_aula{i+1}" if i < 3 else "curso_concluido"
        content = re.sub(r'href="\{\{ url_for\([^)]+\) \}\}" class="btn-primary"', f'href="{{{{ url_for(\'{next_route}\') }}}}" class="btn-primary"', content)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)


def add_routes_to_app():
    app_path = r"c:\Users\mathe\Desktop\tecnoidade\app.py"
    with open(app_path, "r", encoding="utf-8") as f:
        app_content = f.read()

    new_routes = []
    for i in range(1, 5):
        if f"curso_celular_aula{i}" not in app_content:
            new_routes.append(f"@app.route('/curso_celular_aula{i}')\ndef curso_celular_aula{i}():\n    return render_template('curso_celular_aula{i}.html')\n")
            
    for i in range(1, 4):
        if f"curso_gov_aula{i}" not in app_content:
            new_routes.append(f"@app.route('/curso_gov_aula{i}')\ndef curso_gov_aula{i}():\n    return render_template('curso_gov_aula{i}.html')\n")

    if new_routes:
        # Find the line before `if __name__ == '__main__':`
        insert_idx = app_content.find("if __name__ == '__main__':")
        if insert_idx != -1:
            updated_content = app_content[:insert_idx] + "\n".join(new_routes) + "\n" + app_content[insert_idx:]
            with open(app_path, "w", encoding="utf-8") as f:
                f.write(updated_content)

replace_placeholders()
create_missing_screens()
add_routes_to_app()
print("All screens updated and routes added.")
