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