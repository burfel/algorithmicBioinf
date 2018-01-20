# A1.1
mydata = read.table("expr_CEL_out.txt")

mydataG <- numeric()
mydataK <- numeric()
myIndex <- c(21011, 21031, 5373, 5372, 5371, 5370, 5369, 5368, 5367, 5378) #TODO


mydataGr <- numeric()
mydataKr <- numeric() 

for(i in 1:nrow(mydata)) {
  Gi <- sum(log2(mydata[i,]$K_18),log2(mydata[i,]$K_19),log2(mydata[i,]$K_21),log2(mydata[i,]$K_22),log2(mydata[i,]$K_23))/5
  Ki <- sum(log2(mydata[i,]$G_20),log2(mydata[i,]$G_24),log2(mydata[i,]$G_25),log2(mydata[i,]$G_26),log2(mydata[i,]$G_27))/5
  mydataG <- c(mydataG,Gi)
  mydataK <- c(mydataK,Ki)
}
for (i in myIndex) {
  Gr <- sum(log2(mydata[i,]$K_18),log2(mydata[i,]$K_19),log2(mydata[i,]$K_21),log2(mydata[i,]$K_22),log2(mydata[i,]$K_23))/5
  Kr <- sum(log2(mydata[i,]$G_20),log2(mydata[i,]$G_24),log2(mydata[i,]$G_25),log2(mydata[i,]$G_26),log2(mydata[i,]$G_27))/5
  mydataGr <- c(mydataGr,Gr)
  mydataKr <- c(mydataKr,Kr)
}

#TODO: mark top ten
smoothScatter(mydataG,mydataK,xlab="log2(G)",ylab="log2(K)")
par(new=TRUE)
points(mydataGr,mydataKr,xlab="",ylab="",col='red')