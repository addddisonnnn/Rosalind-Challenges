"""
Title: Finding a Motif in DNA
Link: https://rosalind.info/problems/subs/

Problem:
Given two strings s and t, t is a substring of s. If t is contained as a contiguous collection of symbols in 
s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., 
the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s.

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset:
GATATATGCATATACTT
ATAT

Sample Output:
2 4 10

"""
if __name__ == "__main__":
    filename = "data/rosalind_subs.txt"
    with open(filename, 'r') as file:
        s = file.readline().strip()
        t = file.readline().strip()
    
    coord = [] #list that will be returned
    for i in range(len(s)-len(t)):  #loop through the length of s, minus the length of t since we're creating subsets
        subset=s[i: i+len(t)] #creates subsets within the s string
        if subset==t: #if that subset is equal to t, record its position
            coord.append(i+1)

    print(*coord)