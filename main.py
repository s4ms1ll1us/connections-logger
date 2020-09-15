#!/usr/bin/env python3

from app import Configurator
from app import Sniffer


def main():
    configurator = Configurator()
    try:
        interface = configurator.get_interface()
    except ValueError:
        print("[-] No interface specified. Please set one with option -i.")
        exit(1)

    sniffer = Sniffer(interface)
    try:
        sniffer.sniff()
    except PermissionError:
        print("[-] It is required to run the sniffer as sudo.")


if __name__ == '__main__':
    main()
