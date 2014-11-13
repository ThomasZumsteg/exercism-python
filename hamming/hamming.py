"""Finds the hamming distance between two DNA sequences"""

def distance(strand_a, strand_b):
    """Counts the differences in two sequences of DNA"""
    return sum(1 for a,b in zip(strand_a, strand_b) if a != b)