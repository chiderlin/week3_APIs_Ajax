import requests
import json
import re

url = requests.get("https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json")
print(url.status_code)
data = json.loads(url.text)
data = data["result"]["results"]
all_data_str = ""

# longitude 經度, latitude緯度
for area in data:
    etl_img = area["file"].lower()
    etl_img = etl_img.replace("http"," http") # 在http前面加space
    etl_img = etl_img.split(" ") # 再用split以" "作為分割點 => 變成list
    all_data_str += f'{area["stitle"]}, {area["longitude"]}, {area["latitude"]}, {etl_img[1]}\n' # 觀察後: etl_img[0] 一定是'',所以取etl_img[1]
    
with open(file="data.txt", mode="w", encoding="utf-8") as f:
    f.write(all_data_str)