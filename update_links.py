import os
import re

template_dir = r"c:\Users\mathe\Desktop\tecnoidade\templates"

# Regex to match href="some_page.html"
# But we need to make sure we don't break things that are already {{ url_for(...) }}
pattern = re.compile(r'href="([^"]+)\.html"')

for filename in os.listdir(template_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(template_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace href="page.html" with href="{{ url_for('page') }}"
        new_content = pattern.sub(lambda m: f'href="{{{{ url_for(\'{m.group(1)}\') }}}}"', content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
print("Done")
