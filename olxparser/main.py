import random
from bs4 import BeautifulSoup
import requests
import lxml
import time

url = "https://www.olx.ua/uk/transport/legkovye-avtomobili/"
HEADERS = \
    {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
mark = []
price = []


def main():
    req = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(req.text, "lxml")

    urls = soup.find_all("a", class_="thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink")
    for items in urls:
        # time.sleep(random.randint(1,5))
        item_href = items.get("href")
        req_2 = requests.get(item_href, headers=HEADERS)

        # with open("index2.html", "w", encoding="utf-8") as file:
        #     file.write(req_2.text)

        soup_2 = BeautifulSoup(req_2.text, "lxml")
        car_info = soup_2.find("div", class_="css-1wws9er")

        car_Mark = car_info.find("h1", class_="css-1soizd2 er34gjf0").text
        car_Price = car_info.find("h3", class_="css-ddweki er34gjf0").text

        print("[+] " + car_Mark + "\tЦіна: " + car_Price + "\tСсилка: " + item_href)


if __name__ == '__main__':
    main()
