import argparse


class Configuration:
    @staticmethod
    def get_interface():
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--interface", dest="interface", help="Specify which interface to use")
        arguments = parser.parse_args()
        if arguments.interface is None:
            raise ValueError("Interface option is not set")
        return arguments.interface
