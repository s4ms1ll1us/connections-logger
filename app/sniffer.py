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
            scapy.sniff(iface=self.interface, store=False, prn=self.process_packet)
        except PermissionError:
            raise PermissionError("Permission error: It is required to run the sniffer as sudo.")

    @staticmethod
    def process_packet(packet):
        print(f"Direction: {packet.direction} Destination: {packet.dst}")
