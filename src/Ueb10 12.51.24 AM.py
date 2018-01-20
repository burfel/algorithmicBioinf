
import sys, scipy, numpy

#Aufgabe 1

stringmatrix = []
with open(sys.argv[1]) as f:
	#skip header
	next(f)  
	for line in f:
		stringmatrix.append(line.split())
#delete first column
stringmatrix = scipy.delete(stringmatrix, 0, 1)  
p = len(stringmatrix[1])
n = len(stringmatrix)
matrix = [[0 for x in xrange(p)] for x in xrange(n)]
for i in range(n):
	for j in range(p):
		floats = float(stringmatrix[i][j])
		matrix[i][j] = floats
		
#Aufgabe 2

def sorting(matrix):
	sortmatrix = [[0 for x in xrange(n)] for x in xrange(p)]
	index = [[0 for x in xrange(n)] for x in xrange(p)]
	for j in range(p):
		sortmatrix[j] = [matrix[i][j] for i in range(len(matrix))]
		index[j]=([i[0] for i in sorted(enumerate(sortmatrix[j]), key = lambda x:x[1])])
		sortmatrix[j] = sorted(sortmatrix[j])
	sortedmatrix = [[sortmatrix[i][j] for i in range(len(sortmatrix))] for j in range(len(sortmatrix[0]))]
	indexed = [[index[i][j] for i in range(len(index))] for j in range(len(index[0]))]
	return sortedmatrix, indexed

(mmatrix, index) = sorting(matrix)
	
def mean(matrix):
    n = len(matrix)
    p = len(matrix[1])
    for i in range(n):
        mue = sum(matrix[i])/float(p)
        for j in range(p):
            matrix[i][j] = mue
    return matrix

midmatrix = mean(mmatrix)

def backsort(matrix, index):
    endmatrix = [[0 for x in xrange(p)] for x in xrange(n)]
    for j in range(p):
        for i in range(n):
            endmatrix[index[i][j]][j] = matrix[i][j]
    return endmatrix

endmatrix = backsort(matrix,index)
stringmatrix2 = str(endmatrix)

#Aufgabe 3

outFile = sys.argv[2]
with open(outFile,'w') as o:
	o.write(stringmatrix2)