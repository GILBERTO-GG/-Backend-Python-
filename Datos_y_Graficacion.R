library(R.utils)
rm(list=ls())
cat("\014")

data <- iris

plot(x = data$Petal.Length, y = data$Petal.Width, xlab = "Length [cm]", ylab = "width [cm]",
  main = "Petals from the IRIS dataset", col = c("black", "brown", "red") [as.integer(data$Species)],
  pch = c(0, 1, 2))
legend(x = "bottomright", legend = c("setosa", "versicolor", "virginica"), col = c("black", "brown", "red"),
       pch = c(0, 1, 2))
grid(nx = NULL, ny = NULL, col = "lightgray", lty = "dotted")

