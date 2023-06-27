library(quanteda)
library(ggplot2)
require(quanteda.textmodels)
require(quanteda.textplots)
library(stringr)

#rm(list = ls())
 
#Function to read text from file
read_text <- function(file_path) {
  text <- readLines(file_path)
  return(text)
}

setwd('C:/Ritoban/IIMK/Spyder Projects/Wordcloud/outtxtmthprocomb2')

#Get a list of all the parties----
parties <- list.files(recursive = FALSE)

#Initializations----
preprocessed_text = list()
no_of_files = list()
count = 1
j = 1
#Read all the cleaned .TXT----
for(party in parties){
  files <-  list.files(party)
  no_of_files[j] <- length(files)
  j = j+1
  
  for(file in files){
    preprocessed_text[count] <-  read_text(paste0(party,'/',file))
    count = count + 1
  }

}

#List of folders and their number of files----
names(no_of_files) <- parties
no_of_files

#Creating the corpus----
corpus <- corpus(c(unlist(preprocessed_text[1:2])))

# Create a document-feature matrix
dfm <- dfm(corpus)
print('created dfm')

# Apply Wordfish algorithm
wordfish_results <- textmodel_wordfish(dfm)
print('applied wf')

positions <- data.frame(Article = c("BJP m1", "BJP m2", "BJP m3", "BJP m4", "BJP m5", "BJP m6", "BJP m7", "BJP m8", "BJP m9", "BJP m10", "BJP m11", "BJP m12", "BJP m13", "BJP m14", "BJP m15", "BJP m16", "BJP m17", "BJP m18", "BJP m19", "BJP m20", "BJP m21", "BJP m22", "BJP m23", "BJP m24", "BJP m25","COMBINED m1", "COMBINED m2", "COMBINED m3", "COMBINED m4", "COMBINED m5", "COMBINED m6", "COMBINED m7", "COMBINED m8", "COMBINED m9", "COMBINED m10", "COMBINED m11", "COMBINED m12", "COMBINED m13", "COMBINED m14", "COMBINED m15", "COMBINED m16", "COMBINED m17", "COMBINED m18", "COMBINED m19", "COMBINED m20","COMBINED m21", "COMBINED m22", "COMBINED m23", "COMBINED m24", "COMBINED m25"), Position = wordfish_results$theta)#, "OTHER m6", "OTHER m7", "OTHER m8", "OTHER m9", "OTHER m10", "OTHER m11", "OTHER m12", "OTHER m13", "OTHER m14", "OTHER m15", "OTHER m16", "OTHER m17", "OTHER m18", "OTHER m19", "OTHER m20", "OTHER m21", "OTHER m22", "OTHER m23", "OTHER m24", "OTHER m25"), Position = wordfish_results$theta)
positions <- data.frame(Article = c("BJP m1", "BJP m2", "BJP m3", "BJP m4"), Position = wordfish_results$theta)#, "OTHER m6", "OTHER m7", "OTHER m8", "OTHER m9", "OTHER m10", "OTHER m11", "OTHER m12", "OTHER m13", "OTHER m14", "OTHER m15", "OTHER m16", "OTHER m17", "OTHER m18", "OTHER m19", "OTHER m20", "OTHER m21", "OTHER m22", "OTHER m23", "OTHER m24", "OTHER m25"), Position = wordfish_results$theta)
positions <- data.frame(Article = c("BJP m1", "BJP m2"), Position = wordfish_results$theta)#, "OTHER m6", "OTHER m7", "OTHER m8", "OTHER m9", "OTHER m10", "OTHER m11", "OTHER m12", "OTHER m13", "OTHER m14", "OTHER m15", "OTHER m16", "OTHER m17", "OTHER m18", "OTHER m19", "OTHER m20", "OTHER m21", "OTHER m22", "OTHER m23", "OTHER m24", "OTHER m25"), Position = wordfish_results$theta)

# Print ideological positions
print(positions)

summary(wordfish_results)
textplot_scale1d(wordfish_results$se)


names <- c('n1','n2','n3','n4')
rownames(dfm) <- names


