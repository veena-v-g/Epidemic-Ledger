# install.packages("sf")
# install.packages("mapview")
library(sf)
library(mapview)

#Input: one csv file with the columns 'lon' and 'lat' which correspond to longitudinal and latitude coordinates
#Output: one html file containing the plotted coordinates on a map.


mapLocations <- function(location.df, output.name) {
  output <- output.name
  location.data <- location.df
  #convert the dataframe to be read by mapview
  locations_zika <- st_as_sf(location.data, coords = c("lon", "lat"), crs = 4326)
  
  #load into a map
  mapped <- mapview(locations_zika)
  
  #write map
  mapshot(mapped, url = paste0(output, ".html"))
  
  print("Your map is saved to: ")
  print(paste0(output,".html"))
  
}

dataset <- "cdc_zika_geocoded.csv"
location.data <- read.csv(file=dataset, stringsAsFactors = F)

#remove any locations which don't have lon and lat coordinates
location.data <- location.data[is.na(location.data$lon) == F,]
location.data <- location.data[is.na(location.data$lat) == F,]

#1. write first map
output <- gsub("geocoded.csv", "mapped", dataset)
mapLocations(location.data, output)

#2. Remove rows where value(#of cases) == 0
location.data <- location.data[location.data$value != 0, ]
output <- paste0(output, "_casesNotZero")
mapLocations(location.data, output)

#End program
warnings()
rm(list = ls())