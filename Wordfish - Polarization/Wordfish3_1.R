rm(list=ls())
library(quanteda)
require(quanteda.textmodels)

#Function to read .TXT files for chosen month----

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
#----

monthly_wordfish <- function(source,parties,months,min_term=1,min_doc=1) {
  party_wise <- list()
  
  for(party in parties){
    
    source_p <- paste0(source,'/',party)
    
    monthly <- list()
    for(month in months){
      
      source_m <- paste0(source_p,'/',month)
      prepped_text <- read_all(source_m)$texts
      
      #Create the DFM----
      corpus <- corpus(c(unlist(prepped_text)))
      dfm <- dfm(corpus)
      
      #Rename dfm rows
      rownames <- read_all(source_m)$names
      rownames(dfm) <- rownames
      
      #Trim the dfm
      dfm <- dfm_trim(dfm, min_termfreq = min_term, min_docfreq = min_doc)
      
      #Apply wordfish algorithm----
      wordfish_results <- textmodel_wordfish(dfm, sparse = TRUE)
      
      #Aggregate the wordfish results----
      se <- list(summary(wordfish_results)$estimated.document.positions['se'])
      
      positions <- data.frame(position = wordfish_results$theta,se = se)
      
      #positions$Article <- gsub("\\.txt$", "", positions$Article)
      
      monthly[[month]] <- positions
    }
    party_wise[[party]] <- monthly
  }
  
  return(party_wise)
}


#Call-------------------------------
topic <- 'Covid'
source <- paste0("C:/Ritoban/IIMK/Newspaper Articles/Wordfish Data/",topic)
parties <- c('bjp','cong','regional')
months <- c('m1','m2','m3')
min_term <- 20
min_doc <- 5
df <- monthly_wordfish(source,parties,months,min_term,min_doc)
#mean(df1$cong$m1$position)

#write.csv(df1$cong$m1,paste0(source,'/','Monthly Wordfish/Cong - m1.csv'),row.names = FALSE)

#Dataframe for mean----
means <- list()
for(party in parties){
  i <- 1
  for(month in months){
    means[[party]][i] <- mean(df[[party]][[month]]$position)
    i <- i+1
  }
}
mean <- data.frame(Months = c('m1','m2','m3'),BJP = means$bjp,Congress = means$cong,Regional = means$regional)
#----

#Save Files----
for(party in parties){
  for(month in months){
    file_name <- paste0(party," - ",month)
    write.csv(df[[party]][[month]],paste0(source,'/','Monthly Wordfish/',file_name,'.csv'),row.names = TRUE)

  }
}

View(mean)
