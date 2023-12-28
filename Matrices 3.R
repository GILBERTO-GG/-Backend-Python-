library(R.utils)
rm(list = ls())
cat("\014")

A <- matrix(data = c(1,2,3,4,5,6), nrow = 3, ncol = 2, byrow = TRUE)

for(j in 1:ncol(A)){
  for (i in 1:nrow(A)) {
    print(A[i,j])
  }
}