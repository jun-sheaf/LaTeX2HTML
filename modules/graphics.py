num = 1
for i in range(size):
    line = tex_file[i]
    while '\\includegraphics[' in line:
        replace = GRAPHICS
        replace = replace.replace('URL', FIGURE_URLS[0])
        replace = replace.replace('NUM', str(num))
        line = regex.sub('\\\\includegraphics\[.*?\]\{.*?\}', replace, line)
        del FIGURE_URLS[0]
        num += 1
    tex_file[i] = line