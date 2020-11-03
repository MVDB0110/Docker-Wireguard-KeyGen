from flask import Flask, request
import wgtools
import base64

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
        byte_string = generate_server_config(priv=private_key,pub=public_key).encode('ascii')
        base64_bytes = base64.b64encode(byte_string)
        config = base64_bytes.decode('ascii')
        key_list.append({"Type": "Server", "Server": i, "Private": private_key, "Public": public_key, "Config": config})

    for i in range(0,client_count):
        public_key, private_key = wgtools.keypair()
        key_list.append({"Type": "Client", "Client": i, "Private": private_key, "Public": public_key })
    
    result = {
    "Code" : 200,
    "Message" : "Wireguard keys generated",
    "Data": key_list,
    }

    return result

def generate_server_config(priv,pub):
    config = "[Interface]\n"
    config += "Address = 10.0.0.1/24\n"
    config += "ListenPort = 51820\n"
    config += "PrivateKey = " + priv + "\n"
    config += "PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE\n"
    config += "PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE\n"
    config += "\n"
    config += "[Peer]\n"
    config += "PublicKey = " + pub + "\n"
    config += "AllowedIPs = 10.0.0.0/24\n"
    return config

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)