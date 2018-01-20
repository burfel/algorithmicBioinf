# Using Python 2.7

import random

def generateDNAs(nr, len, kumulProbs):
    DNAs = []
    for i in range(nr):
        DNAs.append(generateDNA(len, kumulProbs))
    return DNAs

def generateDNA(len, kumulProbs):
    DNA = []
    for i in range(len):
        DNA.append(generateNukleotide(random.random(), kumulProbs))
    return ''.join(DNA)
    
def generateNukleotide(rand,kumulProbs):
    nukleotides = ['A','C','G','T']
    return [nukleotides[i] for i in range(len(kumulProbs)) \
        if kumulProbs[i] >= rand][0]
    
def countInSequences(DNA,DNAs):
    counts = 0
    for seq in DNAs:
        counts = counts + seq.count(DNA)
    return counts

def formatDNAs(DNAs, sequenceName):
    newDNAs = []
    for i in range(len(DNAs)):
        newDNAs.append("> " + sequenceName + " No." + repr(i) + "\n" + DNAs[i] + "\n")
    return  newDNAs
    
    
if __name__ == '__main__':
    probs = [0.3,0.2,0.2,0.3]
    kumulProbs=[]
    for i in range(len(probs)):
        kumulProbs.append(sum(probs[0:i+1]))
    DNAs = generateDNAs(20000,2000,kumulProbs)
    file1 = open('library.fasta','w')
    file1.writelines(formatDNAs(DNAs, "library"))
    file1.close()
    DNA = generateDNAs(1,200,kumulProbs)
    file2 = open('query.fasta','w')
    file2.writelines(formatDNAs(DNA,"query"))
    file2.close()
    print "count of the query sequence in the library sequences: " \
        + repr(countInSequences(DNA[0],DNAs))