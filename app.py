from flask import Flask, request
import wgtools

app = Flask(__name__)

@app.route('/')
def keys():
    key_list = []

    if request.args.get('clients') is not None:
        client_count = int(request.args.get('clients'))
    else:
        client_count = 1
    
    if request.args.get('servers') is not None:
        server_count = int(request.args.get('servers'))
    else:
        server_count = 1
    
    for i in range(0,server_count):
        public_key, private_key = wgtools.keypair()
        key_list.append({"Type": "Server", "Server": i, "Private": private_key, "Public": public_key })

    for i in range(0,client_count):
        public_key, private_key = wgtools.keypair()
        key_list.append({"Type": "Client", "Client": i, "Private": private_key, "Public": public_key })
    
    result = {
    "Code" : 200,
    "Message" : "Wireguard keys generated",
    "Data": key_list,
    }

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)