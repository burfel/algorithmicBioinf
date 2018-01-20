# A1.1
mydata = read.table("expr_CEL.txt")
summary(mydata)
boxplot(mydata)


# A1.2
mydatalog = log2(mydata) 
mydatalogt <- as.data.frame(t(mydatalog))
d <- dist(mydatalogt, method = "euclidean")
fit <- hclust(d, method="complete") 
plot(fit,labels=NULL) 


# A1.3
smoothScatter(mydatalog$G_20,mydatalog$G_25,xlab="log2(G_20)",ylab="log2(G_25)")
smoothScatter(mydatalog$K_18,mydatalog$G_25,xlab="log2(K_18)",ylab="log2(G_25)")


# A1.4
M <- numeric()
A <- numeric()
for(i in 1:nrow(mydata)) {
  K18i <- mydata[i,]$K_18
  G25i <- mydata[i,]$G_25
  M <- c(M,log2(K18i/G25i))
  A <- c(A,0.5*log2(K18i*G25i))
}
smoothScatter(A,M)