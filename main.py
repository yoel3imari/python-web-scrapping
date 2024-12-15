# %%
import requests 
from bs4 import BeautifulSoup
import json

response = requests.get("https://en.wikipedia.org/wiki/Khabib_Nurmagomedov")

with open("response.html", "w", encoding="utf-8") as file:
    file.write(response.text)

# %%

soup = BeautifulSoup(response.text, "html.parser")

# %%
table = soup.select("table.wikitable")[1]
trs = table.find_all("tr")
opponents = []
for tr in trs:
    tds = tr.find_all("td")
    if not tds:
        continue
    opp_node = tds[2]
    opp = opp_node.string
    if opp is not None:
        opponents.append(opp)
        continue
    opponents.append(opp_node.a.string)






opp_json = json.dumps(opponents)
with open("khabib_opponents.json", "w", encoding="utf-8") as f:
    f.write(opp_json)


