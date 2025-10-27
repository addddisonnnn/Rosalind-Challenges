"""
Title: Rabbits and Recurrence Relations
Link: https://rosalind.info/problems/fib/

Problem:
A sequence is an ordered collection of objects. We use a_n to represent the n-th of a sequence.

A recurrence relation is a way of defininf the terms of a seuqnece with 
respect to the values of previous terms.

When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation 
to generate terms for progressively larger values of n. This problem introduces us to the computational technique of dynamic programming, 
which successively builds up solutions by using the answers to smaller cases.

Input: (n, k) where n <= 40, k <=5

Output: Fn = Fn-1 + Fn-2 * 3
Total number of rabbit pairs present after n months, where every pair of reproduction age produces a litter of k raabits

Sample Dataset:
5 3
Sample Output
19

F1 = 1
F2 = 1
F3 = F2 + F1 * 3 = 1 + 1 * 3 = 4
F4 = F3 + F2 * 3 = 4 + 1 * 3 = 7
F5 = F4 + F3 * 3 = 7 + 4 * 3 = 19
F6 = F5 + F4 * 3 = 19 + 7 * 3 = 40
"""
def computefib(n, k):
    if n==1 or n==2: #this should always be the same regardless of k
        return 1
    Fib = [0] * (int(n)+1) #create an array of appropriate size
    Fib[1] = 1
    Fib[2] = 1
    
    for i in range(3, int(n)+1): #initializes the array with current and previous values
        previous = Fib[i-1]
        offspring = Fib[i-2] * k
        Fib[i] = previous + offspring
    return Fib[int(n)]

if __name__ == "__main__":
    filename = "data/rosalind_fib.txt"
    with open(filename, 'r') as file:
        line = file.read().strip()
    parts = line.split()
    n = int(parts[0])
    k = int(parts[1])
    print(computefib(n,k))