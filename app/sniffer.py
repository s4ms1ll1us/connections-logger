from .packet_info import PacketInfo
try:
    import scapy.all as scapy
except ImportError:
    print("[-] The scapy python module is required, but not installed.")
    exit(1)


class Sniffer:
    def __init__(self, interface, data_preparer):
        self.interface = interface
        self.data_preparer = data_preparer

    def sniff(self):
        self.data_preparer.reset()
        try:
            scapy.sniff(filter='ip', iface=self.interface, store=False, prn=self.__process_packet)
        except PermissionError:
            raise PermissionError("Permission error: It is required to run the sniffer as sudo.")

    def __process_packet(self, packet):
        if scapy.IP in packet:
            src_ip = packet[scapy.IP].src
            dst_ip = packet[scapy.IP].dst
            self.data_preparer.update_packet_info(PacketInfo(src_ip, dst_ip))
