class DataCollector:
    def __init__(self, resolver):
        self.__resolver = resolver
        self.__packet_infos = []

    def update_packet_info(self, packet_info):
        # Currently only destination ips are interesting.
        new_dst_ip = packet_info.dst_ip
        location_info = self.__resolver.get_location_info(new_dst_ip)
        if location_info is None:
            return
        for info in self.__packet_infos:
            if info.dst_ip == new_dst_ip:
                return
        self.__packet_infos.append(packet_info)
        print(f"The IP address {new_dst_ip} is from {location_info['city']} "
              f"({location_info['region']}/{location_info['country']}).")

    def reset(self):
        self.__packet_infos.clear()
