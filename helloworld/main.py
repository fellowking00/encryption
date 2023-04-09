
import base64
import os

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from flask import Flask, request

app = Flask(__name__)
app.config['ENV'] = 'production' # Set Flask environment to production
app.debug = False # Disable debug mode

@app.route('/encrypt')
def encryptt():
    key = request.args.get('key', '')
    card_no = request.args.get('card_no', '')
   
    if not key or not card_no:
        return "Key and card_no query parameters are required.", 400

    try:
        rsa_key = RSA.import_key(key)
    except ValueError:
        return "Invalid key format. Please provide a valid RSA public key format.", 400

    cipher = PKCS1_v1_5.new(rsa_key)
    
    try:
        encrypted_card_no = cipher.encrypt(card_no.encode('utf-8'))
    except ValueError:
        return "Invalid card number. Please provide a valid credit card number.", 400

    encoded_card_no = base64.b64encode(encrypted_card_no).decode('utf-8')

    return encoded_card_no, 200

if __name__ == '__main__':
    app.run()
