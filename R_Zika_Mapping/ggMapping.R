# devtools::install_github("dkahle/ggmap")
library(ggmap)

 key <- "AIzaSyA5vYrqxRjSAj9ngibryDSwJrxunhKVCd8"
 register_google(key = key)


wd <- "/Users/immortalcha/"
dataset <- "cdc_zika_geocoded.csv"
dataset <- paste0(wd, dataset)
location.data <- read.csv(file=dataset, stringsAsFactors = F)

#plot by cases vs area
world <- make_bbox(lon = location.data$lon, lat = location.data$lat, f = 0.10)
world <- get_map(location = world, maptype = "terrain", source = "google")
basicMap <- function(inputMap, location.data, data.key) {
  location.map <- ggmap(inputMap) +
    geom_point(data = location.data, mapping = aes(x = lon, y= lat, color = data.key), show.legend = FALSE)
  return(location.map)
}

c <- basicMap(world, location.data, location.data$data_field_code)

#Iput: location.data is a dataframe with lon and lat column for coordinates
#And data.key is a column from location.data with which to identify outliers.
#inputMap is the map you'd like to plot on
world <- get_googlemap(center = c(-80, 0), zoom = 3)
ggmap(world) +
  geom_point(data = location.data,
             aes(color=data_field,x = lon, y = lat),show.legend=FALSE) 

# geocode("seattle")

# ggmap(map)
 # geom_point(data = location.data,
   #          aes(x = lon, y = lat), color = "purple")

