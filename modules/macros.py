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