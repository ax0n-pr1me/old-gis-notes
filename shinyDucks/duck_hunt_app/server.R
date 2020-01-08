#Duck Hunter for Fish and Wildlife Service v2

library(shiny)
library(leaflet)
library(sp)
library(raster)
library(rgdal)

# load static data

RGB = raster("../layers/rgb.tif")
#NIR = raster("../layers/nir.tif")
DSM = raster("../layers/dsm.tif")


# Define server logic required to draw a histogram
shinyServer(function(input, output) {

    # define the dataset that adjusts to changing input in selectInput(inputId="baseMap" , )

    mapfile <- reactive({
            switch(input$Raster,
                   "RGB" = RGB,
                   "NIR" = NIR,
                   "DSM" = DSM)
        })
    
    # define the outputinto the shiny app
    output$Raster <- renderLeaflet({


    #crs(r) <- CRS("+init=epsg:4326")
    
    leaflet() %>% addTiles() %>%

    addRasterImage(mapfile(),
                   colors = "Spectral",
                   opacity = 1)
      
  })

})

