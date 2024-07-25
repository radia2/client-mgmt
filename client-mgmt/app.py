from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import requests
from api import client
import api.client as client
import os
import jwt
import datetime, base64

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/manage_clients")
def manage_clients():
    return render_template("clientmgmt.html")

@app.route("/create_client", methods=["POST"])
def create_client():
    data = request.get_json()
    api_key = request.headers.get('x-api-key') 
    client_name = data["clientName"]
    network = data["network"]
    providers = data["providers"].split(",")
    providers = [provider.strip() for provider in providers]
    public_key = data.get("publicKey")

    print(f"request : {request}")
    print(f"Client Name: {client_name}")
    print(f"Networks: {network}")
    print(f"Providers: {providers}")
    print(f"Public Key: {public_key}")
    print(f"API Key: {api_key}")

    try:
        response = client.create_client(client_name, network, providers, public_key, api_key)
        print("Response status code:", response.status_code)
        print("Response content:", response.content)
    except Exception as e:
        print(f"Error in client.create_client: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

    if response.status_code == 201:
        return jsonify({"message": "Client created successfully"}), 201
    else:
        return jsonify({"error": "Failed to create client"}), response.status_code

@app.route("/update_client/<client_name>", methods=['POST'])
def update_client(client_name):
    data = request.json
    updated_client_name = data['client']
    updated_providers = data['providers']

    response = client.update_client(client_name, updated_client_name, updated_providers)
    
    print(f"Update Client Response Status: {response.status_code}")
    print(f"Update Client Response Content: {response.content}")

    if response.status_code == 200:
        return jsonify({"message": "Client updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to update client", "details": response.json()}), response.status_code
    
@app.route('/signingClient/<client_name>', methods=['GET'])
def get_client(client_name):
    response = client.get_client(client_name)
    if response.ok:
        return jsonify(response.json())
    else: 
        return jsonify({'error': 'Client not found'}), 404

if __name__ == "__main__":
    app.run(debug=True)
