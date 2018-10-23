### mutate DNA and its protein sequence at the corresponding amino acid site

### This program is to print out the sequence of mutated protein on the terminal.

#### To run the project with Python 3.0, run the command on your terminal.
#### python mutate.py ADAgene.fasta ADAprotein.fasta 239 129 G

-ADAgene.fasta is the file of the gene of ADA
-ADAprotein.fasta is the file of the protein sequence of ADA
-239 is the position for mutation counting from the start codon.
-129 is the initial star codon CDS
-G is the mutation of the DNA at opsition 239

To test the program, under other circumstances:

#### Case1 (NM_000022.2(ADA):c.22G>A (p.Asp8Asn)), run the command on your terminal
### python mutate.py ADAgene.fasta ADAprotein.fasta 22 129 A

#### Case2 (NM_000022.2(ADA):c.239A>G (p.Lys80AGA), run the command on your terminal
### python mutate.py ADAgene.fasta ADAprotein.fasta 239 129 G

#### Case3 (NM_001146725.1(Bombyx mori cytochrome P450): c.30T>A(p.Ile10Met) ATT > ATG), run your command on your terminal 
### python mutate.py P450gene.fasta P450protein.fasta 30 35 G 

reference:
https://www.ncbi.nlm.nih.gov/clinvar/variation/1973/
https://www.ncbi.nlm.nih.gov/nuccore/NM_001146725.1

### example of mutating DNA and its Protein sequence
#### Given gene ADA (RefSeq NM_000022.2), forward translate the DNA substitution mutation c.239A>G to the expected amino acid change and codon position.
#### c.239A>G denotes that at nucleotide 239 an A is changed to a G. Nucleotide 1 is the A of the ATG-translation initiation codon.

#### Find the mRNA in the GenBank at NCBI at the following website:https://www.ncbi.nlm.nih.gov/nuccore/NM_000022.2/
#### Save the FASTA file of the sequence of NM_000022.2, the mRNA of Homo sapiens adenosine deaminase (ADA) https://www.ncbi.nlm.nih.gov/nuccore/NM_000022.2/

#### Find out the corresponding change of amino acid, based on the codon change. Since the c239A>G will mutate AAA into AGA, by looking up into a DNA codon table, we could conclude a Lysine(K) has been mutated into an Arginine(R) at position math.

#### get the protein sequence from the website below: https://www.ncbi.nlm.nih.gov/protein/NP_000013.2?report=fasta

#### Get the mutated protein sequence by changing the amino acid. For ADA protein sequence, change the Lysine(K) at position 80 of protein sequence into the Arginine(R).
