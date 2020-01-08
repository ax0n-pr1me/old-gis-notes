library(shiny)
library(leaflet)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel("Duck Hunter for USFWS v0.1"),
  
  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
       selectInput(inputId = "Raster",
                   label = "Select Raster",
                   choices = c("RGB",
                               "NIR",
                               #"NDVI",
                               "DSM"))
    ),
    
    # Show Map
    mainPanel(
      leafletOutput("Raster"),
      p()
      #actionButton("recalc", "recalc_label")
      )
    )
  )
)
