library(arules)

#filename = 'C:/Users/Matthew Martin/Documents/School/Data Mining/Project/store_data.csv'
#X = read.csv(filename)
#X = readLines(filename)
D= read.table('C:/Users/Matthew Martin/Documents/School/Data Mining/Project/input.txt',header = TRUE)
D = as.matrix(D)
n = dim(D)[1]
is <- apriori(D, parameter = list(support= 0.1, target="frequent"))
d = length(is)
DD = matrix(0,n,dd)
for( i in 1:d){
  l = as(is[i]@items,"list")[[1]]
  print(l)
}
