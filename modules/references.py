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