"""
Title: Counting Point Mutations
Link: https://rosalind.info/problems/hamm/

Problem:
Given two strings s and t of equal length, the Hamming distance between s and t, 
denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).

Sample Dataset:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output
7
"""
if __name__ == "__main__":
    filename = "data/rosalind_hamm.txt"
    s_seq, t_seq = "",""

    with open(filename, 'r') as f:
        s_seq = f.readline().strip()
        t_seq = f.readline().strip()

    distance = 0
    for i in range(len(s_seq)):
        if s_seq[i] != t_seq[i]:
            distance+=1
    print(distance)