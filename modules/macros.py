for name, macro in MACROS.items():
	if macro[0] != '':
		param = []
		letters = 1
		for letter in macro[0]:
			if letter == 's':
				param.append('(\[(?:[^\[\]]++|(?'+str(letters)+'))*\])')
			if letter == 'p':
				param.append('(\((?:[^\(\)]++|(?'+str(letters)+'))*\))')
			if letter == 'b':
				param.append('(\{(?:[^\{\}]++|(?'+str(letters)+'))*\})')
			letters += 1
		word = ''
		for p in param:
			word += p
		if macro[0][0] == 's':
			starting = '['
		if macro[0][0] == 'p':
			starting = '('
		if macro[0][0] == 'b':
			starting = '{'
		for i in range(0,len(tex_file)):
			line = tex_file[i]
			while '\\'+name+starting in line:
				replace = macro[1][1]
				text = regex.search('\\\\'+name+word, line)
				temp_param = param
				for j in range(1,letters):
					replace = replace.replace('TEXT'+str(j), text.group(j)[1:-1])
					temp_param[j-1] = text.group(j)
				temp_text = ''
				for p in temp_param:
					temp_text += p
				line = line.replace('\\'+name+temp_text, replace)
			line = line.replace('\\'+name, macro[1][0])
			tex_file[i] = line
	else:
		tex_file[i] = tex_file[i].replace('\\'+name, macro[1][0])