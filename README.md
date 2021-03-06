# Docker-Wireguard-KeyGen
## How to run
### *** Requirements *** 
- Docker or orchestration like Docker Swarm or Kubernetes

### *** Starting container ***
- Open a Command Line Interface (CLI).
- Clone Git repository (git clone https://github.com/MVDB0110/Docker-Wireguard-KeyGen)
- Build the docker image (eg. 'docker build -t docker-wireguard-keygen .')
- Start a container instance (eg. 'docker run -d -p 80:80 docker-wireguard-keygen')

## Query Parameters
Clients: Number of clients which must be generated.

## Example Response:
`http://<ip>:<port>/?clients=3`
```
{
	"Code": 200,
	"Data": [{
		"Client": 0,
		"Config": "W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjAuMC4yLzI0Ckxpc3RlblBvcnQgPSA1MTgyMApQcml2YXRlS2V5ID0gU0VDaFBqWUhZVEd5d0xVenRQejJob0dtYnZmSHVNaFdDajFlditkSG4wMD0KCltQZWVyXQpQdWJsaWNLZXkgPSB5cncvd1BvT1BpY3U3WDlENEI3YkhoRWJsL0VDTWdqenJxRFhUa0pzUlFZPQpFbmRwb2ludCA9IApBbGxvd2VkSVBzID0gMC4wLjAuMC8wCg==",
		"Private": "SEChPjYHYTGywLUztPz2hoGmbvfHuMhWCj1ev+dHn00=",
		"Public": "gNQOHgFgMLIcOxHlpuMqWlFn6+O8PvHo6CIwKDPe8Eg=",
		"Type": "Client"
	}, {
		"Client": 1,
		"Config": "W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjAuMC4zLzI0Ckxpc3RlblBvcnQgPSA1MTgyMApQcml2YXRlS2V5ID0gZUNwTU9NQXNEbkltUk1RNzNGbnR5cEtiMGxkNGgyNXpocUI5TTUxYWVIaz0KCltQZWVyXQpQdWJsaWNLZXkgPSB5cncvd1BvT1BpY3U3WDlENEI3YkhoRWJsL0VDTWdqenJxRFhUa0pzUlFZPQpFbmRwb2ludCA9IApBbGxvd2VkSVBzID0gMC4wLjAuMC8wCg==",
		"Private": "eCpMOMAsDnImRMQ73FntypKb0ld4h25zhqB9M51aeHk=",
		"Public": "dXrlIc1IZ+7MUXuJydMdrvFpxTgR634LKbuYlASoaR0=",
		"Type": "Client"
	}, {
		"Client": 2,
		"Config": "W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjAuMC40LzI0Ckxpc3RlblBvcnQgPSA1MTgyMApQcml2YXRlS2V5ID0gY0xYRlFNQTVnWm9YNnFaTHZscEtZQTNaak9UODkvMi9MZUtRREZha3dHdz0KCltQZWVyXQpQdWJsaWNLZXkgPSB5cncvd1BvT1BpY3U3WDlENEI3YkhoRWJsL0VDTWdqenJxRFhUa0pzUlFZPQpFbmRwb2ludCA9IApBbGxvd2VkSVBzID0gMC4wLjAuMC8wCg==",
		"Private": "cLXFQMA5gZoX6qZLvlpKYA3ZjOT89/2/LeKQDFakwGw=",
		"Public": "M6G3SaftOrC8nchCwBXXek0XzveEmRhW6IM4Gscoa2w=",
		"Type": "Client"
	}, {
		"Config": "W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjAuMC4xLzI0Ckxpc3RlblBvcnQgPSA1MTgyMApQcml2YXRlS2V5ID0gd0tZWDdqaU5qQ2wxL29EVkdQMUNlZlR3YW8wTjBlemVHdEg2YnNKVmIwRT0KUG9zdFVwID0gaXB0YWJsZXMgLUEgRk9SV0FSRCAtaSAlaSAtaiBBQ0NFUFQ7IGlwdGFibGVzIC10IG5hdCAtQSBQT1NUUk9VVElORyAtbyBldGgwIC1qIE1BU1FVRVJBREUKUG9zdERvd24gPSBpcHRhYmxlcyAtRCBGT1JXQVJEIC1pICVpIC1qIEFDQ0VQVDsgaXB0YWJsZXMgLXQgbmF0IC1EIFBPU1RST1VUSU5HIC1vIGV0aDAgLWogTUFTUVVFUkFERQoKW1BlZXJdClB1YmxpY0tleSA9IGdOUU9IZ0ZnTUxJY094SGxwdU1xV2xGbjYrTzhQdkhvNkNJd0tEUGU4RWc9CkFsbG93ZWRJUHMgPSAxMC4wLjAuMi8yNAoKW1BlZXJdClB1YmxpY0tleSA9IGRYcmxJYzFJWis3TVVYdUp5ZE1kcnZGcHhUZ1I2MzRMS2J1WWxBU29hUjA9CkFsbG93ZWRJUHMgPSAxMC4wLjAuMy8yNAoKW1BlZXJdClB1YmxpY0tleSA9IE02RzNTYWZ0T3JDOG5jaEN3QlhYZWswWHp2ZUVtUmhXNklNNEdzY29hMnc9CkFsbG93ZWRJUHMgPSAxMC4wLjAuNC8yNAoK",
		"Private": "wKYX7jiNjCl1/oDVGP1CefTwao0N0ezeGtH6bsJVb0E=",
		"Public": "yrw/wPoOPicu7X9D4B7bHhEbl/ECMgjzrqDXTkJsRQY=",
		"Server": 1,
		"Type": "Server"
	}],
	"Message": "Wireguard keys generated"
}
```
## Knowledge
### *** Wireguard ***
- https://www.wireguard.com/quickstart/
- https://upcloud.com/community/tutorials/get-started-wireguard-vpn/
