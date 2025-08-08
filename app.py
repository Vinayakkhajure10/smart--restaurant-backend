from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

ORDERS_FILE = "backend/database.json"

def load_orders():
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as file:
            return json.load(file)
    return []

def save_orders(orders):
    with open(ORDERS_FILE, "w") as file:
        json.dump(orders, file, indent=2)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/place_order", methods=["POST"])
def place_order():
    data = request.form
    order = {
        "name": data.get("name"),
        "table": data.get("table"),
        "items": data.get("items"),
        "total": data.get("total"),
        "status": "Preparing"
    }
    orders = load_orders()
    orders.append(order)
    save_orders(orders)
    return redirect("/order_status")

@app.route("/order_status")
def order_status():
    orders = load_orders()
    return render_template("order_status.html", orders=orders)

@app.route("/admin")
def admin():
    orders = load_orders()
    return render_template("admin.html", orders=orders)

@app.route("/update_status", methods=["POST"])
def update_status():
    table = request.form.get("table")
    new_status = request.form.get("status")
    orders = load_orders()
    for order in orders:
        if order["table"] == table:
            order["status"] = new_status
    save_orders(orders)
    return redirect("/admin")

if __name__ == "__main__":
    app.run(debug=True)