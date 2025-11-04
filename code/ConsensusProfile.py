"""
Title: Consensus and Profile
Link: https://rosalind.info/problems/cons/

Problem:
A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; 
the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix.

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset:
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output:
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6

"""
import random
if __name__ == "__main__":
    filename = "data/rosalind_cons.txt"
    sequences = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if !line.startswith('>'):
                sequences.append(line)
    
    coord = [] #list that will be returned
    for i in range(len(s)-len(t)):  #loop through the length of s, minus the length of t since we're creating subsets
        subset=s[i: i+len(t)] #creates subsets within the s string
        if subset==t: #if that subset is equal to t, record its position
            coord.append(i+1)

    print(*coord)