import pandas as pd
import matplotlib.pyplot as plt

def clean_data(data):
    data['Price'] = data['Price'].replace('[^0-9.]', '', regex = True).astype(float)
    return data

def analyze_data(data):
    most_expensive = data.loc[data['Price'].idxmax()]
    cheapest = data.loc[data['Price'].idxmin()]
    brand_counts = data['Brand'].value_counts()
    seller_counts = data['Seller'].value_counts()

    print("Most Expensive Product : \n", most_expensive)
    print("\n Cheapest Product : \n", cheapest)
    print("\n Number of Products by Each Brand : \n", brand_counts)
    print("\n Number of Products by Each Seller : \n", seller_counts)

    return brand_counts, seller_counts

def visualize_data(brand_counts, seller_counts):
    plt.figure(figsize = (12,6))
    brand_counts[:10].plot(kind = 'bar', color = 'red', title = 'Top 10 Brands by Product Count')
    plt.ylabel('Number of Products')
    plt.show()

    plt.figure(figsize = (12, 6))
    seller_counts[:10].plot(kind = 'bar', color = 'yellow', title = 'Top 10 Sellers by Product Count')
    plt.ylabel('Number of Products')
    plt.show()