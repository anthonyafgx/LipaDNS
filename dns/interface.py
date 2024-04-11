from abc import ABC, abstractmethod

class DNSInterface(ABC):
    @property
    def api_key(self) -> str:
        return self._api_key
    
    @api_key.setter
    def api_key(self, value: str):
        self._api_key = value

    @property
    def domain_name(self) -> str:
        return self._domain_name
    
    @domain_name.setter
    def domain_name(self, value: str):
        self._domain_name = value

    def __init__(self, api_key:str, domain_name:str):
        self.api_key = api_key
        self.domain_name = domain_name
    
    @abstractmethod
    def update_dns_record(self, new_ip: str) -> bool:
        '''
        @parameter new_ip: ipv4 string
        @returns tries getting the ip for one minute.
                If successful, TRUE
                If timeout, FALSE
        '''
        return