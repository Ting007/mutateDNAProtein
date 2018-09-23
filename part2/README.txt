To run the project with Python 3.0:
python mutate.py ADAgene.fasta ADAprotein.fasta 239 129 G

-ADAgene.fasta is the file of the gene of ADA
-ADAprotein.fasta is the file of the protein sequence of ADA
-239 is the position for mutation counting from the start codon.
-129 is the initial star codon CDS
-G is the mutation of the DNA at opsition 239

To test the program:

Case1 (NM_000022.2(ADA):c.22G>A (p.Asp8Asn)):
python mutate.py ADAgene.fasta ADAprotein.fasta 22 129 A

Case2 (NM_000022.2(ADA):c.239A>G (p.Lys80AGA):
python mutate.py ADAgene.fasta ADAprotein.fasta 239 129 G

Case3 (NM_001146725.1(Bombyx mori cytochrome P450): c.30T>A(p.Ile10Met) ATT > ATG): 
python mutate.py P450gene.fasta P450protein.fasta 30 35 G 

reference:
https://www.ncbi.nlm.nih.gov/clinvar/variation/1973/
https://www.ncbi.nlm.nih.gov/nuccore/NM_001146725.1



