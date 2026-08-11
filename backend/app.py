from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


lista = [{'id': 1, 'nome': 'red dead redemption', 'anno_pub': '2010', 'versione': 'deluxe'}]

@app.route("/giochi", methods=["GET"])
def get_giochi():
    return jsonify(lista), 200

@app.route('/giochi', methods=["POST"])
def add_giochi():
    nuovo_gioco = request.get_json()
    nuovo_gioco['id'] = len(lista) + 1
    lista.append(nuovo_gioco)
    return jsonify(nuovo_gioco), 201

@app.route("/giochi/<int:gioco_id>", methods=["DELETE"])
def delete_giochi(gioco_id): 
    global lista
    lista = [g for g in lista if g["id"] != gioco_id]
    return jsonify({"messaggio": f"Gioco {gioco_id} eliminato"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)