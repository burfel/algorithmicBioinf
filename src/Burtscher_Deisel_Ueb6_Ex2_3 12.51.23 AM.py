import matplotlib.pyplot as plt
import math
import numpy

rate_matrix = [ [1715,544,3155,0,4380,0,4329,4188,442,2526,2377],
                [224,1967,0,0,0,0,0,0,914,765,427],
                [1185,1765,0,4380,0,0,0,192,3015,1057,525],
                [1256,104,1225,0,0,4380,51,0,9,32,1051]]
pi = [0.3,0.2,0.2,0.3]
                
if __name__ == "__main__":
    # calculate count and probability matrix
    C_PC = [] # Count-Matrix with Pseudo-Counts
    for line in rate_matrix:
        C_PC_line = []
        for cell in line:
            C_PC_line.append(cell+1)
        C_PC.append(C_PC_line)
    print "C'= " + repr(C_PC) + "\n"
    P = [] # Probability-Matrix
    for line in C_PC:
        P_line = []
        for i in range(len(line)):
            P_line.append(\
                line[i]*1.0/(C_PC[0][i] + C_PC[1][i] + \
                C_PC[2][i] + C_PC[3][i]))
        P.append(P_line)
    print "P'= " + repr(P) + "\n"
    
    # calculate Log-Odds Score Matrix
    S = [] # Position-specific Log-Odds Score-Matrix using ln
    for i in range(len(P)):
        S_line = []
        for cell in P[i]:
            S_line.append(math.log((cell/pi[i]),math.exp(1)))
        S.append(S_line)
    print "S= " + repr(S) + "\n"
    
    # calculate the Entropy at every Position
    H = [] # Entropy-Matrix
    for i in range(len(P[0])):
        terms = []
        for j in range(len(P)):
            terms.append(P[j][i] * math.log(P[j][i],2))
        H.append(- sum(terms))
    print "H= " + repr(H) + "\n"
    
    # Calculate Share of Entropy
    H_P = [] # Share of Entropy per Symbol and Position
    for line in P:
        H_P_line = []
        for i in range(len(line)):
            H_P_line.append(line[i]*(2-H[i]))
        H_P.append(H_P_line)
        
    # Plot as bar Graph
    ind = numpy.arange(11) 
    width = 0.5
    pT = plt.bar(ind, H_P[3], width, color='red')
    pG = plt.bar(ind, H_P[2], width, color='yellow', bottom=H_P[3])
    pC = plt.bar(ind, H_P[1], width, color='blue', \
        bottom=[sum(i) for i in zip(H_P[3], H_P[2])])
    pA = plt.bar(ind, H_P[0], width, color='green', \
        bottom=[sum(i) for i in zip(H_P[3], H_P[2],H_P[1])])
    plt.xlabel('positions')
    plt.xticks(ind+width/2., range(1,12))
    plt.ylabel('bits')
    plt.title('Motif-Logo of the GATA-motif')
    plt.legend( (pA[0], pC[0], pG[0], pT[0]), ('A', 'C', 'G', 'T') )
    plt.savefig('Burtscher_Deisel_Ueb6_Ex2_3.png')
    plt.show()

            