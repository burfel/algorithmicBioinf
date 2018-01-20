import random
import matplotlib.pyplot as plt

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

# Plots the course of the hamming distances of the generations of 
# mutated DNA sequences given by the list DNA. The plot is saved in 
# the file U1A1-plot.png.
def plot_mutations(DNAs):
  plt.close("all")
  distances = []
  first = DNAs[0]
  for x in range(len(DNAs)):
    distances.append(hamming_distance(first,DNAs[x]))
  plt.figure()
  plt.plot(range(len(distances)),distances)
  plt.xlabel('Generation')
  plt.ylabel('Hamming-Distance')
  title = 'Mutation of DNA (length=' + repr(len(first)) + ') after ' \
    + repr(len(DNAs) - 1) + ' Generations'
  plt.title(title)
  plt.savefig('Burtscher_Deisel_Ueb1_Ex1.png')
  plt.show()

# Auxiliary function:
# Naively calculates the hamming distance of the lists s1 and s2
def hamming_distance(s1,s2):
  distance = 0
  for i in range(len(s1)):
    distance = distance + int(s1[i] != s2[i])
  return distance

# Extra function:
# Formats DNA (given as a list of characters) as a string
def DNA_to_string(DNA):
  string = ''
  for i in DNA:
      string = string+i
  return string
  
# Extra function:
# Prints every DNA out of the list DNAs formattet as a string
def print_DNAs(DNAs):
  for DNA in DNAs: print DNA_to_string(DNA)
  
# Extra function:
# Calculates the average of the hamming distances of the first and 
# last generations (given by the list DNAs) in n iterations
def average_end_hd(DNAs,n):
  sum = 0
  for i in range(n):
    sum += hamming_distance(DNAs[0],DNAs[-1])
    print i
  return (sum/amount)
  
  
if __name__ == '__main__':
  DNAs = mutate_DNA(generate_DNA(1000),10000)
  plot_mutations(DNAs)

