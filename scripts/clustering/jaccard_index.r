#This script takes a .csv file and output a dendrogram of k clusters
#In the console, just pass cardsort the path to the file and the number of clusters you want
#For example, cardsort('/Data/card_sort.csv', 5)

compare <- function(x1, x2) {
      x3 <- x1 + x2
      ints <- sum(x3 > 1)
      uno <- sum(x3 > 0)
      return (ints / uno)
}

getJaccard <- function(data) {
  	l = length(data[1,])
  	jmatrix <- matrix(nrow=l,ncol=l)
  	for (i in 1:l) {
  		for (j in i:l) {
  			s <- compare(data[i], data[,j])
  			jmatrix[i,j] <- s
  			jmatrix[j,i] <- s
  		}
  		}
  	return (jmatrix)
}

cardsort <- function(filename, blocks) {
      filedata <- read.csv(filename, header=T, sep=",", row.names=NULL)
      data <- getJaccard(filedata)
      colnames(data) <- colnames(filedata)
      hc <- hclust(dist(t(data)), method="ward.D")
      hc$labels <- colnames(data)
      plot(as.dendrogram(hc),horiz=F)
      rect.hclust(hc, k=blocks, border="#0078D6")
}
