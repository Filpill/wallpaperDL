import os
import string
import random
import requests

def wallpaper_search_api(query):
    url = f"https://wallhaven.cc/api/v1/search?q={query}"
    res = requests.get(url)
    json_data = res.json()
    dl_links = [wallpaper["path"] for wallpaper in json_data["data"]]
    return dl_links

def generate_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

def download_wallpaper(url):
    print(f"Downloading...{url}")
    user="filpill"
    temp_wallpapers = 'desktop_setup/wallpaperDL/temp_screens'
    res = requests.get(url)
    wall_name = generate_id()
    ext = os.path.splitext(url)[1]
    dl_path = fr"/home/{user}/{temp_wallpapers}/{wall_name}{ext}"
    open(dl_path,'wb').write(res.content)

# Search Query
query = input("Enter search criteria: ")
wall_dl_url = wallpaper_search_api(query)

# Download Wallpapers Based on Search Query
for url in wall_dl_url:
    download_wallpaper(url)
