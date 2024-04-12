from dns.interface import DNSInterface

import os

class CloudflareDNS(DNSInterface):
    _zone_id: (str | None)

    def __init__(self, api_key:str, domain_name:str):
        # LOAD NS SERVICE ENV VARIABLES
        self._zone_id = os.getenv("CLOUDFLARE_ZONE_ID")
        if (self._zone_id == None or self._zone_id == ""):
            raise ValueError("CLOUDFLARE_ZONE_ID NOT DEFINED")
        return super().__init__(api_key=api_key, domain_name=domain_name)

    def update_dns_record(self, new_ip: str) -> bool:
        
        
        return True