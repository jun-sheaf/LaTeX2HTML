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
			if replace_text_size == 3:
				while '\\begin{'+environment+'}[' in line:
					replace = replace_text[2]
					label = regex.search('\\\\begin\{'+environment+'\}'+'(\[(?:[^\[\]]++|(?1))*\])', line).group(1)[1:-1]
					replace = replace.replace('LABEL', label)
					replace = replace.replace('NUM', str(num))
					line = line.replace('\\begin{'+environment+'}['+label+']', replace)
					num += 1
			while '\\begin{'+environment+'}' in line:
				replace = replace_text[0]
				replace = replace.replace('NUM', str(num))
				line = line.replace('\\begin{'+environment+'}', replace)
				num += 1
			line = line.replace('\\end{'+environment+'}', replace_text[1])
			tex_file[i] = line