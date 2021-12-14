#!/usr/bin/env python

import configparser
import time
from alarm import AlarmModule, AlarmFactory
from temperatureutil.temperatureUtil import TemperatureUtil
from cpu_util import CpuUtil
from discspace_util import DiscSpaceUtil
from ram_util import RamUtil
from usermonitoring import UserMonitoring
from monitoring_data import MonitoringData
import sys


def main():

    # Parameters:
    # t = terminate/test
    valid_args = ["-t","-h"]
    args = sys.argv

    # Lade configdatei
    config = configparser.ConfigParser()
    config.read('config.ini')
    default_config = config["DEFAULT"]
    control_config = config["program_control"]

    logfile_url = default_config["logfileURL"]
    loglevel = default_config["loglevel"]

    log_interval = control_config["log_intervall"]

    is_loop = True

    for arg in args:
        if arg in valid_args:
            if arg == "-t":
                print("Starte im Testmodus.")
                is_loop = False
            if arg == "-h":
                print("Kommandozeilenparameter: \n" +
                "-t = Testfall programm wird nur einmal ausgeführt\n" + 
                "-h = Ausgabe der hilfe auf der Konsole\n" + 
                "Festlegung der Kontrollparameter in der Config.ini unter \"program_control\".\n" + 
                "discspace   = Kontrolle aller Festplaten auf Freienspeicher\n" +
                "ram         = Kontrolle des Ram's auf auslastung\n" +
                "cpu_temp    = Kontrolle der CPU Temperatur\n" +
                "cpu_use     = Kontrolle der CPU auslastung\n" +
                "user        = Kontrolle der einglogten User\n" +
                "log_intervall = Intervall in dem das Programm die Kontrolle durchführt")
                return    

    af = AlarmFactory(logfile_url, loglevel)
    af.get_alarm("").log(level="DEBUG", message="Hello World")

    # Anstelle der AlarmFactory wird nu noch das AlamModule ben�tigt
    am = AlarmModule(logfile_url, loglevel)

    tempuse = TemperatureUtil
    cpuuse = CpuUtil
    diskspacer = DiscSpaceUtil
    ramuse = RamUtil
    monitoringdata = MonitoringData(None, None)
    
    # loop
    while True:
        # Speichernutzung Festplatte
        if control_config.getboolean("discspace"):
            monitoringdata = diskspacer.discspace(config)
            monitoringdata.testPrinter()
            am.log(monitoringdata)
        # Arbeitsspeicher
        if control_config.getboolean("ram"):
            monitoringdata = ramuse.ramused(config)
            monitoringdata.testPrinter()
            am.log(monitoringdata)
        # Temperatur
        if control_config.getboolean("cpu_temp"):
            monitoringdata = tempuse.cputemperature(config)
            am.log(monitoringdata)
            monitoringdata.testPrinter()
        # CPU Auslastung
        if control_config.getboolean("cpu_use"):
            monitoringdata = cpuuse.cpuused(config)
            am.log(monitoringdata)
            monitoringdata.testPrinter()
        # Angemeldete User
        if control_config.getboolean("user"):
            users_data = UserMonitoring.get_logged_in_users()
            am.log(log_level="INFO", data=users_data)
        if not is_loop:
            return
        time.sleep(int(log_interval))
        # loop


if __name__ == "__main__":
    main()
