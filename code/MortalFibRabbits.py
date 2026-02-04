"""
Title: Consensus and Profile
Link: https://rosalind.info/problems/fibd/

Problem:
The aim is to modify the previous recurrence relation to achieve dynamic programming in
the case that all rabbits die out after a fixed number of months.
It's assumed each pair of rabbits reaches maturity in one month and produces a single pair of offspring each month.

Given: Positive integers n <= 100 and m <= 20

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months

Sample Dataset:
6 3

Sample Output:
4

F1 = 1
F2 = 1
F3 = F2 + F1 * 3 = 1 + 1 * 3 = 4
F4 = F3 + F2 * 3 = 4 + 1 * 3 = 7
F5 = F4 + F3 * 3 = 7 + 4 * 3 = 19
F6 = F5 + F4 * 3 = 19 + 7 * 3 = 40

tooyoung = prev_offspring
tooold = Fn-3_tooyoung

In the first month, the 1st pair has just been produced, totaling 1.
In the second month, the 1st pair is now an adult, totaling 1.
In the third month, the 1st pair reproduces the 2nd pair, totaling 2.
In the fourth month, the 1st dies, 2nd pair reproduces, the 2nd is now an adult, totaling 3.
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
    filename = "data/rosalind_fibd.txt"
    with open(filename, 'r') as file:
        line = file.read().strip()
    parts = line.split()
    n = int(parts[0])
    k = int(parts[1])
    print(computefib(n,k))