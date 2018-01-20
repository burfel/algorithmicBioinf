# Using Python 2.7 
import sys, math, time, os.path


def readExpressionMatrix(infile):
    with open(infile) as file:
        content = file.readlines()
    content = [line.strip("\n").split("\t") for line in content]
    line0 = content[0]
    column0 = []
    content = content[1:]
    for line in content:
        column0.append(line[0])
        del line[0]
    result = [[float(element) for element in line] for line in content]
    return result, line0, column0

def quantileNormalization(exprMatrix, outfile):
    if os.path.isfile(outfile):
	  resultMatrix, line0, column0 = readExpressionMatrix(outfile)
    else: 
	sortedExprMatrixT = map(lambda *row: list(row), *exprMatrix)
	for i in range(len(sortedExprMatrixT)):
	    sortedExprMatrixT[i].sort()
	sortedExprMatrix = map(lambda *row: list(row), *sortedExprMatrixT)
	medians = [median(line) for line in sortedExprMatrix]
	resultMatrix = exprMatrix
	# Achtung: sehr ineffizient hier!
	ts = time.time()
	for i in range(len(exprMatrix)):
	    if i % 100 == 0:
		print "Fortschritt: " + repr(i) + " von " + repr(len(exprMatrix))
		print (time.time() - ts)
		ts = time.time()
	    for j in range(len(exprMatrix[i])):
		for i2 in range(len(sortedExprMatrix)):
		    if exprMatrix[i][j] == sortedExprMatrix[i2][j]:
			resultMatrix[i2][j] = medians[i]
    return resultMatrix

def writeExpressionMatrix(outfile, expressionMatrix, line0, column0):
    for i in range(len(expressionMatrix)):
        expressionMatrix[i] = [column0[i]] + expressionMatrix[i]
    expressionMatrix = expressionMatrix
    result = []
    for line in expressionMatrix:
        resLine = [line[0]] + [repr(element) for element in line[1:]]
        result.append("\t".join(resLine) + "\n")
    with open(outfile,"w") as file:
        file.write("\t".join(line0) + "\n")
        file.writelines(result)
    
def median(list):
    if len(list) % 2 == 1:
        return list[(len(list) + 1)/2]
    else:
        return (list[len(list)/2] + list[len(list)/2 + 1])/2
      
def tstatistic(exprMatrix, line0):
    nIndex = []
    tIndex = []
    for element in line0:
	if element[0] == "G":
	    nIndex.append(line0.index(element)+1)
	else:
	    tIndex.append(line0.index(element)+1)
    T = []
    for line in exprMatrix:
	listn = [line[i] for i in nIndex]
	listt = [line[i] for i in tIndex]
	nn = len(listn)
	nt = len(listt)
	Xn = 1.0*sum(listn)/nn 
	Xt = 1.0*sum(listt)/nt 
	an = 1.0/(nn-1) * sum([(element - Xn)**2 for element in listn])
	at = 1.0/(nt-1) * sum([(element - Xt)**2 for element in listt])
	S = math.sqrt((((nn-1)*an*an) + ((nt-1)*at*at))/(nn+nt-2))
	T.append(S)
    return T
  
def topTen(matrix,column0):
    sortedArray = sorted(range(len(matrix)), key=lambda i:matrix[i]) 
    topTen = []
    topTenIndices = []
    for index in sortedArray[-1:-11:-1]:
	topTen.append(column0[index])
        topTenIndices.append(index)
    return topTenIndices, topTen
  
if __name__ == "__main__":
    if len(sys.argv) > 1:
        infile = sys.argv[1]
        if len(sys.argv) > 2:
            outfile = sys.argv[2]
        else:
            outfile = "expr_CEL_out.txt"
    else:
        infile = "expr_CEL.txt"
        outfile = "expr_CEL_out.txt"

    # A2
    exprMatrix, line0, column0 = readExpressionMatrix(infile)
    quantileNormMatrix = quantileNormalization(exprMatrix, outfile)
    writeExpressionMatrix(outfile, quantileNormMatrix, line0, column0)
    
    # A3
    tstatisticNorm = tstatistic(quantileNormMatrix, line0)
    topTenIndices, topTen = topTen(tstatisticNorm, column0)
    print "top Ten differentiell exprimierte Gene: " + repr(topTen)   
    print "Indices dazu: " + repr(topTenIndices)
