import socket
from .resolve_error import ResolveError


class Resolver:
    @staticmethod
    def get_host(ip):
        try:
            host = socket.gethostbyaddr(ip)
        except socket.herror:
            raise ResolveError("Cannot resolve the ip address.")

        if len(host) > 0 and host[0] is not None:
            return host[0]
