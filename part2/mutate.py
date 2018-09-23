import sys

def changeProtein(proteinFile, position, mutation):
	codon = {'ATT':'I', 'ATC':'I', 'ATA':'I', 'CTT':'L', 'CTC':'L', 'CTA':'L',\
	'CTG':'L', 'TTA':'L', 'TTG':'L', 'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',\
	'TTT':'F', 'TTC':'F', 'ATG':'M', 'TGT':'C', 'TGC':'C', 'GCT':'A', 'GCC':'A',\
	'GCA':'A', 'GCG':'A', 'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'CCT':'P',\
	'CCC':'P', 'CCA':'P', 'CCG':'P', 'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',\
	'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S', 'TAT':'Y',\
	'TAC':'Y', 'TGG':'W', 'CAA':'Q', 'CAG':'Q', 'AAT':'N', 'AAC':'N', 'CAT':'H',\
	'CAC':'H', 'GAA':'E', 'GAG':'E', 'GAT':'D', 'GAC':'D', 'AAA':'K', 'AAG':'K',\
	'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R'}

	f = open(proteinFile, 'r')
	next(f)
	protein_seq = f.readlines()
	f.close
	protein = ''
	for frag in protein_seq:
		protein += frag.rstrip()
	res = list(protein)
	res[position] = codon[mutation]
	return ''.join(res)

if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	next(f)
	# sys.argv[1] must be the file name of the input file.
	dis = f.readlines()
	f.close

	#define the position of gene
	g_pos = int(sys.argv[2])

	gene = ''
	for fragment in dis:
		gene += fragment.rstrip()

	gene_loc = g_pos+int(sys.argv[3])-2

	codon = ''
	if g_pos%3 == 0:
		codon = gene[gene_loc-2]+gene[gene_loc-1]+sys.argv[4]
	if g_pos%3 == 1:
		codon = sys.argv[4] + gene[(gene_loc+1)] + gene[(gene_loc +2)]
	if g_pos%3 == 2:
		codon = gene[(gene_loc-1)] + sys.argv[4] + gene[(gene_loc + 1)]
	print(codon)
	#find the position of amino acid
	a_pos = g_pos//3
	if g_pos%3==0:
		a_pos -= 1
	proteinFile = sys.argv[5]
	res = changeProtein(proteinFile, a_pos, codon)
	print(res)






