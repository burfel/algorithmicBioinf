
## Uebung 5
## Aufgabe 3


import random

# returns the nucleotide given a number between [0,1)
def getNucleotide(random_number=0):
	bases = ['A', 'C', 'G', 'T']
	if random_number <= 0.3: 
		return bases[0]
	if random_number >= 0.3 and random_number < 0.6:
		return bases[3]
	if random_number >= 0.6 and random_number < 0.8:
		return bases[1]
	if random_number >= 0.8:
		return bases[2]

# produces a random sequence of given length
def make_sequence(seqlength=100):
	a = []
	sequence = []
	for i in range(seqlength):
		nuc = getNucleotide(random.random())
		sequence.append(nuc)
	#print sequence
	return sequence

# generates 20000 sequences of length 2000
def main():
	sequences = []
	new_seq = []
	sequence = []
	for i in range(20000):
		new_seq = ''.join(make_sequence(2000))
		sequences.append(new_seq)
	#print '\n'.join(sequences)
	file = open('sequences.fasta','w')
	file.write('\n'.join(sequences))
	file.close() 
	
if __name__ == "__main__":
	main()
	
