from dns.interface import DNSInterface

import os
import requests

class CloudflareDNS(DNSInterface):
    _zone_id: (str | None)

    def __init__(self, api_key:str, domain_name:str):
        # LOAD NS SERVICE ENV VARIABLES
        self._zone_id = os.getenv("CLOUDFLARE_ZONE_ID")
        if (self._zone_id == None or self._zone_id == ""):
            raise ValueError("CLOUDFLARE_ZONE_ID NOT DEFINED")
        return super().__init__(api_key=api_key, domain_name=domain_name)

    def update_dns_record(self, new_ip: str) -> bool:
        # Check if domain exists
        url: str = f"https://api.cloudflare.com/client/v4/zones/{self._zone_id}/dns_records"
        
        headers: dict[str,str] = {
            "Content-Type": "application/json",
            "X-Auth-Email": ""
        }

        parameters: dict[str,str] = {
            "name": self.domain_name
        }

        response = requests.request("GET", url=url, headers=headers, params=parameters)

        # if (response.json)

        return True