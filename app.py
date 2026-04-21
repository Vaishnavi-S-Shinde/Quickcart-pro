from flask import Flask, render_template, request, jsonify, session
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'quickcart_secret_key_12345'

# Products data - aapke existing products
PRODUCTS = [
    {"id": 1, "name": "iPhone 15 Pro Max", "category": "Electronics", "price": 129999, "rating": 4.8, "badge": "Hot", "description": "Latest A17 Pro chip", "image": "https://picsum.photos/300/200?random=1", "original_price": 145000, "stock": 15, "brand": "Apple"},
    {"id": 2, "name": "Sony WH-1000XM5", "category": "Electronics", "price": 29999, "rating": 4.9, "badge": "Bestseller", "description": "Noise cancellation", "image": "https://picsum.photos/300/200?random=2", "original_price": 35000, "stock": 8, "brand": "Sony"},
    {"id": 3, "name": "Nike Air Max", "category": "Clothing", "price": 12999, "rating": 4.6, "badge": "Trending", "description": "Running shoes", "image": "https://picsum.photos/300/200?random=3", "original_price": 15999, "stock": 25, "brand": "Nike"},
    {"id": 4, "name": "MacBook Pro M3", "category": "Electronics", "price": 169999, "rating": 4.9, "badge": "New", "description": "16-inch, 36GB RAM", "image": "https://picsum.photos/300/200?random=4", "original_price": 189999, "stock": 10, "brand": "Apple"},
    {"id": 5, "name": "Samsung 4K TV", "category": "Electronics", "price": 64999, "rating": 4.7, "badge": "Sale", "description": "55-inch Smart TV", "image": "https://picsum.photos/300/200?random=5", "original_price": 79999, "stock": 5, "brand": "Samsung"},
    {"id": 6, "name": "Leather Jacket", "category": "Clothing", "price": 4999, "rating": 4.5, "badge": "", "description": "Premium leather", "image": "https://picsum.photos/300/200?random=6", "original_price": 7999, "stock": 12, "brand": "Puma"},
    {"id": 7, "name": "Study Table", "category": "Furniture", "price": 7999, "rating": 4.4, "badge": "", "description": "Wooden study table", "image": "https://picsum.photos/300/200?random=7", "original_price": 11999, "stock": 7, "brand": "LG"},
    {"id": 8, "name": "Smart Watch", "category": "Accessories", "price": 3999, "rating": 4.3, "badge": "", "description": "Fitness tracker", "image": "https://picsum.photos/300/200?random=8", "original_price": 5999, "stock": 30, "brand": "Boat"},
    {"id": 9, "name": "Yoga Mat", "category": "Sports", "price": 999, "rating": 4.6, "badge": "", "description": "Non-slip mat", "image": "https://picsum.photos/300/200?random=9", "original_price": 1499, "stock": 50, "brand": "Adidas"},
    {"id": 10, "name": "Coffee Mug Set", "category": "Home & Living", "price": 699, "rating": 4.7, "badge": "", "description": "Set of 4 mugs", "image": "https://picsum.photos/300/200?random=10", "original_price": 999, "stock": 40, "brand": "Philips"},
    {"id": 11, "name": "Wireless Earbuds", "category": "Electronics", "price": 2499, "rating": 4.4, "badge": "", "description": "Bluetooth 5.0", "image": "https://picsum.photos/300/200?random=11", "original_price": 3999, "stock": 45, "brand": "Boat"},
    {"id": 12, "name": "Gaming Keyboard", "category": "Electronics", "price": 4599, "rating": 4.7, "badge": "Gaming", "description": "RGB mechanical", "image": "https://picsum.photos/300/200?random=12", "original_price": 6999, "stock": 20, "brand": "Mi"}
]

# Add discount
for p in PRODUCTS:
    p['discount'] = int(((p['original_price'] - p['price']) / p['original_price']) * 100)

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html', products=PRODUCTS)

@app.route('/api/products')
def get_products():
    """API to get products"""
    return jsonify(PRODUCTS)

@app.route('/api/product/<int:pid>')
def get_product(pid):
    """Get single product"""
    product = next((p for p in PRODUCTS if p['id'] == pid), None)
    return jsonify(product) if product else jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 QuickCart Pro Server Starting...")
    print("="*50)
    print("\n📍 Open this URL in your browser:")
    print("   👉 http://localhost:5000")
    print("\n💡 Press CTRL+C to stop the server")
    print("="*50 + "\n")
    app.run(debug=True, host='127.0.0.1', port=5000)