from flask import Flask, render_template

app = Flask(__name__)

meniu=[# Espresso
    "Small Espresso",
    "Double Espresso",
    "Flavoured Espresso",
    "Flavoured Double Espresso",
    
    # Coffee & Milk
    "Flat White",
    "Café Latte",
    "Cappuccino",
    "Flavoured Café Latte",
    "Flavoured Cappuccino",
    
    # Specialties
    "Caramel Macchiato",
    "Café Mocca",
    "White Mocca",
    
    # Chocolate & Tea
    "Hot Chocolate",
    "Flavoured Hot Chocolate",
    "Ceai (Mentă, Fructe de pădure, Verde, Negru)",
    
    # Summer Drinks
    "Ice Frappe",
    "Cocktail Non Alcoholic",
    "Ice Cappuccino",
    
    # Soft Drinks
    "Coca-Cola",
    "Schweppes (Mandarine / Tonic)",
    "Dorna Apă Plată"]

@app.route('/')
def home():
    return render_template('Main.html')
@app.route('/meniu')
def meniu():
    # This will look for meniu.html in your /templates folder
    return render_template('meniu.html')

if __name__ == '__main__':
    app.run(debug=True)