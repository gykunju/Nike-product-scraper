from scraper import scrape_data
import mongodb


def set_shoes_data():
    men = scrape_data("https://www.nike.com/w/mens-shoes-nik1zy7ok")
    women = scrape_data("https://www.nike.com/w/womens-shoes-5e1x6zy7ok")
    big_kids = scrape_data("https://www.nike.com/w/big-kids-shoes-agibjzv4dhzy7ok")
    little_kids = scrape_data("https://www.nike.com/w/little-kids-shoes-6dacezv4dhzy7ok")
    toddlers = scrape_data("https://www.nike.com/w/baby-toddler-shoes-2j488zy7ok")

    data = men + women + big_kids + little_kids + toddlers
    mongodb.insert_shoes(data)
    print(len(data))

def set_clothing_data():
    men = scrape_data("https://www.nike.com/w/mens-clothing-6ymx6znik1")
    women = scrape_data("https://www.nike.com/w/womens-clothing-5e1x6z6ymx6")
    big_kids = scrape_data("https://www.nike.com/w/big-kids-clothing-6ymx6zagibjzv4dh")
    little_kids = scrape_data("https://www.nike.com/w/little-kids-clothing-6dacez6ymx6zv4dh")
    toddlers = scrape_data("https://www.nike.com/w/baby-toddler-kids-clothing-2j488z6ymx6zv4dh")

    data = men + women + big_kids + little_kids + toddlers
    mongodb.insert_clothing(data)

def set_accessory_data():
    men = scrape_data("https://www.nike.com/w/mens-accessories-equipment-awwpwznik1")
    women = scrape_data("https://www.nike.com/w/womens-accessories-equipment-5e1x6zawwpw")
    kids = scrape_data("https://www.nike.com/w/kids-accessories-equipment-awwpwzv4dh")

    data = men + women + kids
    mongodb.insert_accessories(data)


### SCRAPE AND SET TO DB
# set_shoes_data()
# set_clothing_data()
# set_accessory_data()


# data = mongodb.get_accessories()
# count = 0
# for d in data:
#     print(d)
#     count +=1
# print(count)


ans = mongodb.price_range(50, "women", "shoes")
if ans:
    for a in ans:
        print(a)
else:
    print("Nothing")


### MINIMUM AND MAXIMUM
# shoes = mongodb.get_minimum_shoe_price()
# print(shoes)
# shoes = mongodb.get_maximum_shoe_price()
# print(shoes)
