import os
import json
with open('data/db.json') as f:
    db = json.load(f)
chars = list(os.listdir('data/imgs'))
chars.sort()
c_out_lines = ['//AUTO-GENERATED; DO NOT EDIT']
for char in chars:
    with open(f'data/imgs/{char}') as f:
        lines = [ [ i for i in line.strip() ] for line in f.readlines() ]

    c_out_lines.append(f'unsigned char ch{char}[5] = {{')
    for i in range(5):
        c_out_lines.append([])
        for line in lines:
            c_out_lines[-1].append(str(line[i]))
        c_out_lines[-1] = f'''  0b{''.join(c_out_lines[-1])},'''
    c_out_lines[-1] = c_out_lines[-1].replace(',', '')
    c_out_lines.append('};')

c_out_lines.append('unsigned char* getChat(char character) {')
c_out_lines.append('  switch (character) {')
for char in chars:
    if char == 'error':
        continue
    try:
        c_out_lines.append(f'''    case '{db[char]}':''')
    except KeyError:
        c_out_lines.append(f'''    case '{char}':''')
    c_out_lines.append(f'      return ch{char};')
c_out_lines.append('    default:')
c_out_lines.append('      return cherror;')
c_out_lines.append('  }')
c_out_lines.append('}')

with open('ogfont.c', 'w+') as f:
    for c_out_line in c_out_lines:
        f.write(f'{c_out_line}\n')
