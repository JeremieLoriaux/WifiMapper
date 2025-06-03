from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests

url = "https://www.wifimap.io/map/4415-brussels"
public_hotspots = []

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
for elem in soup.find_all("div", attrs={"class": "HotspotsListItem_hotspotListItem__Bab1Y HotspotsListItem_cursorPointer__jmEKv"}):
    wifi_data = [p.get_text(strip=True) for p in elem.find_all("p")]
    public_hotspots.append(wifi_data)
