#rm(list=ls())
library(quanteda)
require(quanteda.textmodels)

source <- "C:/Ritoban/IIMK/Newspaper Articles/Wordfish Data"
#Choose Topic-------------------------------------------------------------------
topic <- 'Covid'
source <- paste0(source,'/',topic)
#-------------------------------------------------------------------------------
destination <- paste0(source,'/',topic,'/monthly')
  
months <- paste0(rep('m',26),seq(1,26))
parties <- c('bjp','cong','regional')

#Create the folders for the 26 months----
folder_path <- paste0(source,'/Monthly')
for(month in months){
  path <- paste0(folder_path,'/',month)
  dir.create(path)
}
rm(path)
#----

#Rename and move files from party-wise to month wise----
parties <- c('bjp','cong','regional')
destination <- paste0("C:/Ritoban/IIMK/Newspaper Articles/Wordfish Data/",topic,'/Monthly')
months <- paste0('m',seq(1,26))
for(party in parties){
  party_source <- paste0(source,'/',party)
  
  for(month in months){
    
    month_source <- paste0(party_source,'/',month)
    
    files <- list.files(month_source)
    
    for(file in files){
      file_path <- paste0(month_source,'/',file)
      dest_file_path <- paste0(destination,'/',month)
      file.copy(file_path,dest_file_path)
      
      file.rename(paste0(dest_file_path,'/',file),paste0(dest_file_path,'/',party,'-',file))
    }
  }
}
#----

#Function to read text from .TXT----
read_text <- function(file_path) {
  text <- readLines(file_path)
  return(text)
}
#----------

#Choose Month-------------------------------------------------------------------
month <- 'm1'
#-------------------------------------------------------------------------------
source_m <- paste0(source,'/monthly/',month)
files_m <- list.files(source_m)

#Read the .TXT files for chosen month----
prepped_text <- list()
i <- 1
for(file in files_m){
  prepped_text[i] <- read_text(paste0(source_m,'/',file))
  i <- i + 1
}
rm(list = c("i","file"))
#----

#Create the DFM----
corpus <- corpus(c(unlist(prepped_text)))
dfm <- dfm(corpus)

#Rename dfm rows
rownames(dfm) <- files_m

#dfm <- dfm_trim(dfm, min_termfreq = 20, min_docfreq = 5)
dfm_viewer <- as.matrix(dfm)
dfm_viewer <- as.data.frame(dfm_viewer)
View(dfm_viewer)
#----


#Apply wordfish algorithm----
wordfish_results <- textmodel_wordfish(dfm, sparse = TRUE)
#---

#Print wordfish results----
se <- list(summary(wordfish_results)$estimated.document.positions['se'])

positions <- data.frame(position = wordfish_results$theta,se = se)

#positions$Article <- gsub("\\.txt$", "", positions$Article)
View(positions)
  
#write.csv(positions,paste0(source,'/','Monthly Wordfish/ALL - m1.csv'),row.names = FALSE)
#----


#Mean Calculations----
months <- c('m1','m2','m3')
a <- 0
b <- 0
c <- 0
d <- 0
read_source <- paste0(source,'/','Monthly Wordfish/ALL - ')
i <- 1
for(month in months){
  path <- paste0(read_source,month,'.csv')
  df <- read.csv(path)
  posit <- df['position']
  a <- c(a,mean(posit[1:2063,]))
  b <- c(b,mean(posit[2064:2314,]))
  c <- c(c,mean(posit[2315:dim(posit)[1],]))
  d <- c(d,mean(posit[2064:dim(posit)[1],]))
  i <- i+1
}
rm(list=c("i","read_source","path","df","posit"))
mean_all2 <- data.frame(Month = months, BJP = a[-1], Congress = b[-1], Regional = c[-1], Others = d[-1])
View(mean_all2)
#----
