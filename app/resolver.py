from urllib.request import urlopen
import json


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

    def __get_data(self, ip):
        url = self.__create_url(ip)
        response = urlopen(url)
        return json.load(response)

    @staticmethod
    def __create_url(ip):
        return f"https://ipinfo.io/{ip}/json"
