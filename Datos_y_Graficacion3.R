library(R.utils)
rm(list=ls())
cat("\014")

data <- precip
data <- data[1:10]

barplot(data, width = 1, xlab = "Cities", ylab = "Precipitation [inches]", main = "Average
        rainfall in 10 cities from US and Puerto Rico", names.arg = names(data),
        col = "dodgerblue1") 