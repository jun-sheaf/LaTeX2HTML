num = 1
for i in range(size):
	line = tex_file[i]
	if '\\ref{' in line or '\\label{' in line:
		for prefix, replace_text in REFERENCE_PREFIXES.items():
			while '\\label{'+prefix in line:
				replace = replace_text[0]
				ID = regex.search('\\\\label\{'+prefix+'(.*?)\}', line).group(1)
				replace = replace.replace('PREFIX', prefix)
				replace = replace.replace('ID', ID)
				line = line.replace('\\label{'+prefix+ID+'}', replace)
			while '\\ref{'+prefix in line:
				replace = replace_text[1]
				ID = regex.search('\\\\ref\{'+prefix+'(.*?)\}', line).group(1)
				replace = replace.replace('PREFIX', prefix)
				replace = replace.replace('ID', ID)
				line = line.replace('\\ref{'+prefix+ID+'}', replace)
	tex_file[i] = line