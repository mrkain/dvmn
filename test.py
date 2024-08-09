import requests


article_ids = ["Лондон", "Череповец", "Шереметьево", "fggwg"]
url_template = "https://wttr.in/{}?M?nTqu&lang=ru"

for article_id in article_ids:
    url = url_template.format(article_id)
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Ошибка {response.status_code}")
