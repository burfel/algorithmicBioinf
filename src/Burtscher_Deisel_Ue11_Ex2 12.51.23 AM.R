source("http://bioconductor.org/biocLite.R")
biocLite("DESeq")
library("DESeq") 

# A2.1
mydata <- newCountDataSet(read.table("D:/Dropbox/UNI/ALBI/Uebungen/ue11/DESeq_counttable.txt"), c("u","u","t","t"))
print(mydata)

# A2.2
mydata <- estimateSizeFactors(mydata)
sizeFactors(mydata)

# A2.3
mydata <- estimateDispersions(mydata)

# A2.4
result = nbinomTest(mydata,"u","t")
keep <- c()
for (i in 1:nrow(result)){
  #print(result[i,1])
  #print(round(result[i,7], digits = 5))
  if (!is.na(result[i,7])){
    if(round(result[i,7], digits = 5)<0.01){
      keep <- c(keep,i)
    }
  }
}
result <- result[keep,]
uhoch <- c()
for (i in 1:nrow(result)){
  if (result[i,3] > result[i,4]){
    uhoch <- c(uhoch,result[i,1])
  }
}