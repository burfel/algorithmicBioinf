# Using Python 2.7

import numpy
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import random
    
if __name__ == '__main__':
    file = open('scores.txt','r')
    stringList = file.readlines()[2:-7]
    intList = [int(filter(None,line.split(' '))[4]) for line in stringList]
    intListMaxima = []
    for i in range(len(intList)/2):
        intListMaxima.append(max(intList[i*2],intList[i*2+1]))
    hist,binEdges = numpy.histogram(intListMaxima,\
        range = (min(intListMaxima),max(intListMaxima)),\
        bins = max(intListMaxima)-min(intListMaxima)+1)
    normedHist = [elem*100.0/len(intListMaxima) for elem in hist]
    mean = sum(intListMaxima)/float(len(intListMaxima))
    intArray = numpy.array(intListMaxima)
    sigma = intArray.std()
    print "Mittelwert = " + repr(mean)
    print "Standardabweichung = " + repr(sigma)
    norm = mlab.normpdf(numpy.array(range(min(intListMaxima),\
        max(intListMaxima)+1)),mean,sigma)
    normTimes = [elem*100 for elem in norm]
    plt.figure()
    plt.plot(range(min(intListMaxima),max(intListMaxima)+1),normedHist,\
        label="Haeufigkeit der Scores")
    plt.plot(range(min(intListMaxima),max(intListMaxima)+1),normTimes,\
        label="Normalverteilung mit \ngleichen Parametern")
    plt.legend()
    plt.xlabel('Score')
    plt.ylabel('Percent of all Sequences')
    plt.title("Histogram over the Scores of the Sequences")
    plt.savefig('Burtscher_Deisel_Ueb5_Ex3_4.png')
    plt.show()

