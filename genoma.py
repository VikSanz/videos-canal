import Bio
import fastaparser

### Muestra de Wuhan
from Bio import SeqIO

for record in SeqIO.parse("sequence.fasta", "fasta"):
    print(record.id)

### Muestra de Washington
from Bio import SeqIO

for record in SeqIO.parse("sequence-2.fasta", "fasta"):
    print(record.id)

### Muestra de Wuhan
with open("sequence.fasta") as fasta_file:
        parser = fastaparser.Reader(fasta_file)
        for seq in parser:
            # seq is a FastaSequence object
            print('ID:', seq.id)
            print('Descripción:', seq.description)
            print('Secuencia:', seq.sequence_as_string())
            print()

wuhan = seq.sequence_as_string()

### Muestra de Washington
with open("sequence-2.fasta") as fasta_file:
        parser = fastaparser.Reader(fasta_file)
        for seq in parser:
            # seq is a FastaSequence object
            print('ID:', seq.id)
            print('Descripción:', seq.description)
            print('Secuencia:', seq.sequence_as_string())
            print()

wa = seq.sequence_as_string()

len(wuhan)

### Puedes buscar cualquier proteína del link: https://www.nytimes.com/interactive/2020/04/03/science/coronavirus-genome-bad-news-wrapped-in-protein.html
nsp1 = 'auggagagccuugucccugguuucaacgagaaaacacacguccaacucaguuugccuguuuuacagguucgcgacgugcucguacguggcuuuggagacuccguggaggaggucuuaucagaggcacgucaacaucuuaaagauggcacuuguggcuuaguagaaguugaaaaaggcguuuugccucaacuugaacagcccuauguguucaucaaacguucggaugcucgaacugcaccucauggucauguuaugguugagcugguagcagaacucgaaggcauucaguacggucguaguggugagacacuugguguccuugucccucaugugggcgaaauaccaguggcuuaccgcaagguucuucuucguaagaacgguaauaaaggagcugguggccauaguuacggcgccgaucuaaagucauuugacuuaggcgacgagcuuggcacugauccuuaugaagauuuucaagaaaacuggaacacuaaacauagcagugguguuacccgugaacucaugcgugagcuuaacggaggg'

nsp = nsp1.replace('u', 'T').replace('a', 'A').replace('g', 'G').replace('c','C')

nsp in wuhan

wuhan.find(nsp)

### Frecuencia de nucleótidos
freq1 = {b: wuhan.count(b)/len(wuhan) for b in 'ATGC'}
