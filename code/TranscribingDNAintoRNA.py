"""
Title: Transcribing DNA into RNA
Link:

Problem:
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u 
is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset
GATGGAACTTGACTACGTAAATT
Sample Output
GAUGGAACUUGACUACGUAAAUU
"""
def transcribe(sequence):
    RNAseq = ""
    for i in range(len(sequence)):
        if sequence[i]=="T":
            RNAseq+="U"
        else:
            RNAseq+=sequence[i]
    return(RNAseq)

if __name__ == "__main__":
    filename = "data/rosalind_rna.txt"
    with open(filename, 'r') as file:
        filecontents = file.read().strip()
    sequence = transcribe(filecontents)
    print(sequence)