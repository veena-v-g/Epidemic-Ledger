install.packages("ggmap")
install.packages("dplyr")
install.packages("tidyr")
install.packages("xlsx")

library(ggmap)
library(tidyr)
library(dplyr)
library(xlsx)


dataset <- "C:\\Users\\Anita\\Documents\\Fall_2018\\hackseq18\\cdc_zika.csv"
dataset.df <- read.csv(dataset, stringsAsFactors = F)


##################################Geocode Data#############################################################################
#1. Clean data
#set locations to the format: sublocation, country
#2. Geocode data with ggmap
#https://www.jessesadler.com/post/geocoding-with-r/
#3. Map

grabUniqueLocations <- function(dataset.df) {
  return(unique(dataset.df))
}

grabCoor <- function(dataset) {
  locations_df <- mutate_geocode(dataset, location, source="dsk")
  return(locations_df)
}


dataset.df$location <- gsub( "-", ",", dataset.df$location)
dataset.df$location <- gsub( "_", " ", dataset.df$location)

uniqueLocAnnotated <- data.frame(stringsAsFactors = F)
uniqueLocAnnotated <- grabUniqueLocations(dataset.df$location)
uniqueLocAnnotated <- as.data.frame(uniqueLocAnnotated, stringsAsFactors = F)
colnames(uniqueLocAnnotated)[colnames(uniqueLocAnnotated) == "uniqueLocAnnotated"] <- "location" #rename the column


#grab the lat and lon for each location
location.df <- grabCoor(uniqueLocAnnotated)
write.xlsx(location.df, file = gsub(".csv", "_geocoded.xlsx",dataset), row.names = F, col.names = T)



warnings()

