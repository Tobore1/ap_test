from networkscan import Networkscan
class R_Ping:
    def __init__(self, network = "192.168.150.1"):
        self.network = network
    def scan(self):
        print("Scanning...")
        network = Networkscan(self.network)
        network.run()
        for host in network.list_of_hosts_found:
            if host == self.network:
                return "Radio is working"
            else:
                return "Radio is not working"

works = R_Ping().scan()

if __name__ == "__main__":
    pass
