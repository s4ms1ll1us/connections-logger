#!/usr/bin/env python3

from core import Configuration
from core import Sniffer
from core import DataCollector
from core import Resolver


def main():
    configuration = Configuration()
    interface = ''
    try:
        interface = configuration.get_interface()
    except ValueError:
        print("[-] No interface specified. Please set one with option -i.")
        exit(1)

    resolver = Resolver()
    data_collector = DataCollector(resolver)
    sniffer = Sniffer(interface, data_collector)
    try:
        sniffer.sniff()
    except PermissionError:
        print("[-] No permissions to capture packets on the specified interface."
              "You may have to run it with sudo privileges.")


if __name__ == '__main__':
    main()
