#!/usr/bin/env python3

from app import Configuration
from app import Sniffer
from app import DataCollector
from app import Resolver


def main():
    configuration = Configuration()
    try:
        interface = configuration.get_interface()
    except ValueError:
        print("[-] No interface specified. Please set one with option -i.")
        exit(1)

    data_collector = DataCollector()
    resolver = Resolver()
    sniffer = Sniffer(interface, data_collector, resolver)
    try:
        sniffer.sniff()
    except PermissionError:
        print("[-] No permissions to capture packets on the specified interface."
              "You may have to run it with sudo privileges.")


if __name__ == '__main__':
    main()
