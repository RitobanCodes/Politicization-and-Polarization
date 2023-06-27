rm(list=ls())
require(quanteda.textplots)
library(quanteda)
require(quanteda.textmodels)

start_time <- Sys.time()
read_text <- function(file_path) {
  text <- readLines(file_path)
  return(text)
}

read_all <- function(source){
  files <- list.files(source)
  prepped_text <- list()
  i <- 1
  for(file in files){
    prepped_text[i] <- read_text(paste0(source,'/',file))
    i <- i + 1
  }
  
  results <- list(texts = prepped_text,names = files)
  return(results)
}

#-------------------------------------------------------------------------------
topic <- 'Covid'
source <- paste0("C:/Ritoban/IIMK/Newspaper Articles/Wordfish Data/",topic)
parties <- c('bjp','cong','regional')
months <- paste0('m',seq(1,26))
#-------------------------------------------------------------------------------
#
monthly_wordfish <- list(0)
for(month in months){
  source_m <- paste0(source,'/Monthly/',month)
  
  #Read all the documents in a list and obtain the document names
  prepped_text <- read_all(source_m)$texts
  names <- read_all(source_m)$names
  
  #Create the DFM----
  corpus <- corpus(c(unlist(prepped_text)))
  dfm <- dfm(corpus)
  
  if(month == 'm16'){
    dfm <- dfm_trim(dfm, min_termfreq = 30, min_docfreq = 6)
  }else{
    dfm <- dfm_trim(dfm, min_termfreq = 20, min_docfreq = 5)
  }
    
  
  #Rename dfm rows
  rownames(dfm) <- names
  
  #Apply wordfish algorithm----
  
  wordfish_results <- textmodel_wordfish(dfm, sparse = TRUE)
  #textplot_scale1d(wordfish_results, margin = "features")
  #plt.title(month)
  #Organize wordfish results----
  
  se <- list(summary(wordfish_results)$estimated.document.positions['se'])
  positions <- data.frame(position = wordfish_results$theta,se = se)
  
  monthly_wordfish[[month]] <- positions
}
end_time <- Sys.time()
print("Time Taken:")
(end_time-start_time)

for(month in months){
  write.csv(monthly_wordfish[[month]],paste0(source,'/Monthly Wordfish/All - ',month,'.csv'))
}