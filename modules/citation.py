import bibtexparser

with open(FILES['bib']) as bibtex_file:
	bib_database = bibtexparser.load(bibtex_file)

BIB_DICT = {}

j = 0
for i in range(size):
	line = tex_file[i]
	while '\\cite{' in line:
		cite = regex.search("\\\\cite\{(.*?)\}", line)
		if cite.group(1) not in BIB_DICT:
			j += 1
			BIB_DICT[cite.group(1)] = str(j)
		else:
			j = int(BIB_DICT[cite.group(1)])
		replace = CITATION_TEXT[0]
		replace = replace.replace('ID',cite.group(1))
		replace = replace.replace('NUM',str(j))
		line = line.replace('\\cite{'+cite.group(1)+'}', replace )
	while '\\cite[' in line:
		cite = regex.search("\\\\cite\[(.*?)\]\{(.*?)\}", line)
		if cite.group(2) not in BIB_DICT:
			j += 1
			BIB_DICT[cite.group(2)] = str(j)
		else:
			j = int(BIB_DICT[cite.group(2)])
		replace = CITATION_TEXT[1]
		replace = replace.replace('TEXT',cite.group(1))
		replace = replace.replace('NUM',str(j))
		replace = replace.replace('ID',cite.group(2))
		line = line.replace('\\cite['+cite.group(1)+']{'+cite.group(2)+'}', replace )
	tex_file[i] = line
	
def ProcessBib( entry , text ):
	bib = {'TITLE': None, 'AUTHOR': None, 'PUBLISHER': None, 'ADDRESS': None, 'YEAR': None, 'DOI': None, 'TYPE': None }
	
	if 'title' in entry:
		bib['TITLE'] = entry['title'][1:-1]

	if 'author' in entry:
		bib['AUTHOR'] = ''
		entry['author'] = entry['author'].split(' and ')
		if len(entry['author']) == 1:
			entry['author'][0] = entry['author'][0].strip('.')
			bib['AUTHOR'] = entry['author'][0].strip()
		elif len(entry['author']) == 2:
			bib['AUTHOR'] = entry['author'][0].strip()+' and '+entry['author'][1].strip()
		else:
			for i in range(1,len(entry['author'])-1):
				bib['AUTHOR'] += ', '+entry['author'][i].strip()
			bib['AUTHOR'] += ', and '+entry['author'][len(entry['author'])-1].strip()

	if 'publisher' in entry:
		bib['PUBLISHER'] = entry['publisher'].strip()

	if 'address' in entry:
		bib['ADDRESS'] = entry['address'].strip()

	if 'year' in entry:
		bib['YEAR'] = entry['year'].strip()

	if 'doi' in entry:
		bib['DOI'] = "<a style='font: monospace' href='https://doi.org/"+entry['doi'].strip()+"'>"+entry['doi'].strip()+'</a>'

	if 'ENTRYTYPE' in entry:
		bib['TYPE'] = entry['ENTRYTYPE'].lower().capitalize()
	
	final_entry = text
	
	for k,v in bib.items():
		if v == None:
			final_entry = final_entry.replace(k, "")
		else:
			final_entry = final_entry.replace(k, v)
	
	final_entry = final_entry[:-1]
	final_entry += "."
	final_entry = "<li id='"+entry['ID']+"'>" + final_entry
	
	return final_entry
	
bibliography = {}
for entry in bib_database.entries:
	if entry['ID'] in BIB_DICT:
		bibliography[BIB_DICT[entry['ID']]] = ProcessBib( entry , BIBLIOGRAPHY )+'\n'
		
final_bib = ""
for i in range(len(bibliography)):
	final_bib += bibliography[str(i+1)]

final_bib = final_bib.replace('  ',' ')
final_bib = final_bib.replace(' ,',',')
