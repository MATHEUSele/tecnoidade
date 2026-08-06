import os

TEMPLATES_DIR = r"c:\Users\mathe\Desktop\tecnoidade\templates"

for filename in os.listdir(TEMPLATES_DIR):
    if not filename.endswith(".html"): continue
    filepath = os.path.join(TEMPLATES_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "\\'" in content:
        content = content.replace("\\'", "'")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed quotes in {filename}")
