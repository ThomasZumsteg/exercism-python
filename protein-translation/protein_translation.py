from itertools import count

CODON_MAP = (
    (('AUG',),'Methionine'),
    (('UUU', 'UUC'),'Phenylalanine'),
    (('UUA', 'UUG'),'Leucine'),
    (('UCU', 'UCC', 'UCA', 'UCG'),'Serine'),
    (('UAU', 'UAC'),'Tyrosine'),
    (('UGU', 'UGC'),'Cysteine'),
    (('UGG',),'Tryptophan'),
    (('UAA', 'UAG', 'UGA'),'STOP'))

PROTEINS = { codon: name for codons, name in CODON_MAP for codon in codons }

def proteins(strand):
    proteins = []
    for i in count(0, 3):
        codon = strand[i:i+3] 
        protein = PROTEINS.get(codon, None)
        if protein is 'STOP' or len(codon) < 3:
            return proteins
        elif proteins is not None:
            proteins.append(protein)
