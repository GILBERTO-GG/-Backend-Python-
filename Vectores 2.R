library(R.utils)

rm(list=ls())
cat("\014")

vector <- 1:100

for(i in 1:length(vector)){
  if(i%%2 == 0){
    printf("vector[%d] = %d\n", i, vector[i])
  }
}
