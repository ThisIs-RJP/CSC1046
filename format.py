### Written by RJ Paraiso prior to this project

import re
import glob

def format(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    rules = re.findall(r'([^{]+)\{([^}]+)\}', content)
    formatted_rules = []
    
    for selector, properties in rules:
        props = [prop.strip() for prop in properties.split(';') if prop.strip()]
        formatted_props = []
        
        max_prop_length = max(len(prop.split(':')[0].strip()) if ':' in prop else 0 for prop in props)
        
        for prop in props:
            if ':' in prop:
                name, value = prop.split(':', 1)
                name        = name.strip()
                value       = value.strip()
                padding     = ' ' * (max_prop_length - len(name))
                
                formatted_props.append(f'    {name}:{padding} {value};')
        
        formatted_rule = f'{selector.strip()} {{\n' + '\n'.join(formatted_props) + '\n}'
        formatted_rules.append(formatted_rule)
    
    with open(file_path, 'w') as f:
        f.write('\n\n'.join(formatted_rules))

css_files = glob.glob('website/chessProject/chessApp/static/css/*.css')

for css_file in css_files:
    format(css_file)
