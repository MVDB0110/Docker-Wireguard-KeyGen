from flask import Flask
import wgtools

app = Flask(__name__)

@app.route('/')
def home():
    public_key, private_key = wgtools.keypair()
    if public_key is not None and private_key is not None:
        result = {
        "Code" : 200,
        "Message" : "Wireguard key generated",
        "Data": {
            "Private": private_key,
            "Public": public_key
        },
        }
    else:
        result = {
        "Code" : 203,
        "Message" : "No content",
        "Data": None
        }
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)