install.packages("sf")
install.packages("mapview")
library(sf)
library(mapview)

location.data <- read.csv()
locations_zika <- st_as_sf(location)