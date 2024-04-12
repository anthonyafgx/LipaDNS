import os
from dotenv import load_dotenv
import time

from dns.interface import DNSInterface
from dns.cloudflare import CloudflareDNS
from ip.interface import IPInterface
from ip.ipify import Ipify

def main(dns: DNSInterface, ip: IPInterface):
    update_interval: float = float(os.getenv(key="UPDATE_INTERVAL_SECONDS",default=60.0))
    last_ip: str = ""
    while True:
        new_ip: str = ip.scan_ipv4()
        if (last_ip != new_ip):
            dns.update_dns_record(new_ip=new_ip)
        time.sleep(update_interval)

if __name__ == "__main__":
    load_dotenv()
    
    api_key: (str | None) = os.getenv('API_KEY')
    domain_name: (str | None) = os.getenv('DOMAIN_NAME')
    
    # GENERAL ENV VARIABLES
    if (api_key == None or api_key == ""): 
        raise ValueError("API_KEY not defined")

    if (domain_name == None or domain_name == ""):
        raise ValueError("DOMAIN_NAME not deinfed")

    dns = CloudflareDNS(api_key=api_key, domain_name=domain_name)
    ip = Ipify()
    main(dns=dns, ip=ip)