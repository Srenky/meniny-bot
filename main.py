import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.kvety.sk/meniny-dnes-kto-ma-dnes-meniny/"

    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")

    if soup.find("p", {"class": "nameday__circle-text"}) != None:
        meniny_text = soup.find("p", {"class": "nameday__circle-text"})
    if meniny_text.find("strong") != None:
        print(f'Dnes ma meniny: {meniny_text.find("strong").text}')


if __name__ == "__main__":
    main()
