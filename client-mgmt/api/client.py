import requests
from os import getenv
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask import session
import jwt
import logging, json, base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from functools import wraps


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

API_BASE_URL = "https://custody.arianee.com"
API_KEY = getenv("REACT_APP_API_KEY")
print(f"api key: {API_KEY} ")

def create_client(client_name, network, providers, public_key, api_key):
    url = f"{API_BASE_URL}/signingClient/create"
    headers = {
        'x-api-key': api_key,  # Use the API key from the parameter
        'Content-Type': 'application/json',
    }
    payload = {
        'client': client_name,
        'networks': [network],
        'providers': providers
    }
    
    if public_key:
        payload['publicKey'] = public_key

    response = requests.post(url, json=payload, headers=headers)
    return response



def submit_jwt(token, public_key):
    logger.debug(f"Received token: {token}")
    logger.debug(f"Received public key: {public_key}")

    try:
        # Load the public key
        key = serialization.load_pem_public_key(
            public_key.encode(),
            backend=default_backend()
        )
        logger.debug("Loaded Public Key Successfully")

        # Decode the JWT
        decoded = jwt.decode(token, key, algorithms=["RS256"])
        logger.debug(f"Decoded JWT: {json.dumps(decoded, indent=2)}")

        return {'success': True, 'message': 'JWT verified successfully', 'decoded': decoded}

    except jwt.ExpiredSignatureError:
        logger.error("JWT has expired")
        return {'success': False, 'message': 'JWT has expired'}
    except jwt.InvalidTokenError as e:
        logger.error(f"Invalid JWT: {str(e)}")
        return {'success': False, 'message': f'Invalid JWT: {str(e)}'}
    except Exception as e:
        logger.error(f"Error verifying JWT: {str(e)}")
        return {'success': False, 'message': f'Error verifying JWT: {str(e)}'}

def update_client(client_name, updated_client_name, updated_providers):
    url = f"{API_BASE_URL}/signingClient/update/{client_name}"
    headers = {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json'
    }
    payload = {
        'client': updated_client_name,
        'providers': updated_providers
    }
    response = requests.post(url, json=payload, headers=headers)
    print(payload)
    print(headers)
    print(response)
    return response

def get_client(client_name):
    url = f"{API_BASE_URL}/signingClient/{client_name}"
    headers = {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response