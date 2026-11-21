
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
"""
 URL test : https://ganjoor.net/hafez/ghazal/
 Class name : notice
"""
url = input("please enter the url:")

class_name = input("please enter the class:")

response = requests.get(url, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")


links = soup.select(f".{class_name}")

for link in links:
    print("MATN:", link.get_text(strip=True))


images = soup.find_all("img")
images_links = []

for image in images:
    src = image.get("src")

    if src:
        full_url = urljoin(response.url, src)
        images_links.append(full_url)

print(list(images_links))

