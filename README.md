<!--
TODO:
    - What it does
    - What it takes
    - What it gives
-->

# Epidemic-Ledger

Applying blockchain methodologies for tracking infectious diseases.  The project at the moment places the data into the blockchain from the CSV, takes the data from the CSV and places the information into a R framework that maps the data to the map.  The two parts of the pipeline needs to be connected and launched from a AWS server.  

## Requirements

### Language

* Python 3.6
* Kotlin 1.3.20
* R

### Libraries

* Kotlin
  * Corda 3.3
* Python
  * numpy 1.15
  * virtualenv
* R
  * sf
  * mapview
  * dplyr
  * xlsx
  * tidyr
  * dkahle/ggmap
  

## Installation

1. Open a terminal
1. Type `git clone https://github.com/vghorakavi/Epidemic-Ledger`

## Input

* Disease transmission case data
  * Location
  * Health Status

## Output

* Blockchain of infectious disease transmissions
* A Map of all the disease cases

## Datasets

[Zika Data](https://github.com/vghorakavi/InfectiousBlockchain/blob/master/Datasets/Mosquito/Zika/cdc_zika.csv)

## Articles

### Introduction/Use Case

https://medium.com/@vghorakavi/using-blockchain-to-track-infectious-diseases-ad29b2a20b64
