from dns.interface import DNSInterface
from exceptions import APIRequestError

import os
import requests
from typing import Any

class CloudflareDNS(DNSInterface):
    _zone_id: (str | None)

    def __init__(self, api_key:str, domain_name:str):
        # LOAD NS SERVICE ENV VARIABLES
        self._zone_id = os.getenv("CLOUDFLARE_ZONE_ID")
        if (self._zone_id == None or self._zone_id == ""):
            raise ValueError("CLOUDFLARE_ZONE_ID NOT DEFINED")
        return super().__init__(api_key=api_key, domain_name=domain_name)

    def update_dns_record(self, new_ip: str):
        # Get dns record id
        url: str = f"https://api.cloudflare.com/client/v4/zones/{self._zone_id}/dns_records"
        
        headers: dict[str,str] = {
            "Content-Type": "application/json",
            "X-Auth-Email": "",
            "Authorization": f"Bearer {self.api_key}"
        }

        parameters: dict[str,str] = {
            "name": self.domain_name,
            "type": "A"
        }

        response = requests.request("GET", url=url, headers=headers, params=parameters).json()

        if (not response["success"]):
            errors: dict[str,str] = response["errors"]
            raise APIRequestError(message=f"API request failed: {errors}",errors=errors)
        
        dns_record_id: str = response["result"][0]["id"]
        
        # Update dns record (updates the specified parts of the record. Use the Overwrite endpoint if you want to overwrite everything)
        url = f"https://api.cloudflare.com/client/v4/zones/{self._zone_id}/dns_records/{dns_record_id}"

        body: dict[str, Any] = {
            "content": new_ip,
            "name": self.domain_name,
            "type": "A",
            "comment": "Dynamic Record updated automatically by LupaDNS"
        }
        
        response = requests.request("PATCH", url=url, headers=headers, json=body).json()

        if (not response["success"]):
            errors: dict[str,str] = response["errors"]
            raise APIRequestError(message=f"API request failed: {errors}",errors=errors)

        return