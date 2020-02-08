from bs4 import BeautifulSoup
import requests


html_link = "https://theinternship.io/"
html_doc = requests.get(html_link)
lst_text, lst_img, result = [], [], []

if html_doc.ok:
    
    data = BeautifulSoup(html_doc.text, 'html.parser').find_all("div",{"class": "partner", "data-v-018ba4ef": ""})
    for i in data:
        text_link, img_link = i.find("span").getText(), i.find("img").get("src")
        lst_text.append(len(text_link))
        lst_img.append(img_link)

    while len(lst_text) != 0:
        maxText_index = lst_text.index(min(lst_text))
        result.append(lst_img[maxText_index])
        lst_text.remove(lst_text[maxText_index])
        lst_img.remove(lst_img[maxText_index])

    print("\n".join(result))



