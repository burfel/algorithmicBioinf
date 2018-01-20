# Using Python 2.7
import matplotlib.pyplot as plt
import math
import numpy

pseudocount = 0.00001
seqs = ["UAAACUCUAAAUUUAGAUGUCC","UAAACUCACGAUAGGGAUGUCC",\
    "UAAACUCUACAUGUGGAUGUCC","UAAACUCUCCAUUGAGAUGUCC"]
nucs = "ACGU"
nucCombs = [i + j for i in nucs for j in nucs]
indCombs = []
for i in range(len(seqs[0])):
    for j in range (i+1,len(seqs[0])):
        indCombs.append([i,j])
MI = []
        
f = [[None]*len(nucs) for i in range(len(seqs[0]))]
f1 = [[None]*len(nucCombs) for i in range(len(indCombs))]

if __name__ == "__main__":
    # calculate f(x_i) for all x and all i
    for i in range(len(seqs[0])):
        string = seqs[0][i] + seqs[1][i] + seqs[2][i] + seqs[3][i]
        for x in range(len(nucs)):
            f[i][x] = string.count(nucs[x]) + pseudocount
            
    # calculate f(x_i,y_j) for all x,y,i and j
    for ij in range(len(indCombs)):
        [i,j] = indCombs[ij]
        string = seqs[0][i] + seqs[0][j] + "x" + seqs[1][i] + seqs[1][j] + \
            "x" + seqs[2][i] + seqs[2][j] + "x" + seqs[3][i] + seqs[3][j]
        for xy in range(len(nucCombs)):
            f1[ij][xy] = string.count(nucCombs[xy]) + pseudocount

    # calculate MI_ij for all i and j
    for ij in range(len(indCombs)):
        sum = 0
        multiplier = 1
        for xy in range(len(nucCombs)):
            fx = f[indCombs[ij][0]][nucs.index(nucCombs[xy][0])]
            fy = f[indCombs[ij][1]][nucs.index(nucCombs[xy][1])]
            fxy = f1[ij][xy]
            sum = sum + (fxy * math.log(fxy/(fx*fy), 2))
        MI.append(sum*multiplier)

    # print results
    for ij in range(len(indCombs)):
        print "MI_(" + repr(indCombs[ij][0]) + "," + repr(indCombs[ij][1]) + ") = " + repr(MI[ij])

        