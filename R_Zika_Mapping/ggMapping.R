#devtools::install_github("dkahle/ggmap")
library(ggmap)

dataset <- "cdc_zika_geocoded.tab"
output.name <- "cdc_zika_output"
location.data <- read.table(file=dataset, stringsAsFactors = F, header = T)

upperLimit <- max(location.data$value, na.rm = T)
location.data$value <- lapply(location.data$value, as.integer)
location.data <- location.data[is.na(location.data$value) == F,]
location.data <- location.data[location.data$location_type != "region",]
location.data <- as.data.frame(location.data)

#plot by cases vs area
world <- make_bbox(lon = location.data$lon, lat = location.data$lat, f = 0.10)

world <- get_map(location = world, maptype = "terrain", source = "stamen")

#Iput: location.data is a dataframe with lon and lat column for coordinates
#And data.key is a column from location.data with which to identify outliers.
#inputMap is the map you'd like to plot on
basicMap <- function(inputMap, location.data, data.key, plot.title, plot.subtitle) {
  location.map <- ggmap(inputMap) +
    geom_point(data = location.data, mapping = aes(x = lon, y= lat, color = data.key), size = 0.3, shape = 8, alpha = 0.5, show.legend = F) + 
    ggtitle(plot.title, subtitle = plot.subtitle) + xlab("Latitude") + ylab("Longitude")
  return(location.map)
}

zika.map <- basicMap(world, location.data, location.data$data_field_code, "CDC Zika Reports", "Grouped by ISO Report Code")
ggsave(file = paste0(output.name, "_1.png"), plot = zika.map, width = 40, height = 49)

warnings()
rm(list=ls())