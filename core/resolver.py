from urllib.request import urlopen
import json
import socket


class Resolver:
    def get_location_info(self, ip):
        data = self.__get_data(ip)
        # It is assumed that the data is always complete
        if 'country' in data and 'region' in data and 'city' in data:
            return {
                'country': data['country'],
                'region': data['region'],
                'city': data['city']
            }

    def get_location_resolver_ip(self):
        domain = self.__get_domain()
        return socket.gethostbyname(domain)

    def __get_data(self, ip):
        url = self.__create_url(ip)
        response = urlopen(url)
        return json.load(response)

    def __create_url(self, ip):
        domain = self.__get_domain()
        return f"https://{domain}/{ip}/json"

    @staticmethod
    def __get_domain():
        return "ipinfo.io"
