import os
import re
import glob
import shutil

# Copy the latest generated images
brain_dir = "/Users/Santiago_1/.gemini/antigravity-ide/brain/dc47b8f2-af10-4601-8523-8d30ea9bf289/"
assets_dir = "/Users/Santiago_1/Documents/GitHub/MAC-WEB/assets/"

for prefix in ["hero_novedades", "hero_trabaja", "hero_contacto"]:
    files = glob.glob(os.path.join(brain_dir, prefix + "_*.png"))
    if files:
        # Get the latest generated image
        latest_file = max(files, key=os.path.getmtime)
        dest = os.path.join(assets_dir, prefix + ".png")
        shutil.copy2(latest_file, dest)

files = [
    'empresa.html',
    'servicios.html',
    'productos.html',
    'novedades.html',
    'trabaja-con-nosotros.html',
    'contacto.html',
    'cobertura-nacional.html'
]

for fname in files:
    if not os.path.exists(fname):
        continue
        
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the section style padding from whatever it is (e.g. 110px 0 40px or 140px 0 60px) to 180px 0 100px
    def replace_padding(m):
        style = m.group(1)
        style = re.sub(r'padding:\s*\d+px\s+\d+px\s+\d+px', 'padding: 180px 0 100px', style) # if it had 3 values
        style = re.sub(r'padding:\s*\d+px\s+\d+\s+\d+px', 'padding: 180px 0 100px', style) # if it had 0 for right/left
        return f'<section class="section" style="{style}">'
        
    content = re.sub(r'<section class="section" style="([^"]+)">', replace_padding, content, count=1)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
