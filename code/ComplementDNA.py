"""
Title: Complementing a Strand of DNA
Link: https://rosalind.info/problems/revc/

Problem:
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc 
formed by reversing the symbols of s, then taking the complement of each symbol 
(e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT
"""
def complementrary(sequence):
    complementstrand = ""
    complementdict = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}
    for base in reversed(sequence):
        complementstrand += complementdict.get(base)
    return complementstrand
if __name__ == "__main__":
    filename = "data/rosalind_revc.txt"
    with open(filename, 'r') as file:
        filecontents = file.read().strip()
    print(complementrary(filecontents))