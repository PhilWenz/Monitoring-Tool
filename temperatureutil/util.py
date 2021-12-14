from abc import ABC, abstractmethod


class Util:

    @staticmethod
    @abstractmethod
    def get_cpu_temp():
        print("abstract method")