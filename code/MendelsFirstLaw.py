"""
Title: Mendel's First Law
Link: https://rosalind.info/problems/iprb/

Problem:
An event is a collection of outcomes. Because outcomes are distinct, the probability of an event
can be written as the sum of the probabilities of it constituent outcomes.

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals 
are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a 
dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Sample Dataset:
2 2 2

Sample Output:
0.78333

My thought process:

For example: six genotypes: two DD, two Dd, two dd
P(X=DD , Y=DD)=(1/3)(1/5)=(1/15) ~ 100% produce dominant
P(X=DD , Y=Dd)=(1/3)(2/5)=(2/15) ~ 100% produce dominant
P(X=DD , Y=dd)=(1/3)(2/5)=(2/15) ~ 100% produce dominant

P(X=Dd , Y=DD)=(1/3)(2/5)=(2/15) ~ 100% produce dominant
P(X=Dd , Y=Dd)=(1/3)(1/5)=(1/15) ~ 75% produce dominant
P(X=Dd , Y=dd)=(1/3)(2/5)=(2/15) ~ 50% produce dominant

P(X=dd , Y=dd)=(1/3)(1/5)=(1/15) ~ 0% produce dominant
P(X=dd , Y=Dd)=(1/3)(2/5)=(2/15) ~ 50% produce dominant
P(X=dd , Y=DD)=(1/3)(2/5)=(2/15) ~ 100% produce dominant

P(dominant)=    P(X=DD) + 
                P(X=Dd , Y=DD) + P(X=Dd , Y=Dd)*75% + P(X=Dd , Y=dd)*50% + 
                P(X=dd , Y=dd)*0% + P(X=dd , Y=Dd)*75% + P(X=dd , Y=DD)*100%
"""
import random
if __name__ == "__main__":
    filename = "data/rosalind_iprb.txt"
    with open(filename, 'r') as f:
        k, m, n = f.readline().strip().split()
        k, m, n = int(k), int(m), int(n)
    total = k+m+n

    probability = 0.0 # keep track of the probability of a dominant phenotype

    # get the probability one parent is homozygous dominant
    prob_X_homo_dom = k/total

    # get the probabilities one parent is heterozygous and its potential mates
    prob_X_heter_Y_homo_dom = (m/total)*(k/(total-1))
    prob_X_heter_Y_heter = (m/total)*((m-1)/(total-1))
    prob_X_heter_Y_homo_rec = (m/total)*(n/(total-1))

    # get the probabilities one parent is homozygous recessive and its potential mates
    prob_X_homo_rec_Y_homo_dom = (n/total)*((k)/(total-1))
    prob_X_homo_rec_Y_heter = (n/total)*((m)/(total-1))
    prob_X_homo_rec_Y_homo_rec = (n/total)*((n-1)/(total-1))

    # add the probability of one parent being homozygous dominant
    probability += prob_X_homo_dom
    # add the probability of one parent being heterozygous and its potential mates
    probability += prob_X_heter_Y_homo_dom + prob_X_heter_Y_heter*(3/4)+prob_X_heter_Y_homo_rec*(1/2)
    # add the probability of one parent being homozygous recessive and its potential mates
    probability += prob_X_homo_rec_Y_homo_dom + prob_X_homo_rec_Y_heter*(1/2)
    
    print(probability)