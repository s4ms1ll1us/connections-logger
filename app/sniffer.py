from .connection_endpoints import ConnectionEndpoints
try:
    import scapy.all as scapy
except ImportError:
    print("[-] The scapy python module is required, but not installed.")
    exit(1)


class Sniffer:
    def __init__(self, interface, data_collector):
        self.__interface = interface
        self.__data_collector = data_collector

    def sniff(self):
        self.__data_collector.reset()
        try:
            scapy.sniff(filter='ip', iface=self.__interface, store=False, prn=self.__process_packet)
        except PermissionError:
            raise PermissionError("Permission error: It is required to run the sniffer as sudo.")

    def __process_packet(self, packet):
        if 'IP' in packet:
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst
            self.__data_collector.update_connection_endpoints(ConnectionEndpoints(src_ip, dst_ip))
