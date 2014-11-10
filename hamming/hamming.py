"""Finds the hamming distance between two DNA sequences"""

def distance(strand_a, strand_b):
    """Counts the differences in two sequences of DNA"""
    differences = 0
    for nucleotide_a, nucleotide_b in zip(strand_a, strand_b):
        if nucleotide_a != nucleotide_b:
            differences += 1
    return differences
