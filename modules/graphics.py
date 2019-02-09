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