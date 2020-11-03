# Docker-Wireguard-KeyGen
## Query Parameters
Clients: Number of clients which must be generated.\
Servers: Number of servers which must be generated.

## Example Response:
'http://<ip>:<port>/?clients=3&servers=2'
```
{
	"Code": 200,
	"Data": [{
		"Private": "WOjaHmy3d8ij11ldF/13bAe1amidgfcsr2QnR9gQc0k=",
		"Public": "SYGR76Alumi3ZvW+ZQ6X2W32npjiWjCOXhwFzgB7uTw=",
		"Server": 0,
		"Type": "Server"
	}, {
		"Private": "qKfiGCPvE+Jm8JH3abuqts9QAX0ZuzTzCRlmFLdtWUQ=",
		"Public": "W56xKYVsVDmt/lFlJUXDpi+6S9ySpp0XJCnViI4ldQU=",
		"Server": 1,
		"Type": "Server"
	}, {
		"Client": 0,
		"Private": "INm+8jMuV6JfiLjhV7xNMDty7/I4GBbcKfmNMTg2BHQ=",
		"Public": "2k08L34Rcu+GgE7IeI9csPDcIC9Xu2ZGoD8Iv68EH1k=",
		"Type": "Client"
	}, {
		"Client": 1,
		"Private": "uBDccQqh0EvBIgdawRnFtLaai04bJZutaCAI/ZTOZEo=",
		"Public": "ERsrxvhJVywVMXWJWtCAa0XmDw/0R1BPYPyosSImCTY=",
		"Type": "Client"
	}, {
		"Client": 2,
		"Private": "+IFBiFBWsY92lzx6UVlPc71ubxx/IKBp3d0uZ39cpVI=",
		"Public": "ZODrhOIP8eyPr1gsR/zNk/vhW3HbmeJtiRtDF81+IU4=",
		"Type": "Client"
	}],
	"Message": "Wireguard keys generated"
}
```
