library(R.utils)
rm(list=ls())
cat("\014")

data <- islands
continent <- c(data["North America"], data["South America"])

pie(continent, labels = names(continent), col = c("blue", "green"), main = "Distribution of 
    the American continent")

legend(x = "bottomright", legend = names(continent), col = c("blue", "green"), 
       pch = c(15, 15))