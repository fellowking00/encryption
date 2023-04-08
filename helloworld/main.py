
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from flask import Flask, request


app = Flask(__name__)

@app.route('/encrypt')
def encryptt():
key = request.args.get('key', '')
card_no = request.args.get('card_no', '')

# Create RSA key object from public key
rsa_key = RSA.importKey(key)

# Create cipher object using PKCS1 v1.5 padding scheme
cipher = PKCS1_v1_5.new(rsa_key)

# Encrypt the card number using cipher
encrypted_card_no = cipher.encrypt(card_no.encode('utf-8'))

# Encode the encrypted message in base64
encoded_card_no = base64.b64encode(encrypted_card_no)

print(encoded_card_no.decode())

if __name__ == '__main__':

    app.run()
