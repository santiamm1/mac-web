import os
import re

dir_path = '/Users/Santiago_1/Documents/GitHub/MAC-WEB'

target = r'<span id="logo-fallback" style="display:none; font-family:\'Outfit\',sans-serif; font-weight:800; font-size:1.4rem; color:var\(--color-primary\);"><span style="color:var\(--color-accent-yellow\)">M</span>\s*</a>'

updated_count = 0
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine path to assets
            if os.path.basename(root) == 'productos':
                asset_path = '../assets/logo.png'
            else:
                asset_path = 'assets/logo.png'
                
            replacement = f'''<img src="{asset_path}" alt="Miguel Cordini Logo" class="logo-img" onerror="this.style.display='none'; document.getElementById('logo-fallback').style.display='block';">
                <span id="logo-fallback" style="display:none; font-family:'Outfit',sans-serif; font-weight:800; font-size:1.4rem; color:var(--color-primary);"><span style="color:var(--color-accent-yellow)">M</span>IGUEL <span style="color:var(--color-accent-yellow)">C</span>ORDINI</span>
            </a>'''
            
            new_content = re.sub(target, replacement, content)
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file_path}")
                updated_count += 1

print(f"Total files updated: {updated_count}")
