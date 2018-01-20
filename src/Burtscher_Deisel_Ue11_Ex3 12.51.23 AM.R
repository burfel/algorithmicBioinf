# A3.2
mydata = matrix(c(c(125,125),c(375,375)),2)
chisq.test(mydata)


# A3.3/4
pvalues <- c(chisq.test(mydata)$p.value)
while (mydata[2,1] > 0) {
  mydata[1,1] = mydata[1,1] + 1
  mydata[1,2] = mydata[1,2] - 1
  mydata[2,1] = mydata[2,1] - 1
  mydata[2,2] = mydata[2,2] + 1
  pvalues <- c(pvalues,chisq.test(mydata)$p.value)
}
plot(pvalues)