from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.Nike

def insert_shoes(data):
    collection = db.shoes
    print("Deleting Present Data...")
    collection.delete_many({})
    print("Inserting Data...")
    print("Shoes Inserted") if collection.insert_many(data) else "Shoes Insertion Failed"

def insert_clothing(data):
    collection = db.clothing
    print("Deleting Present Data...")
    collection.delete_many({})
    print("Inserting Data...")
    print("Clothing Inserted") if collection.insert_many(data) else "Clothing Insertion Failed"

def insert_accessories(data):
    collection = db.accessories
    print("Deleting Present Data...")
    collection.delete_many({})
    print("Inserting Data...")
    print("Accessories Inserted") if collection.insert_many(data) else "Accessories Insertion failed!"


def get_shoes(name = None, group = "all"):
    collection = db.shoes
    if name and group != "all":
        shoe = collection.find({"name": name, "group": group})
        if shoe:
            return shoe
        else:
            print("Item not found")
    if name:
        shoe = collection.find({"name": name})
        if shoe:
            return shoe
        else:
            print("Shoe Not found")
    if group == "all":
        return collection.find().sort({"price": 1})
    else:
        return collection.find({"group": group}).sort({"price": 1})

def get_clothing(name = None, group = "all"):
    collection = db.clothing
    if name and group != "all":
        clothing = collection.find({"name": name, "group": group})
        if clothing:
            return clothing
        else:
            print("Item not found")
    if name:
        clothing = collection.find({"name": name})
        if clothing:
            return clothing
        else:
            print("clothing Not found")
    if group == "all":
        return collection.find().sort({"price": 1})
    else:
        return collection.find({"group": group}).sort({"price": 1})

def get_accessories(name = None, group = "all"):
    collection = db.accessories
    if name and group != "all":
        accessories = collection.find({"name": name, "group": group})
        if accessories:
            return accessories
        else:
            print("Item not found")
    if name:
        accessories = collection.find({"name": name})
        if accessories:
            return accessories
        else:
            print("accessories Not found")
    if group == "all":
        return collection.find().sort({"price": 1})
    else:
        return collection.find({"group": group}).sort({"price": 1})
    
def get_minimum_shoe_price():
    collection = db.shoes
    shoe = collection.find_one({}, {"price": 1, "_id": 0}, sort=[("price", 1)]) 
    return shoe['price']

def get_maximum_shoe_price():
    collection = db.shoes
    shoe = collection.find_one({}, {"price": 1, "_id": 0}, sort=[("price", -1)])
    return shoe['price']

def concatenate_cursors(*cursors):
    for cursor in cursors:
        for document in cursor:
            yield document

def price_range(price, group = "all", category = "all"):
    if category != "all" and group != "all":
        if category == "shoes":
            collection = db.shoes
        elif category == "clothing":
            collection = db.clothing
        elif category == "accessories":
            collection = db.accessories
        else:
            print("Invalid category")
            return False

        print("getting data...")
        data = collection.find({"group": group, "price": {"$lt": price}}).sort({"price": 1})
        if list(data):
            print("returning data...")
            return data
        else:
            print("No matches")
            return False 
    elif category == "all" and group == "all":
        shoes = db.shoes.find({"price": {"$lt": price}}).sort({"price": 1})
        clothing = db.clothing.find({"price": {"$lt": price}}).sort({"price": 1})
        accessories = db.accessories.find({"price": {"$lt": price}}).sort({"price": 1})

        data = concatenate_cursors(shoes, clothing, accessories)
        if data:
            return data
        else:
            print("No matches")
            return False
    elif group != "all":
        shoes = db.shoes.find({"group": group, "price": {"$lt": price}})
        clothing = db.clothing.find({"group": group, "price": {"$lt": price}})
        accessories = db.accessories.find({"group": group, "price": {"$lt": price}})

        data = concatenate_cursors(shoes, clothing, accessories)
        if data:
            return data
        else:
            print("No matches")
            return False
