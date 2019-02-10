num = 1
footnotes = []
for i in range(size):
    line = tex_file[i]
    while '\\footnotemark' in line:
        line = line.replace('\\footnotemark','')
        for j in range(i,size):
            if '\\footnotetext{' in tex_file[j]:
                line_two = tex_file[j]
                footnote= regex.search('\\\\footnotetext(\{(?:[^\{\}]++|(?1))*\})', line_two).group(1)[1:-1]
                footnotes.append('<li class="footnote" id="fn:'+str(num)+'">'+footnote.strip()+' <a href="#fnref:'+str(num)+'" title="Return to line">⇪</a></li>\n')
                line_two = line_two.replace('\\footnote{'+footnote+'}', '<sup id="fnref:'+str(num)+'"><a href="#fn:'+str(num)+'">'+str(num)+'</a></sup>')
                tex_file[j] = line_two
                num += 1
                break
    while '\\footnote{' in line:
        footnote= regex.search('\\\\footnote(\{(?:[^\{\}]++|(?1))*\})', line).group(1)[1:-1]
        footnotes.append('<li class="footnote" id="fn:'+str(num)+'">'+footnote.strip()+' <a href="#fnref:'+str(num)+'" title="Return to line">⇪</a></li>\n')
        line = line.replace('\\footnote{'+footnote+'}', '<sup id="fnref:'+str(num)+'"><a href="#fn:'+str(num)+'">'+str(num)+'</a></sup>')
        num += 1
    tex_file[i] = line