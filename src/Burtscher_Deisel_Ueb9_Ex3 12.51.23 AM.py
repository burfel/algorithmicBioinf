# Using Python 2.7 /w Biopython
from Bio import SeqIO

global tracematrix

# recursively calculates all basepairs by backtracking through the tracematrix
def traceback(i,j):
    if (tracematrix[i][j] is not None):
        if (tracematrix[i][j][0][0] == i+1) & (tracematrix[i][j][0][1] == j-1):
            basepairs.append([i,j])
        traceback(tracematrix[i][j][0][0],tracematrix[i][j][0][1])
        if (len(tracematrix[i][j]) == 2): 
            traceback(tracematrix[i][j][1][0],tracematrix[i][j][1][1])

# calculates the score delta for two symbols 
def scoring(a, b):
    if ((a == 'G') & (b == 'C')) | ((a == 'C') & (b == 'G')):
        return 3
    elif ((a == 'A') & (b == 'U')) | ((a == 'U') & (b == 'A')) | \
        ((a == 'A') & (b == 'T')) | ((a == 'T') & (b == 'A')) :
        return 2
    else:
        return 0
    
if __name__ == "__main__":
    # read fasta-file
    RNA = list(SeqIO.parse(open("rna16s.fa"),'fasta'))[0].seq
    length = len(RNA)
    
    # initialize nussinov-matrix and trace-matrix
    nussinov = [[0 for i in range(length)] for j in range(length)]
    tracematrix = [[None for i in range(length)] for j in range(length)]
    
    # move through all diagonals
    minHairpinSize = 3
    diag = 1+minHairpinSize
    nr = 0
    while (diag<length):
        i = nr
        j = diag+nr
        nr = nr + 1
        if nr == length - diag:
            nr = 0
            diag = diag + 1
            
        # calculate all values and traces hat would be possibilities if a 
        # bifurcation occured
        bifurValues = [nussinov[i][k] + nussinov[k+1][j] for k in range(i+1,j)]
        bifurTraces = [[[i,k],[k+1,j]] for k in range(i+1,j)]
        # no bifurcation possible
        if (j-i < 2):
            bifurValues = [-1]
            bifurTraces = [[None]]
            
        # calculate the four possible values and their traces
        values = [nussinov[i+1][j],nussinov[i][j-1], \
            nussinov[i+1][j-1] + scoring(RNA[i],RNA[j]) ,max(bifurValues)]
        traces = [[[i+1,j]],[[i,j-1]],[[i+1,j-1]], \
            bifurTraces[bifurValues.index(max(bifurValues))]]

        # choose the maximum value and its corresponding trace
        nussinov[i][j] = max(values)
        tracematrix[i][j] = traces[values.index(max(values))]

    
    # calculate traceback through the trace matrix beginning at the upper right 
    # cell of the 
    traceback(0,length-1)
    basepairs = []

    # print results and calculates the vienna-string by marking every 
    # beginning position of a basepair with "(", every ending one 
    # with ")" and everything else with "."
    print "Basepairs: "
    vienna = ["." for i in range(length)]
    for pair in basepairs:
        print repr(pair[0]) + "-" + repr(pair[1]) + "\t" + RNA[pair[0]] \
            + "==" + RNA[pair[1]]
        vienna[pair[0]] = "("
        vienna[pair[1]] = ")"
    print "Score: -" + repr(len(basepairs))
    print "Vienna: " + "".join(vienna)