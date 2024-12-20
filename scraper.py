import requests
from bs4 import BeautifulSoup
import random
from time import sleep

def get_random_proxy():
    proxies = [
        "http://192.168.1.100:8080",
        "http://192.168.1.101:8080",
        # add as many proxies you need
    ]
    return {"http":random.choice(proxies), "https":random.choice(proxies)}

def scrape_products(url, headers, min_products = 200):
    products = []
    page = 1

    while len(products) < min_products:
        print(f"Scraping page {page}...")
        try:
            response = requests.get(url + f"?page = {page}", headers = headers, proxies = get_random_proxy(), timeout = 10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            product_cards = soup.find_all("div", class_ = "productContainer")

            for card in product_cards:
                try:
                    name = card.find("h3", class_ = "name").text.strip()
                    price = card.find("h3", class_ = "price").text.strip()
                    brand = card.find("h3", class_ = "brand").text.strip()
                    seller = card.find("h3", class_ = "seller").text.strip()

                    products.append({
                        "Name" : name,
                        "Price" : price,
                        "Brand" : brand,
                        "Seller" : seller
                    })

                    if len(products) >= min_products:
                        break
                except Exception as e:
                    print(f"Error parsing product : {e}")

            page += 1
            sleep(random.uniform(1, 3))

        except Exception as e:
            print(f"Error fetching page {page} : {e}")
            break
        
    return products