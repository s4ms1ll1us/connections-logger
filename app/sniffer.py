from .packet_info import PacketInfo
from .resolve_error import ResolveError
try:
    import scapy.all as scapy
except ImportError:
    print("[-] The scapy python module is required, but not installed.")
    exit(1)


class Sniffer:
    def __init__(self, interface, data_preparer, resolver):
        self.interface = interface
        self.data_preparer = data_preparer
        self.resolver = resolver

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
            self.data_preparer.add_packet_info(PacketInfo(src_ip, dst_ip))
            try:
                host = self.resolver.get_host(dst_ip)
                print(f"{host} has IP address {dst_ip}")
            except ResolveError:
                # TODO filter this
                print(f"Cannot resolve IP address {dst_ip}")
