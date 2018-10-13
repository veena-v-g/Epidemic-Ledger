# install.packages("sf")
# install.packages("mapview")
library(sf)
library(mapview)

#Input: one csv file with the columns 'lon' and 'lat' which correspond to longitudinal and latitude coordinates
#Output: one html file containing the plotted coordinates on a map.

dataset <- "cdc_zika_geocoded.csv"
location.data <- read.csv(file=dataset, stringsAsFactors = F)

#remove any locations which don't have lon and lat coordinates
location.data <- location.data[is.na(location.data$lon) == F,]
location.data <- location.data[is.na(location.data$lat) == F,]

#convert the dataframe to be read by mapview
locations_zika <- st_as_sf(location.data, coords = c("lon", "lat"), crs = 4326)

#load into a map
mapped <- mapview(locations_zika)

#write map
output <- gsub("geocoded.csv", "mapped", dataset)
mapshot(mapped,file = paste0(output, ".png"), url = paste0(output, ".html"))

print("Your map is saved to: ")
print(paste0(output,".html"))

#End program
warnings()
rm(list = ls())