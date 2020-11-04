from flask import Flask, request
import wgtools
import base64

app = Flask(__name__)

@app.route('/')
def keys():
    key_list = []
    client_public_key_list = []

    if request.args.get('clients') is not None:
        client_count = int(request.args.get('clients'))
    else:
        client_count = 1
    
    server_public_key, server_private_key = wgtools.keypair()

    for i in range(0,client_count):
        public_key, private_key = wgtools.keypair()
        client_public_key_list.append({"Client": i, "Public": public_key})
        byte_string = generate_client_config(clientnr=i,priv=private_key,pub=server_public_key).encode('ascii')
        base64_bytes = base64.b64encode(byte_string)
        config = base64_bytes.decode('ascii')
        key_list.append({"Type": "Client", "Client": i, "Private": private_key, "Public": public_key, "Config": config })
    
    byte_string = generate_server_config(priv=server_private_key,pub_list=client_public_key_list).encode('ascii')
    base64_bytes = base64.b64encode(byte_string)
    config = base64_bytes.decode('ascii')
    key_list.append({"Type": "Server", "Server": 1, "Private": server_private_key, "Public": server_public_key, "Config": config})
    
    result = {
    "Code" : 200,
    "Message" : "Wireguard keys generated",
    "Data": key_list,
    }

    return result

def generate_client_config(clientnr,priv,pub):
    config = "[Interface]\n"
    config += "Address = 10.0.0." + str(clientnr+2) + "/24\n"
    config += "ListenPort = 51820\n"
    config += "PrivateKey = " + priv + "\n"
    config += "\n"
    config += "[Peer]\n"
    config += "PublicKey = " + pub + "\n"
    config += "Endpoint = \n"
    config += "AllowedIPs = 0.0.0.0/0\n"
    return config

def generate_server_config(priv,pub_list):
    config = "[Interface]\n"
    config += "Address = 10.0.0.1/24\n"
    config += "ListenPort = 51820\n"
    config += "PrivateKey = " + priv + "\n"
    config += "PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE\n"
    config += "PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE\n"
    config += "\n"
    for i in pub_list:
        config += "[Peer]\n"
        config += "PublicKey = " + i['Public'] + "\n"
        config += "AllowedIPs = 10.0.0." + str(i["Client"]+2) + "/24\n"
        config += "\n"
    return config

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)