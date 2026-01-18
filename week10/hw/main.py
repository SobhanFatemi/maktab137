from flask import Flask, request, jsonify

app = Flask(__name__)

items = {}

@app.route("/items", methods=["POST"])
def create_item():
    data = request.json
    item_id = len(items) + 1
    items[item_id] = data
    return jsonify({"id": item_id, "item": data})

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    if item_id not in items:
        return jsonify({"error": "not found"}), 404
    items[item_id] = request.json
    return jsonify({"item": items[item_id]})

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({"error": "not found"}), 404
    del items[item_id]
    return jsonify({"message": "deleted"})

app.run()
