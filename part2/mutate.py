import sys

class Protein():
	"""docstring for Protein
	codonlist is the harsh map {codon: amino acid}
	"""

	codonlist = {'ATT':'I', 'ATC':'I', 'ATA':'I', 'CTT':'L', 'CTC':'L', 'CTA':'L',\
	'CTG':'L', 'TTA':'L', 'TTG':'L', 'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',\
	'TTT':'F', 'TTC':'F', 'ATG':'M', 'TGT':'C', 'TGC':'C', 'GCT':'A', 'GCC':'A',\
	'GCA':'A', 'GCG':'A', 'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'CCT':'P',\
	'CCC':'P', 'CCA':'P', 'CCG':'P', 'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',\
	'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S', 'TAT':'Y',\
	'TAC':'Y', 'TGG':'W', 'CAA':'Q', 'CAG':'Q', 'AAT':'N', 'AAC':'N', 'CAT':'H',\
	'CAC':'H', 'GAA':'E', 'GAG':'E', 'GAT':'D', 'GAC':'D', 'AAA':'K', 'AAG':'K',\
	'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R'}

	def __init__(self):
		#geneSeq is the gene sequence
		#proteinSeq is the protein sequence
		#mutation is the codon as a result of mutation
		self.geneSeq = None
		self.proteinSeq = None
		self.mutation = None

	def setGeneSeq(self, geneFile):
		"""
		setter for geneSeq
		setGeneSeq(geneFile): read the DNA-seq file and set self.geneseq
		geneFile: str, filename of gene sequence
		self.geneSeq: str
		"""
		f = open(geneFile, 'r')
		next(f)
		dis = f.readlines()
		f.close
		gene = ''
		for fragment in dis:
			gene += fragment.rstrip()
		self.geneSeq = gene

	def setProtSeq(self, protFile):
		"""
		setter for proteinSeq
		setProtSeq(protFile): read the protein filr and set set.proteinSeq
		protFile: str, filename of protein sequence
		self.proteinSeq: str

		"""
		f = open(protFile, 'r')
		next(f)
		protein_seq = f.readlines()
		f.close
		protein = ''
		for frag in protein_seq:
			protein += frag.rstrip()
		self.proteinSeq = protein

	def geneMutate(self, g_pos, gene_loc, mutate):
		"""
		setter for self.mutation
		g_pos: int, is the location of mutation counting from the start codon atg of CDS
		gene_location: int, is the location of the base of the whole gene including the fragment before CDS
		mutate: char, is the designed mutation
		self.mutation: str, the codon after mutation
		"""
		if g_pos%3 == 0:
			codon = self.geneSeq[gene_loc-2]+self.geneSeq[gene_loc-1]+mutate
		if g_pos%3 == 1:
			codon = mutate +self.geneSeq[(gene_loc+1)] +self.geneSeq[(gene_loc +2)]
		if g_pos%3 == 2:
			codon = self.geneSeq[(gene_loc-1)] + mutate + self.geneSeq[(gene_loc + 1)]
		self.mutation = codon



	def mutateProtein(self, position):
		"""
		mutate the amino acid of protein at postion into the amimo acid /
		determined by the codon of self.mutation.
		position: int, is the position of amino acid in the protein sequence
		rtype: str, the sequence of mutated protein

		"""
		res = list(self.proteinSeq)
		res[position] = Protein.codonlist[self.mutation]
		return ''.join(res)

if __name__ == '__main__':
	ADA = Protein()
	ADA.setGeneSeq(sys.argv[1])
	ADA.setProtSeq(sys.argv[2])

	#define the position of gene where the mutation occur
	#g_pos is the postion counting from start codon
	g_pos = int(sys.argv[3])	
	#gene_loc is the postion of mutation from the start of gene
	gene_loc = g_pos+int(sys.argv[4])-2
	#find out the mutated codon
	ADA.geneMutate(g_pos, gene_loc, sys.argv[5])

	#find the position of mutated amino acid
	a_pos = g_pos//3
	if g_pos%3==0:
		a_pos -= 1

	#mutate the protein
	res = ADA.mutateProtein(a_pos)
	print(res)






