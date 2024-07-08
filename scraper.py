from bs4 import BeautifulSoup  
import requests
import re

def scrap(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Scraping Succesful")
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
    else:
        print("Request unsuccesful")
        return False

def scrape_data(url):
    if re.search("women", url):
        group = "women"
    elif re.search("big-kids", url):
        group = "big kid"
    elif re.search("little-kids", url):
        group = "little kid"
    elif re.search("baby", url):
        group = "toddler"
    elif re.search("kids", url):
        group = "kid"   
    else:
        group = "men"

    if re.search("shoes", url):
        category = "shoes"
    elif re.search("clothing", url):
        category = "clothing"
    elif re.search("accessories", url):
        category = "accessories"

    img = "https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/4e2229e5-22a4-46ac-897b-6860c0a57974/dunk-low-premium-next-nature-womens-shoes-xW59Qz.png"
    
    soup = scrap(url)
    if soup:
        product_cards = soup.find_all("div", class_="product-card__info")

        products = []

        a_cards = soup.find_all("a", class_="product-card__link-overlay")
        
        count = 0
        for card in product_cards:
            title_div = card.find("div", class_="product-card__title")
            title = title_div.text.strip()

            description_div = card.find("div", class_="product-card__subtitle")
            description = description_div.text.strip()

            price_div = card.find("div", class_="product-card__price")
            if price_div:
                current_price_div = price_div.find("div")
                for div in current_price_div:
                    price = div.text.strip()
                    price = re.sub("\$", "", price)
                    price = float(price)
                    break
            
            link = a_cards[count]['href']
            count+=1
            products.append({"name": title, "link": link, "img": img, "price": price, "group": group, "category": category, "description": description})

        print("Products acquired")
        return products
    else:
        print("Soup absent")
        return False