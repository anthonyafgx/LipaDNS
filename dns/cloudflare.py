from dns.interface import DNSInterface

class CloudflareDNS(DNSInterface):
    def update_dns_record(self, new_ip: str) -> bool:
        
        
        return True