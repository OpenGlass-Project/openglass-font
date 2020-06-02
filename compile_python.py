import os
import json
with open('data/db.json') as f:
    db = json.load(f)
chars = list(os.listdir('data/imgs'))
chars.sort()
py_out_lines = [
        '#AUTO-GENERATED; DO NOT EDIT',
        '_chars = {',
]
for char in chars:
    with open(f'data/imgs/{char}') as f:
        lines = [ [ i for i in line.strip() ] for line in f.readlines() ]

    try:
        py_out_lines.append(f'''    '{db[char]}': [''')
    except KeyError:
        py_out_lines.append(f'''    '{char}': [''')
    for line in lines:
        py_out_lines.append(f'''        {line},''')
    py_out_lines.append(f'''    ],''')

py_out_lines.append('}')
py_out_lines.append('def get_char(character):')
py_out_lines.append('    try:')
py_out_lines.append('        return _chars[character]')
py_out_lines.append('    except KeyError:')
py_out_lines.append('        return _chars[\'error\']')

try:
    os.mkdir('ogfont')
except FileExistsError:
    pass

with open('ogfont/__init__.py', 'w+') as f:
    for py_out_line in py_out_lines:
        f.write(f'{py_out_line}\n')
