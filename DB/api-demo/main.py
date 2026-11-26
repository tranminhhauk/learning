import os
from flask import Flask, request, jsonify
import htttp_method
from db import *

app = Flask(__name__)


init_db()

@app.route("/customers", methods = [htttp_method.GET])
def get_customer():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")
    customer = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(customer)

@app.route("/customers", methods = [htttp_method.POST])
def register_customers():
    data = request.get_json()
    if not data or not 'name' or 'age' not in data:
        return jsonify({"error": "Miss name or age"}), 400
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO customers(name, age) VALUES (%s, %s) RETURNING *;",
                (data['name'], data['age'])
        )
    new_customer = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"new customes": new_customer}), 200

@app.route("/customers/<int:customers_id>", methods = [htttp_method.PUT])
def update_customer(customers_id):
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({"error": "Missing name or age"}), 400

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE customers SET name = %s, age = %s WHERE id = %s RETURNING *;",
        (data['name'], data['age'], customers_id)
    )
    updated_customers = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if not updated_customers:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"Updated successfully": updated_customers}), 200

@app.route("/customers/<int:customers_id>", methods=[htttp_method.DELETE])
def delete_user(customers_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM customers WHERE id = %s RETURNING id;", (customers_id,))
    deleted_id = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if not deleted_id:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({"message": f"Deleted user id {customers_id}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)