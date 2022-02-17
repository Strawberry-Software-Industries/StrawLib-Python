import os
import sys

class config:

    def read(cfg_file=""):
        with open(cfg_file, "r") as f:
            data = f.read()

        print(data.rstrip())

    def write(cfg_file="", context=""):
        f = open(cfg_file, "w")
        f.write(context)
        f.close


class file:
    
    def delete(file=""):
        os.remove(file)


    def create(file=""):
        open(file, "x")