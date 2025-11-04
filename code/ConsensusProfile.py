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
if __name__ == "__main__":
    filename = "data/rosalind_cons.txt"
    sequences = []
    current_sequence = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            if line.startswith('>'):
                if current_sequence:  # Save the previous sequence if one exists
                    sequences.append("".join(current_sequence))
                current_sequence = []  # Start a new sequence
            else:
                current_sequence.append(line)
        if current_sequence:  # Save the last sequence
            sequences.append("".join(current_sequence))
    sequencelength = len(sequences[0]) #save for efficency
    
    #initialize a matrix of size four (four bases) by length of sequence
    #The order of bases is A, C, G, T
    CountPerBase = [[0] * sequencelength for _ in range(4)]
    
    for sequence in sequences: #iterate through each sequence
        for i in range(sequencelength): #iterate through each base of the sequence
            if sequence[i] == "A": #for each base that is seen, increase the count
                CountPerBase[0][i]+=1
            elif sequence[i] == "C":
                CountPerBase[1][i]+=1
            elif sequence[i] == "G":
                CountPerBase[2][i]+=1
            else:
                CountPerBase[3][i]+=1
    
    consensus = "" #forming the consensus sequence
    for i in range(sequencelength): #iterate through the length of a sequence
        currentbase = "A" #keep track of what base has the highest count
        currentbasecount = CountPerBase[0][i] #keep track of the base's count
        if currentbasecount <= CountPerBase[1][i]:
            currentbase = "C"
            currentbasecount = CountPerBase[1][i]
        if currentbasecount <= CountPerBase[2][i]:
            currentbase = "G"
            currentbasecount = CountPerBase[2][i]
        if currentbasecount <= CountPerBase[3][i]:
            currentbase = "T"
            currentbasecount = CountPerBase[3][i]
        consensus += currentbase #the base with the highest count will be added to the consensus
    print(consensus)
    print("A:", *CountPerBase[0])
    print("C:", *CountPerBase[1])
    print("G:", *CountPerBase[2])
    print("T:", *CountPerBase[3])