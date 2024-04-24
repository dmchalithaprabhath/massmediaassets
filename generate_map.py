import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Assuming 'data.xlsx' is in the root directory of the repository
excel_path = 'data.xlsx'
html_output_path = 'custom.html'

# Load the Excel data into a DataFrame
df = pd.read_excel(excel_path)

# Initialize a map centered around the average latitude and longitude of the points
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
folium_map = folium.Map(location=map_center, zoom_start=8)

# Create a MarkerCluster object
marker_cluster = MarkerCluster().add_to(folium_map)

# Add markers to the cluster
for index, row in df.iterrows():
    popup_content = f"{row['Frame ID']} - {row['Media Owner']}<br>Status: {row['Status']}<br>{row['Address']}, {row['Town']}"
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=folium.Popup(popup_content, max_width=250),
        tooltip=row['Format']
    ).add_to(marker_cluster)

# Save the map as an HTML file
folium_map.save(html_output_path)
