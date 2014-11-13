"""Turns DNA sequence into RNA sequence"""

from string import maketrans

def to_rna(dna):
    """Makes RNA sequence from DNA sequence"""
    return dna.translate(maketrans('GCTA','CGAU'))
