# WifiMapper

This project scrapes a list of public WiFi hotspots from a specified webpage, geocodes their addresses using the Google Maps API, and generates an interactive map visualizing the hotspots. The resulting HTML file displays markers for each hotspot, which users can click to see detailed information.

## Features

- Web scraping of public WiFi hotspot data from a configurable URL
- Geocoding of hotspot addresses using Google Maps API
- Interactive HTML map generation with clickable markers
- Environment-based configuration using `.env` for security and flexibility

## Requirements

- Python 3.7 or higher
- Google Maps API Key
- Target website must have WiFi hotspot data with a specific HTML structure

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/public-wifi-hotspot-mapper.git
   cd public-wifi-hotspot-mapper
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
3. **Install dependencies**

    Create a .env file in the project root with the following content:
    ```bash
    API_KEY=your_google_maps_api_key
    URL=https://example.com/hotspots
    ``` 
    Replace your_google_maps_api_key with your actual Google Maps API key and https://example.com/hotspots with the URL from which to scrape hotspot data.
## Usage
Run the script using:
```bash
python main.py
``` 


This will:

- Scrape public WiFi hotspot data from the specified URL

- Geocode each address using the Google Maps API

- Generate an interactive HTML file named google_map_hotspots.html

You can open this file in your browser to explore the hotspot locations on a map.
## Project Structure
```bash
public-wifi-hotspot-mapper/
├── main.py                  # Main script to run
├── .env                     # Stores API keys and target URL (not 
                             # tracked by git)
├── requirements.txt         # Python dependencies
├── google_map_hotspots.html # Output map file (generated)
└── README.md                # Project documentation
```
## Dependencies
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

- [requests](https://pypi.org/project/requests/)

- [python-dotenv](https://pypi.org/project/python-dotenv/)

- [googlemaps](https://pypi.org/project/googlemaps/)

You can install them manually with:
```bash
pip install beautifulsoup4 requests python-dotenv googlemaps
```
Or use the provided requirements.txt.
## Notes
- The HTML structure used in scraping is specific and may change. If the source website updates its layout, you may need to modify the scrape_wifi() function accordingly.

- The script is synchronous and intended for small-scale use. For larger datasets or high-frequency usage, consider rate limiting and more robust error handling.

- Ensure your Google Maps API key has Geocoding and Maps JavaScript API enabled.

## Authors
- Mihai : [mihai-ilie-01](https://github.com/mihai-ilie-01)
- Jeremie : [JeremieLoriaux](https://github.com/JeremieLoriaux)