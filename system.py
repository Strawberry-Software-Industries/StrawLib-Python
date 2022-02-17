import psutil
import os
import sys
import socket

class network:

        def ip_address():
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]


class memory:
    
    def usage():
        return int(psutil.virtual_memory().total - psutil.virtual_memory().available)


class cpu:

    def usage():
        return psutil.cpu_percent()