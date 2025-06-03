from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import googlemaps
import os
import json

# Load API key
load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY not found in .env")
url = os.getenv("URL")
if not url:
    raise ValueError("URL not found in .env")

map_client = googlemaps.Client(api_key)

def scrape_wifi(url: str) -> list[dict]:
    public_hotspots = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    for elem in soup.find_all("div", class_="HotspotsListItem_hotspotListItem__Bab1Y HotspotsListItem_cursorPointer__jmEKv"):
        wifi_data = [p.get_text(strip=True) for p in elem.find_all("p")]
        if len(wifi_data) >= 2:
            public_hotspots.append({
                "address": wifi_data[0],
                "wifi_name": wifi_data[1]
            })
    return public_hotspots

def get_geocode(location: str):
    try:
        location_geocode = map_client.geocode(location)
        if location_geocode:
            latlng = location_geocode[0]["geometry"]["location"]
            return latlng
    except Exception as e:
        print(f"Error geocoding {location}: {e}")
    return None

def create_html(hotspot_data):
    html_path = "google_map_hotspots.html"
    with open(html_path, "w") as f:
        f.write(f"""<!DOCTYPE html>
<html>
<head>
    <title>Public WiFi Hotspots</title>
    <script src="https://maps.googleapis.com/maps/api/js?key={api_key}&callback=initMap" async defer></script>
    <style>
      #map {{
        height: 100vh;
        width: 100%;
      }}
    </style>
    <script>
      const hotspots = {json.dumps(hotspot_data, indent=2)};
      function initMap() {{
        const center = {{ lat: 50.8503, lng: 4.3517 }};
        const map = new google.maps.Map(document.getElementById("map"), {{
          zoom: 13,
          center: center,
        }});

        hotspots.forEach(h => {{
          const marker = new google.maps.Marker({{
            position: {{ lat: h.lat, lng: h.lng }},
            map: map,
            title: h.name,
          }});

          const infowindow = new google.maps.InfoWindow({{
            content: `<strong>${{h.name}}</strong><br>${{h.address}}`
          }});

          marker.addListener("click", () => {{
            infowindow.open(map, marker);
          }});
        }});
      }}
    </script>
</head>
<body>
    <div id="map"></div>
</body>
</html>
""")
    print(f"Map HTML saved to: {html_path}")

def main():
    hotspot_data = []
    for hotspot in scrape_wifi(url):
        coords = get_geocode(hotspot["address"])
        if coords:
            hotspot_data.append({
                "name": hotspot["wifi_name"],
                "address": hotspot["address"],
                "lat": coords["lat"],
                "lng": coords["lng"]
            })
    create_html(hotspot_data)

if __name__ == "__main__":
    main()