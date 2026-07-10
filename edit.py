import os
import re

files = [
    'index.html',
    'empresa.html',
    'servicios.html',
    'productos.html',
    'novedades.html',
    'trabaja-con-nosotros.html',
    'contacto.html',
    'cobertura-nacional.html'
]

image_map = {
    'empresa.html': 'hero_empresa.png',
    'servicios.html': 'hero_servicios.png',
    'productos.html': 'hero_productos.png',
    'novedades.html': 'hero_novedades.png',
    'trabaja-con-nosotros.html': 'hero_trabaja.png',
    'contacto.html': 'hero_contacto.png',
    'cobertura-nacional.html': 'agro_bg.png' 
}

for fname in files:
    if not os.path.exists(fname):
        continue
        
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Remove from main menu
    content = re.sub(r'<li><a href="trabaja-con-nosotros\.html" class="nav-link[^"]*">Trabajá con nosotros</a></li>\s*', '', content)
    
    # 3. Inner Page Header updates
    if fname != 'index.html':
        img = image_map.get(fname, 'agro_bg.png')
        
        # Replace the section style
        def replace_header(m):
            style = m.group(1)
            style = re.sub(r'padding:\s*140px\s+0\s+60px', 'padding: 110px 0 40px', style)
            style = re.sub(r'rgba\(39,\s*53,\s*22,\s*0\.85\)', 'rgba(39, 53, 22, 0.65)', style)
            style = re.sub(r'rgba\(15,\s*17,\s*16,\s*0\.95\)', 'rgba(15, 17, 16, 0.75)', style)
            style = re.sub(r'url\([^)]+\)', f"url('assets/{img}')", style)
            return f'<section class="section" style="{style}">'
            
        content = re.sub(r'<section class="section" style="([^"]+)">', replace_header, content, count=1)
        
        # Replace the h1 style font-size to be slightly smaller
        def replace_h1(m):
            style = m.group(1)
            if 'font-size' not in style:
                style += ' font-size: 2.2rem;'
            else:
                style = re.sub(r'font-size:\s*[^;]+;', 'font-size: 2.2rem;', style)
            return f'<h1 style="{style}">'
            
        # We only want to replace the first h1 which is in the header
        content = re.sub(r'<h1 style="([^"]+)">', replace_h1, content, count=1)
        
    # 4. Add Trabaja con nosotros button to contacto.html
    if fname == 'contacto.html':
        new_card = """
                    <!-- Card 5: Trabaja -->
                    <a href="trabaja-con-nosotros.html" class="contact-info-card" style="background-color: rgba(39, 53, 22, 0.05); border-color: rgba(39, 53, 22, 0.2);">
                        <div class="contact-info-icon" style="color: var(--color-primary-light); background-color: rgba(39, 53, 22, 0.1);">
                            <i class="fas fa-user-tie"></i>
                        </div>
                        <div>
                            <h3 class="contact-info-title">Trabajá con nosotros</h3>
                            <p class="contact-info-text">Unite a nuestro equipo</p>
                            <p style="font-size:0.75rem; color:var(--color-primary-light); font-weight:700; margin-top:2px;">Ver oportunidades &rarr;</p>
                        </div>
                    </a>
                </div>
"""
        content = content.replace("                </div>\n\n                <!-- Right: Contact Form -->", new_card + "\n                <!-- Right: Contact Form -->")

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
