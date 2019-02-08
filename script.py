tex_file = open(FILES['select'])
config = exec(open('config.ini').read())
tex_file = tex_file.readlines()

# delete preamble

for i in range(len(tex_file)):
    if tex_file[0].find('\\begin{document}') != -1:
        break
    del tex_file[0]

size = len(tex_file)

# Changing mandatory elements

for i in range(size):
    while(tex_file[i].find('<') != -1 or tex_file[i].find('>') != -1):
        tex_file[i] = tex_file[i].replace('<', "&lt")
        tex_file[i] = tex_file[i].replace('>', "&gt")

# replace math_delimiters

need_to_replace = CENTERED_MATH_DELIMITERS.split(',')
flag = 0
for x in need_to_replace:
    x = x.strip()
    x = x.split(';')
    for i in range(size):
        while(x[0] in tex_file[i] or x[1] in tex_file[i]):
            if flag == 0:
                tex_file[i] = tex_file[i].replace(x[0],'\\[',1)
                flag = 1
            else:
                tex_file[i] = tex_file[i].replace(x[1],'\\]',1)
                flag = 0


need_to_replace = INLINE_MATH_DELIMITERS.split(',')
flag = 0
for x in need_to_replace:
    x = x.strip()
    x = x.split(';')
    for i in range(size):
        while(x[0] in tex_file[i] or x[1] in tex_file[i]):
            if flag == 0:
                tex_file[i] = tex_file[i].replace(x[0],'\\(',1)
                flag = 1
            else:
                tex_file[i] = tex_file[i].replace(x[1],'\\)',1)
                flag = 0

# replace environments

for name, default_replace_text in ENVIRONMENT_TYPES.items():
    environments = ENVIRONMENT_NAMES[name].split(',')

    for environment in environments:
        num = 1
        environment = environment.strip()
        replace_text = default_replace_text[:]
        replace_text_size = len(replace_text)
        for i in range(replace_text_size):
            line = replace_text[i].replace('Placeholder',environment.lower().capitalize())
            line = line.replace('PLACEHOLDER',environment.upper())
            line = line.replace('placeholder',environment.lower())
            replace_text[i] = line
        for i in range(size):
            line = tex_file[i]
            while line.find('\\begin{'+environment+'}[') != -1:
                replace = replace_text[2]
                label = re.search('\\\\begin\{'+environment+'\}'+'\[(.*)\]', line).group(1)
                replace = replace.replace('LABEL', label)
                replace = replace.replace('NUM', str(num))
                line = line.replace('\\begin{'+environment+'}['+label+']', replace)
                num += 1
            if replace_text_size == 1:
                line = line.replace('\\end{'+environment+'}', '')
            else:
                line = line.replace('\\end{'+environment+'}', replace_text[1])
            while line.find('\\begin{'+environment+'}') != -1:
                replace = replace_text[0]
                replace = replace.replace('NUM', str(num))
                line = line.replace('\\begin{'+environment+'}', replace)
                num += 1
            tex_file[i] = line

# replace footnotes

num = 1
footnotes = []
for i in range(size):
    line = tex_file[i]
    while(line.find('\\footnotemark') != -1):
        line = line.replace('\\footnotemark','')
        for j in range(i,size):
            if (tex_file[j].find('\\footnotetext{') != -1):
                line_two = tex_file[j]
                footnote= re.search('\\\\footnotetext\{(.*)\}', line_two).group(1)
                footnotes.append('<li id="fn:'+str(num)+'">'+footnote+'</li>\n')
                line_two = line_two.replace('\\footnotetext{'+footnote+'}', '<a href="#fn:'+str(num)+'" id="fnref:'+str(num)+'"><sup>'+str(num)+'</sup></a>')
                tex_file[j] = line_two
                num += 1
                break
    while(line.find('\\footnote{') != -1):
        footnote= re.search('\\\\footnote\{(.*)\}', line).group(1)
        footnotes.append('<li id="fn:'+str(num)+'">'+footnote+'</li>\n')
        line = line.replace('\\footnote{'+footnote+'}', '<a href="#fn:'+str(num)+'" id="fnref:'+str(num)+'"><sup>'+str(num)+'</sup></a>')
        num += 1
    tex_file[i] = line

# replace graphics

num = 1
for i in range(size):
    line = tex_file[i]
    while line.find('\\includegraphics[') != -1:
        replace = GRAPHICS
        replace = replace.replace('URL', FIGURE_URLS[0])
        replace = replace.replace('NUM', str(num))
        line = re.sub('\\\\includegraphics\[.*\]\{.*\}', replace, line)
        del FIGURE_URLS[0]
        num += 1
    tex_file[i] = line

# replace references

num = 1
for i in range(size):
    line = tex_file[i]
    if line.find('\\ref{') != -1 or line.find('\\label{') != -1:
        for prefix, replace_text in REFERENCE_PREFIXES.items():
            while(line.find('\\label{'+prefix) != -1):
                replace = replace_text[0]
                ID = re.search('\\\\label\{'+prefix+'(.*)\}', line).group(1)
                replace = replace.replace('PREFIX', prefix)
                replace = replace.replace('ID', ID)
                line = line.replace('\\label{'+prefix+ID+'}', replace)
            while(line.find('\\ref{'+prefix) != -1):
                replace = replace_text[1]
                ID = re.search('\\\\ref\{'+prefix+'(.*)\}', line).group(1)
                replace = replace.replace('PREFIX', prefix)
                replace = replace.replace('ID', ID)
                line = line.replace('\\ref{'+prefix+ID+'}', replace)
    tex_file[i] = line

# replace advanced macros

for name, macro in MACROS.items():
    if macro[0] != '':
        word = ''
        letters = 1
        for letter in macro[0]:
            if letter == 's':
                word += '\[(.*)\]'
            if letter == 'p':
                word += '\((.*)\)'
            if letter == 'b':
                word += '\{(.*)\}'
            letters += 1
        if macro[0][0] == 's':
            starting = '['
        if macro[0][0] == 'p':
            starting = '('
        if macro[0][0] == 'b':
            starting = '{'
        for i in range(0,len(tex_file)):
            line = tex_file[i]
            while (line.find('\\'+name+starting) != -1):
                replace = macro[1][1]
                text = re.search('\\\\'+name+word, line)
                temp_text = word
                for j in range(1,letters):
                    replace = replace.replace('TEXT'+str(j), text.group(j))
                    temp_text = temp_text.replace('\\', '')
                    temp_text = temp_text.replace('(.*)', text.group(j), 1)
                line = line.replace('\\'+name+temp_text, replace)
            line = line.replace('\\'+name, macro[1][0])
            tex_file[i] = line
    else:
        tex_file[i] = tex_file[i].replace('\\'+name, macro[1][0])

last_line = tex_file[len(tex_file)-1]
del tex_file[len(tex_file)-1]
tex_file[len(tex_file):] = ['\n<ol class="footnotes">\n']
tex_file[len(tex_file):] = footnotes
tex_file[len(tex_file):] = ['</ol>\n']
tex_file[len(tex_file):] = [last_line]

html = ''
for i in range(len(tex_file)):
    html += tex_file[i]

self.editor.delete("1.0", 'end')
self.editor.insert(END, html)
