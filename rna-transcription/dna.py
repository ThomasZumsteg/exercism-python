"""Turns DNA sequence into RNA sequence"""

def to_rna(dna):
    """Makes RNA sequence from DNA sequence"""
    return dna.translate(str.maketrans('GCTA','CGAU'))
