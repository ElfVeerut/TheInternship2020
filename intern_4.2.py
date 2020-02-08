from bs4 import BeautifulSoup
import requests
import json

html_link = "https://theinternship.io/"
html_doc = requests.get(html_link)

lst_img = []
if html_doc.ok:
    data = BeautifulSoup(html_doc.text, 'html.parser').find_all("div",{"class": "partner", "data-v-018ba4ef": ""})
    for i in data:

        lst_img.append(i.find("img").get("src"))

    result = {"companies":[
        {"logo": html_link + i} for i in lst_img
        ]}

    with open("result.json","w+") as f:
        f.write(json.dumps(result))