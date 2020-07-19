def get_folium_map(df, latitude_col,longitude_col, colour_by = None, popup_name_col = None):
  '''
  Plots an interactive map of longitude latitude coordinates in Folium.
  
  df:             A dataframe with a longitude and latitude coordinates within.
  latitude_col    The column name containing latitude figures
  longitude_col   The column name containing longitude figures
  colour_by       Any column name containing the categories you wish to colour by
  pop_name_col    Enter the column name which contains any popup information you wish to display
                  when you click  point
  '''

  import pandas as pd
  import folium
  import numpy as np
  
  global colourdict
  
  # Set up a list of points
  locationlist = df[[latitude_col, longitude_col]].values.tolist()


  # Find the mean long/lat coordinates so we an use these as the maps centre point
  mean_lat = df[latitude_col].mean()
  mean_long = df[longitude_col].mean()

  m = folium.Map(location=[mean_lat, mean_long], 
                     #zoom_start=zoom, 
                     prefer_canvas=True,
                     zoom_control= True)


  # Check if a colour column has been defined
  # if so, set up a colour dictionary to define some colours
  if colour_by:    
    colour_options = ['blue', 'red', 'green', 'brown','yellow','purple','orange',
                      'darkgreen', 'darkpurple', 'darkred', 'gray', 'darkblue', 'lightblue', 
                      'lightgray', 'lightgreen', 'lightred', 'orange', 'pink', 'purple','cadetblue',
                      'black']
    
    categories = np.unique(df[colour_by])
    colours = np.linspace(0, 1, len(categories))
    colourdict = dict(zip(categories, colours))

    colour_no = 0 # counter for keep track of max colours

    for i in colourdict.keys():
      colourdict[i] = colour_options[colour_no]
      colour_no += 1
      if colour_no == len(colour_options): colour_no = 0 #reset counter if we reach the max



  for point in range(0, len(locationlist)):

      # Check if a popup name column has been defined
      if popup_name_col:
        popup = folium.Popup(df.iloc[point][popup_name_col], parse_html=True)
      else:
        popup = None


      # Check if a colour column has been defined
      if colour_by:
        colour = colourdict[df.iloc[point][colour_by]]
      else:
        colour = 'red'


      folium.CircleMarker(locationlist[point], 
                          radius=1, 
                          color=colour,
                          popup=popup
                         ).add_to(m)

  m

  return m