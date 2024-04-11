from ip.interface import IPInterface

import requests

class Ipify(IPInterface):
    def scan_ipv4(self) -> str:
        return requests.get('https://api.ipify.org').text
    
    def scan_ipv6(self) -> str:
        return requests.get('https://api6.ipify.org').text