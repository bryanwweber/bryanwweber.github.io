"""
Convert pubs.md to non-Kramdown format
"""
import re

with open('bib/pubs.md') as md_f:
    md = md_f.readlines()

span_class = re.compile('<span>([\w\s\d\-/\*\.,:\[\]\(\)~{}?=&#]*)</span>({:\.papertitle}|{:\.authors}|{:\.journal}|{:\.doi}|{:\.comment})')

output = []
year = False
paper = False
for l in md:
    if '{:.year}' in l:
        year = True
        continue
    elif '{:.paper}' in l:
        paper = True
        continue

    if year:
        output.append('<h3 class="pub-year">{}</h3>\n'.format(l.strip('# \n')))
        year = False
        continue

    if paper and l == '\n':
        output.append('{: .paper}\n')
        paper = False
        continue

    a = span_class.search(l)
    if a is not None:
        cl = a.group(2).strip('{}:.')
        if cl == 'papertitle':
            clss = '|p|'
        elif cl == 'authors':
            clss = '|u|'
        elif cl == 'journal':
            clss = '|j|'
        elif cl == 'doi':
            clss = '|d|'
        elif cl == 'comment':
            clss = '|c|'
        output.append('{clss}{item}{clss}  '.format(item=a.group(1), clss=clss))
        continue

    if l == '---\n' or l == '\n':
        continue
    else:
        output.append('<h2>{}</h2>\n'.format(l.strip()))

output.append('{: .paper}')

with open('bib/pubs-converted.md', 'w') as md_f:
    md_f.write('\n'.join(output))
