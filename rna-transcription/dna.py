"""Turns DNA sequence into RNA sequence"""

def to_rna(dna):
    """Makes RNA sequence from DNA sequence"""
    dna_to_rna = {'G': 'C',
                  'C': 'G',
                  'T': 'A',
                  'A': 'U',
                 }
    rna = ''
    for nucleotide in dna:
        rna += dna_to_rna[nucleotide]
    return rna
