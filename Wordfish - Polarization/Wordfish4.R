#rm(list=ls())
#
source <- "C:/Ritoban/IIMK/Newspaper Articles/Wordfish Data"
#Choose Topic-------------------------------------------------------------------
topic <- 'Covid'
#-------------------------------------------------------------------------------
destination <- paste0(source,'/',topic,'/monthly')
  
source <- paste0(source,'/',topic)
months <- paste0(rep('m',26),seq(1,26))
parties <- c('bjp','cong','regional')

#Create the folders for the 26 months----
folder_path <- paste0(source,'/monthly')
for(month in months){
  path <- paste0(folder_path,'/',month)
  dir.create(path)
}
rm(path)
#----

#Rename and move files from party-wise to month wise----
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



