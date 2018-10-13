# install.packages("dplyr")
# install.packages("ggmap")
# install.packages("tidyr")
# install.packages("xlsx")

library(dplyr)
library(ggmap)
library(tidyr)
library(xlsx)

#Input: one csv file (*InputFileName.csv*) with a column named location. Each location is formatted Country-City_Name-Additional_Specifications
#Output: 
#a. A xlsx file named *InputFileName_geocodedLocations.xlsx* containing unique locations from the input file and the associated longitude and latitude coordinates.
#b. A csv file name *InputFileName_geocoded.csv* in which the original input data is annotated with longitude and latitude coordinates.
##All text surrounded by *stars* are generic naming conventions

dataset <- "cdc_zika.csv"
dataset.df <- read.csv(dataset, stringsAsFactors = F)


grabUniqueLocations <- function(dataset.df) {
  return(unique(dataset.df))
}

grabCoor <- function(dataset) {
  locations_df <- mutate_geocode(dataset, location, source="dsk")
  return(locations_df)
}

#format the locations
dataset.df$location <- gsub( "-", ",", dataset.df$location)
dataset.df$location <- gsub( "_", " ", dataset.df$location)

#subset the locations to retrieve only unique locations
#ggmap is limited to 2500 queries per day
uniqueLocAnnotated <- data.frame(stringsAsFactors = F)
uniqueLocAnnotated <- grabUniqueLocations(dataset.df$location)
uniqueLocAnnotated <- as.data.frame(uniqueLocAnnotated, stringsAsFactors = F)
colnames(uniqueLocAnnotated)[colnames(uniqueLocAnnotated) == "uniqueLocAnnotated"] <- "location" #rename the column


#grab the lat and lon for each location
location.df <- grabCoor(uniqueLocAnnotated)
print(paste0(nrow(location.df), " coordinate pairs returned"))

write.xlsx(location.df, file = gsub(".csv", "_geocodedLocations.xlsx",dataset), row.names = F, col.names = T)

#merge the lat and lon onto the orignial dataset.df
dataset.df.annotated <- merge.data.frame(dataset.df, location.df, by=c("location"), all.x=T)

#return data format to orignal format
dataset.df.annotated$location <- gsub( ",", "-", dataset.df.annotated$location)
dataset.df.annotated$location <- gsub( " ", "_", dataset.df.annotated$location)
dataset.df.annotated <- dataset.df.annotated[dataset.df.annotated$location != "",] #remove blank rows

#write results to csv
write.csv(dataset.df.annotated, file=gsub(".csv", "_geocoded.csv", dataset), row.names = F)

#print warnings
warnings()

#clean workspace
rm(list = ls())


