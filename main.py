tex_file = open(FILES['select'])
config = exec(open('customize.ini').read())
tex_file = tex_file.readlines()

# delete preamble

for i in range(len(tex_file)):
	if '\\begin{document}' in tex_file[0]:
		break
	del tex_file[0]

size = len(tex_file)

# changing mandatory elements

for i in range(size):
	while '<' in tex_file[i] or '>' in tex_file[i]:
		tex_file[i] = tex_file[i].replace('<', "&lt")
		tex_file[i] = tex_file[i].replace('>', "&gt")

# replace environments

exec(open('modules/environments.py').read())

# replace footnotes

exec(open('modules/footnotes.py').read())

# replace graphics

exec(open('modules/graphics.py').read())

# replace citations

if FILES['bib'] != None:
	exec(open('modules/citation.py').read())

# replace references

exec(open('modules/references.py').read())

# replace advanced macros

exec(open('modules/macros.py').read())

# replace math_delimiters

need_to_replace = CENTERED_MATH_DELIMITERS.split(',')
flag = 0
for x in need_to_replace:
	x = x.strip()
	x = x.split(';')
	for i in range(size):
		while x[0] in tex_file[i] or x[1] in tex_file[i]:
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
		while x[0] in tex_file[i] or x[1] in tex_file[i]:
			if flag == 0:
				tex_file[i] = tex_file[i].replace(x[0],'\\(',1)
				flag = 1
			else:
				tex_file[i] = tex_file[i].replace(x[1],'\\)',1)
				flag = 0

last_line = tex_file[len(tex_file)-1]
del tex_file[len(tex_file)-1]
if FILES['bib'] != None:
	tex_file[len(tex_file):] = ['\n<div class = "bib-label">References</div><ol class="bibliography">\n']
	tex_file[len(tex_file):] = final_bib
	tex_file[len(tex_file):] = ['</ol>\n']
if len(footnotes) != 0:
	tex_file[len(tex_file):] = ['<hr>\n<ol class="footnotes">\n']
	tex_file[len(tex_file):] = footnotes
	tex_file[len(tex_file):] = ['</ol>\n']

tex_file[len(tex_file):] = [last_line]

html = ''
for i in range(len(tex_file)):
	html += tex_file[i]

self.editor.delete("1.0", 'end')
self.editor.insert(END, html)
