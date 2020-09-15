class DataCollector:
    def __init__(self):
        self.packet_infos = []

    def add_packet_info(self, packet_info):
        self.packet_infos.append(packet_info)

    def reset(self):
        self.packet_infos.clear()
