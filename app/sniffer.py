try:
    import scapy.all as scapy
except ImportError:
    print("[-] The scapy python module is required, but not installed.")
    exit(1)


class Sniffer:
    def __init__(self, interface):
        self.interface = interface

    def sniff(self):
        try:
            scapy.sniff(filter='ip', iface=self.interface, store=False, prn=self.process_packet)
        except PermissionError:
            raise PermissionError("Permission error: It is required to run the sniffer as sudo.")

    @staticmethod
    def process_packet(packet):
        if scapy.IP in packet:
            ip_src = packet[scapy.IP].src
            ip_dst = packet[scapy.IP].dst
            print(f"Source: {ip_src} Destination: {ip_dst}")