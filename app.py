from flask import Flask, render_template, url_for, request
import mongodb


app = Flask(__name__)

@app.route("/")
def index():
    data = list(mongodb.get_shoes()) + list(mongodb.get_clothing()) + list(mongodb.get_accessories())
    return render_template("index.jsx", data=data)

@app.route('/filter_by_price', methods=['GET'])
def filter_by_price():
    price_limit = request.args.get('price', type=float)
    filtered_products = mongodb.price_range(price_limit )
    heading_data = f"Products under ${price_limit}"
    return render_template('index.html', filter_head=heading_data, data=filtered_products)

@app.route("/men")
def men():
    data = list(mongodb.get_shoes(None, "men")) + list(mongodb.get_clothing(None, "men")) + list(mongodb.get_accessories(None, "men"))
    return render_template("index.html", head="All Products", data = data)

@app.route("/men/shoes")
def men_shoes():
    data = list(mongodb.get_shoes(None, "men"))
    return render_template("index.html",head="Shoes", data = data)

@app.route("/men/clothing")
def men_clothing():
    data = list(mongodb.get_clothing(None, "men"))
    return render_template("index.html", head="Clothing", data = data)

@app.route("/men/accessories")
def men_accessories():
    data = list(mongodb.get_accessories(None, "men"))
    return render_template("index.html",head="Accessories", data = data)

@app.route("/women")
def women():
    data = list(mongodb.get_shoes(None, "women")) + list(mongodb.get_clothing(None, "women")) + list(mongodb.get_accessories(None, "women"))
    return render_template("index.html", head="All Products" , data = data)

@app.route("/women/shoes")
def women_shoes():
    data = list(mongodb.get_shoes(None, "women"))
    return render_template("index.html", head="Shoes", data = data)

@app.route("/women/clothing")
def women_clothing():
    data = list(mongodb.get_clothing(None, "women"))
    return render_template("index.html", head="Clothing", data = data)

@app.route("/women/accessories")
def women_accessories():
    data = list(mongodb.get_accessories(None, "women"))
    return render_template("index.html", head="Accessories", data = data)

@app.route("/kids")
def kids():
    data = list(mongodb.get_shoes(None, "big_kid")) + list(mongodb.get_shoes(None, "little_kid")) + list(mongodb.get_shoes(None, "toddler"))+ list(mongodb.get_clothing(None, "big_kid")) + list(mongodb.get_clothing(None, "little_kid")) + list(mongodb.get_clothing(None, "toddler"))  + list(mongodb.get_accessories(None, "kid"))
    return render_template("index.html", data = data)

@app.route("/kids/shoes")
def kids_shoes():
    data = list(mongodb.get_shoes(None, "big_kid")) + list(mongodb.get_shoes(None, "little_kid")) + list(mongodb.get_shoes(None, "toddler"))
    return render_template("index.html", head="Shoes", data = data)

@app.route("/kids/clothing")
def kids_clothing():
    data = list(mongodb.get_clothing(None, "big_kid")) + list(mongodb.get_clothing(None, "little_kid")) + list(mongodb.get_clothing(None, "toddler"))
    return render_template("index.html", head="Shoes", data = data)
    
@app.route("/kids/accessories")
def kids_accessories():
    data = list(mongodb.get_accessories(None, "kid"))
    return render_template("index.html", head="Shoes", data = data)

if __name__ == "__main__":
    app.run(debug=True)
