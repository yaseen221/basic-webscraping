from bs4 import BeautifulSoup
import requests
from io import BytesIO
import PIL
from PIL import Image
import os


search = input("Search for: ")
params = {"q": search}

r = requests.get("http://www.bing.com/images/search", params=params)
soup = BeautifulSoup(r.text, "html.parser")

links = soup.find_all("a", {"class": "thumb"})

for item in links:
    img_object = requests.get(item.attrs["href"])
    title = item.attrs["href"].split("/")[-1].partition("?")[0]
    try:
        img = Image.open(BytesIO(img_object.content))
    except PIL.UnidentifiedImageError:
        print("Error in image")
        continue
    img.save("./scraped_images/" + title)
