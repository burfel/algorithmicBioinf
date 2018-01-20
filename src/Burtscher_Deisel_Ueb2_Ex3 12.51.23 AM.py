import random
import matplotlib.pyplot as plt
import numpy

# generates a random DNA of length 'length'
def generate_DNA(length):
  DNA = list('')
  Bases = ['A','C','G','T']
  for x in range(length):
    i = random.randint(0,3);
    DNA.append(Bases[i])
  return DNA

# mutates the DNA n times and returns the list of mutated DNAs
def mutate_DNA(DNA,n):
  Bases = ['A','C','G','T']
  DNAs = []
  DNAs.append(DNA[:])
  for x in range(n):
    i = random.randint(0,len(DNA)-1)
    j = random.randint(0,3)
    DNA[i] = Bases[j]
    DNAs.append(DNA[:])
  return DNAs

# Plots the course of the hamming distances/sequence length and the jukes 
# cantor correction of the generations of mutated DNA sequences given by the 
# list DNA. The plot is saved in the file Burtscher_Deisel_Ueb2_Ex3.png.
def plot_mutations2(DNAs):
  plt.close("all")
  distances = []
  jukes_cantor = []
  first = DNAs[0]
  for x in range(len(DNAs)):
    distances.append(1.0*hamming_distance(first,DNAs[x])/len(first))
    jukes_cantor.append((jukes_cantor_correction(\
        hamming_distance(first,DNAs[x]),len(first))))
  plt.figure()
  plt.plot(range(len(distances)),distances)
  plt.plot(range(len(distances)),jukes_cantor)
  plt.xlabel('Generation')
  plt.ylabel('Hamming-Distance/Sequence-Length (blue)\nand\nJukes Cantor Correction (green)')
  title = 'Mutation of DNA (length=' + repr(len(first)) + ') after ' \
    + repr(len(DNAs) - 1) + ' Generations'
  plt.title(title)
  plt.savefig('Burtscher_Deisel_Ueb2_Ex3.png')
  plt.show()

# Auxiliary function:
# Naively calculates the hamming distance of the lists s1 and s2
def hamming_distance(s1,s2):
  distance = 0
  for i in range(len(s1)):
    distance = distance + int(s1[i] != s2[i])
  return distance

# Auxiliary function:
# Calculates the jukes cantor correction given the hamming distance and the 
# sequence length
def jukes_cantor_correction(hamming,length):
    if (1.0*hamming/length) < 0.75:
        d = -3.0/4.0 * numpy.log(1-(4.0/3*hamming/length))
    else:
        d = None
    return d
  
if __name__ == '__main__':
  DNAs = mutate_DNA(generate_DNA(1000),10000)
  plot_mutations2(DNAs)

