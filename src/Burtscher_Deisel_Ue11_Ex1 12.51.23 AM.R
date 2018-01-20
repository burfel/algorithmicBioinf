# A1.2
mydata = read.table("http://www.molgen.mpg.de/Algorithmische-Bioinformatik-WS1415/u11/Golub_train")

# A1.3
mydata <- mydata[-1,]
mydata <- as.matrix(sapply(mydata, as.numeric)) 
mydata <- log(mydata)
for (i in 2:nrow(mydata)){
  rowmean <-mean(mydata[i,])
  for (j in 1:ncol(mydata)){
    mydata[i,j] <- mydata[i,j] - rowmean
  }
}
boxplot(mydata, outline=FALSE)

# A1.4
eigen <- eigen(cov(t(mydata)))

# A1.5
ffc <- c(eigen$values[1:5])
print(ffc)
all <- sum(eigen$values)
print((eigen$values[1])/all) # what first component explains
print((sum(ffc)/all)) # what first five components explain



