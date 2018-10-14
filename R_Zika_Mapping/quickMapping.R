# install.packages("sf")
# install.packages("mapview")
library(sf)
library(mapview)

#Input: one tab file with the columns 'lon' and 'lat' which correspond to longitudinal and latitude coordinates
#Output: tow html files containing the all plotted coordinates on a map, and another which omits regions and where no cases were reported.


mapLocations <- function(location.df, output.name) {
  output <- output.name
  
  #convert the dataframe to be read by mapview
  locations_zika <- st_as_sf(location.df, coords = c("lon", "lat"), crs = 4326)
  
  #load into a map
  mapped <- mapview(locations_zika)
  
  #write map
  mapshot(mapped, url = paste0(output, ".html"))
  
  print("Your map is saved to: ")
  print(paste0(output,".html"))
  
}

dataset <- "cdc_zika_geocoded.tab"
location.data <- read.table(file=dataset, stringsAsFactors = F, sep = "\t", header = T)
head(location.data)
#remove any locations which don't have lon and lat coordinates
location.data <- location.data[is.na(location.data$lon) == F,]
location.data <- location.data[is.na(location.data$lat) == F,]

#1. write first map
output <- gsub("geocoded.tab", "mapped", dataset)
mapLocations(location.data, output)

#2. Remove rows where value(#of cases) == 0
#3. Remove case types that are regions since these did not map well
location.data <- location.data[location.data$value != 0, ]
location.data <- location.data[location.data$location_type != "region", ]
location.data <- location.data[is.na(location.data$lon) == F,]
location.data <- location.data[is.na(location.data$lat) == F,]
output <- paste0(output, "_casesNotZero")
mapLocations(location.data, output)


#End program
warnings()
rm(list = ls())