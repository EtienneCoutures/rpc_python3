from http_rpc_client import Client

if __name__ == "__main__":
    c = Client("127.0.0.1:3000")
    print(c.hdd())
    print("-->")
    print(type(c.hdd()))
