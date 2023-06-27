#rm(list = ls())
#rm(list = 'grouped_df')
library(dplyr)

df <- read.csv("C:/Ritoban/IIMK/Newspaper Articles/Wordfish Data/Covid/Monthly Wordfish/ALL - m1.csv")

mean(df[1:2063,2])
mean(df[2064:2314,2])
mean(df[2315:3006,2])
mean(df[,2])

bjp_mean <- mean(positions[,2])
congress_mean <- mean(positions[,2])
regional_mean <- mean(positions[,2])
