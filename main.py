import pandas as pd
from scraper import scrape_products
from analysis import clean_data, analyze_data, visualize_data

URL = "https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/"
HEADERS = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

products = scrape_products(URL, HEADERS)

data = pd.DataFrame(products)
data.to_csv("data/products.csv", index = False)
print("Data saved to data/products.csv")

data = pd.read_csv("data/products.csv")
data = clean_data(data)

brand_counts, seller_counts = analyze_data(data)

visualize_data(brand_counts, seller_counts)