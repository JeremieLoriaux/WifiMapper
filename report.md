# Report: Understanding the Code and Google Maps API Integration

## What Is an API?

An **API** (Application Programming Interface) is a way for different software programs to talk to each other. Companies like Google offer APIs so developers can use services (like maps, weather, or translations) in their own apps. In this project, the Google Maps API is used to convert addresses into geographic coordinates (latitude and longitude) and to show those locations on a map.

---

## Purpose of the Code

This Python program:
1. **Scrapes a website** to find public WiFi hotspot locations.
2. **Uses the Google Maps API** to find each hotspot's coordinates.
3. **Creates an interactive map** that shows all hotspots using those coordinates.

---

## Code Overview

### 1. **Environment Setup**

```python
load_dotenv()
api_key = os.getenv("API_KEY")
url = os.getenv("URL")
```
- Uses a .env file to load the API_KEY (for Google Maps) and URL (the page to scrape).

- If these values are missing, the program stops with an error.

### 2. **Google Maps Client**
```python
map_client = googlemaps.Client(api_key)
```
- map_client is an instance of the googlemaps.Client class.

- It uses the API key to authorize requests to the Google Maps services.

- This client allows the program to access different features of the API, such as geocoding (converting addresses to coordinates).

### 3. **Scraping Hotspot Data**
```python
def scrape_wifi(url: str) -> list[dict]:
```
- The scrape_wifi() function uses requests and BeautifulSoup to load and parse the webpage.

- It finds elements that contain hotspot information.

- Returns a list of dictionaries with "address" and "wifi_name".

### 4. **Getting coordinates**
```python
def get_geocode(location: str):
```
- Uses map_client.geocode(location) to ask Google Maps for the coordinates of an address.

- Returns the latitude and longitude if successful.

### 5. **Creating the Map**
```python
def create_html(hotspot_data):
```
- Builds an HTML page with embedded JavaScript.

- Uses the Google Maps JavaScript API to:

    - Create a map centered on a default location.

    - Place markers for each WiFi hotspot.

    - Show information when a marker is clicked.

### 6. **Main Program**
```python
def main()
```
- Runs all the steps in order:

    1. Scrapes hotspot data from the URL.

    2. Gets coordinates for each hotspot.

    3. Creates an interactive map with markers.

---

## How to get access to the Google Maps API
1. Create a Google Cloud account: https://cloud.google.com

2. Create a new project in the Google Cloud Console.

3. Enable APIs:

    - Maps JavaScript API

    - Geocoding API

4. Generate an API key:

    - Go to the "Credentials" section.

    - Click "Create credentials" → "API key".

5. Save the key and URL in a .env file:
```.env
API_KEY=your_google_maps_api_key
URL=your_target_url
```
[![usefull video](http://img.youtube.com/vi/hsNlz7-abd0/default.jpg)](https://www.youtube.com/watch?v=hsNlz7-abd0 "How to Get a Google Maps API Key in 2 Mins")