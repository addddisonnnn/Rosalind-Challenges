"""
Title: Counting DNA Nucleotides
Link: https://rosalind.info/problems/dna/

Problem:
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; 
the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s
 of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""
def countbases(sequence):
    Acount=sequence.count("A")
    Gcount=sequence.count("G")
    Ccount=sequence.count("C")
    Tcount=sequence.count("T")
    return(Acount, Ccount, Gcount, Tcount)
if __name__ == "__main__":
    filename = "rosalind_dna.txt"
    with open(filename, 'r') as file:
        filecontents = file.read()
    Acount, Ccount, Gcount, Tcount = countbases(filecontents)
    print(Acount, Ccount, Gcount, Tcount)
