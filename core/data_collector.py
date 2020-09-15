class DataCollector:
    def __init__(self, resolver):
        self.__resolver = resolver
        self.__connections = []

    def update_connection_endpoints(self, connection):
        # Currently only destination ips are interesting.
        new_dst_ip = connection.dst_ip
        location_info = self.__resolver.get_location_info(new_dst_ip)
        if location_info is None:
            return
        for info in self.__connections:
            if info.dst_ip == new_dst_ip:
                return
        self.__connections.append(connection)
        # TODO extract this to dedicated class
        print(f"The IP address {new_dst_ip} is from {location_info['city']} "
              f"({location_info['region']}/{location_info['country']}).")

    def reset(self):
        self.__connections.clear()
