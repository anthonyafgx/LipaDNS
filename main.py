import os

from dns.interface import DNSInterface
from dns.cloudflare import CloudflareDNS

def main(dns: DNSInterface):
    pass

if __name__ == "__main__":
    api_key: (str | None) = os.getenv('API_KEY')
    domain_name: (str | None) = os.getenv('DOMAIN_NAME')
    
    if (api_key == None): 
        raise ValueError("API_KEY not defined")

    if (domain_name == None):
        raise ValueError("DOMAIN_NAME not deinfed")

    dns = CloudflareDNS(api_key=api_key, domain_name=domain_name)
    
    main(dns=dns)