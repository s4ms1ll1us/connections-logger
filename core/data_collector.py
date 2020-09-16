class DataCollector:
    def __init__(self, resolver):
        self.__resolver = resolver
        self.__endpoints = []
        self.__not_resolvable = []

    def update_endpoint(self, endpoint):
        new_dst_ip = endpoint
        if self.__should_be_ignored(new_dst_ip):
            return
        location_info = self.__resolver.get_location_info(new_dst_ip)
        if location_info is None:
            self.__not_resolvable.append(endpoint)
            return

        self.__endpoints.append(endpoint)

        # TODO extract this to dedicated class
        print(f"Connected to {new_dst_ip} which is located in {location_info['city']} "
              f"({location_info['region']}/{location_info['country']}).")

    def reset(self):
        self.__endpoints.clear()

    def __should_be_ignored(self, ip):
        resolver_ip = self.__resolver.get_location_resolver_ip()
        if ip == resolver_ip:
            return True
        if ip in self.__endpoints:
            return True
        if ip in self.__not_resolvable:
            return True
        return False
