# Using Python 2.7 /w Biopython

import matplotlib.pyplot as plt
import math
import numpy
from Bio import SeqIO
import itertools


nucls = ['a','c','g','t']
nucl_pairs = [''.join(a) for a in list(itertools.product(''.join(nucls), repeat=2))]
nucl_trips = [''.join(a) for a in list(itertools.product(nucl_pairs,nucls))]

# returns the Transition-Matrix for the given fasta file and prints 
# either for all three reading frames in one or seperately (given by rf_flag)
# the full Model of the Markov-Chain
def get_trans(fasta_file,rf_flag):
    # get fasta_sequences
    sequences_all = list(SeqIO.parse(open(fasta_file),'fasta'))
    if (rf_flag):
        sequences_rf = [[],[],[]]
        for seq in sequences_all:
            sequences_rf[0].append([''.join(a) for a in zip(seq[0::3],seq[1::3],seq[2::3])])
            sequences_rf[1].append([''.join(a) for a in zip(seq[1::3],seq[2::3],seq[3::3])])
            sequences_rf[2].append([''.join(a) for a in zip(seq[2::3],seq[3::3],seq[4::3])])
    else:
        sequences_rf = [[]]        
        for seq in sequences_all:
            sequences_rf[0].append([''.join(a) for a in zip(seq[0::3],seq[1::3],seq[2::3])])
    trans_m = []
    for i in range(len(sequences_rf)):
        # calculate Count-Matrix
        count_m = []
        for pair in nucl_pairs:
            count_m_line = []
            for nucl in nucls:
                c = 0
                for seq in sequences_rf[i]:
                    c = c + seq.count(pair+nucl)
                count_m_line.append(c)
            count_m.append(count_m_line)
        # calculate Transition-Matrix
        trans_m_rf = []
        for line in count_m:
            trans_m_rf_line = []
            for cell in line:
                trans_m_rf_line.append(cell*1.0/sum(line))
            trans_m_rf.append(trans_m_rf_line)
        trans_m.append(trans_m_rf)
        # print the full Model of the Markov-Chain
        print "Markow Kette generiert aus " + fasta_file +  ":"
        if (rf_flag):
            print "fuer Reading Frame Nr. " + repr(i)
        print "Alphabet: " + repr(nucls)
        print "Zustaende: " + repr(nucl_pairs)
        print "Transitions-Matrix: " + repr(trans_m_rf) + "\n"
    return trans_m

# calculates the log-likelihood for all positions in the test_parts
def calc_log_likelihoods(test_parts, genes, ncregions):
    log_likelihoods = []
    for window in test_parts:
        log_likelihoods.append(calc_log_likelihood(window,genes,ncregions))
    return log_likelihoods
    
# calculates the log_likelihood-function at one position
def calc_log_likelihood(window,genes,ncregions):
    ratio = 0
    for i in range(len(window)-2):
        row = nucl_pairs.index(window[i]+window[i+1])
        col = nucls.index(window[i+2])
        ratio = ratio + math.log(genes[row][col]/ncregions[row][col])
    return ratio

# returns all parts of the test_sequence of size w_size
def get_test_parts(test_seq, w_size):
    test_parts = []
    for i in range(len(test_seq)-w_size+1):
        test_parts.append(test_seq[i:i+w_size])
    return test_parts
    
if __name__ == "__main__":
    # get Transition-Matrix for genes and ncregions
    genes_trans = get_trans("y_genes.txt", 1)
    ncregions_trans = get_trans("y_ncregions.txt", 0)[0]

    # For every window-size and for every reading frame:
    # calculate log likelihood-Values per window
    # attention: very slow if we have several window_sizes
    test_seq = list(SeqIO.parse(open("test.txt"),'fasta'))[0].seq
    #w_sizes = [25,50,100,500,1000,2000]
    w_sizes = [50,100]
    log_likelihoods = []
    for w_size in w_sizes:
        print "status: " + repr(w_size)
        test_parts = get_test_parts(test_seq,w_size)
        log_likelihoods_line = []
        for genes in genes_trans:
            log_likelihoods2  = calc_log_likelihoods(test_parts,genes,ncregions_trans)
            log_likelihoods_line.append(log_likelihoods2)
        log_likelihoods.append(log_likelihoods_line)
    # Result: log_likelihoods = nested Matrix of the following format: 
    # log_likelihoods[window_size_index][reading_frame_index}[window_position]
    
    predictions = []
    for i in range(len(w_sizes)):
        predictions_line = []
        greater = ''.join(['1' if item > 0 else '0' for item in log_likelihoods[i][0]])
        # TODO: predictions berechnen
        predictions_line.append(greater)
        predictions.append(predictions_line)
    out_file = open("Predictions.dat",'w')
    for i in range(len(w_sizes)):
        out_file.write("Predictions fuer Window-Length " + repr(w_sizes[i]) + ":\n")
        out_file.writelines(predictions[i])
    out_file.close()
    
    # Plot results: 
    # one subplot per window-size
    f, axarr = plt.subplots(len(w_sizes))
    for i in range(len(w_sizes)):
        axarr[i].plot(log_likelihoods[i][0], color='r', label="RF 1")
        axarr[i].plot(log_likelihoods[i][1],color='b', label="RF 2")
        axarr[i].plot(log_likelihoods[i][2],color='g', label="RF 3")
        axarr[i].set_title('Window-Size: ' + repr(w_sizes[i]))
        axarr[i].legend()
        axarr[i].set_xlabel('position')
        axarr[i].set_ylabel('Log-Likelihood-Ratio')
    plt.savefig('Burtscher_Deisel_Ueb6_Ex3.png')
    plt.show()    
    
