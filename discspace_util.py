import psutil
from monitoring_data import MonitoringData


class DiscSpaceUtil:

    @staticmethod
    def discspace(config) -> MonitoringData:
        drive_config = config["harddrive"]
        msg_config = config["logmsg"]
        soft_max_discspace = float(drive_config["max_discspace1"])
        hard_max_discspace = float(drive_config["max_discspace2"])
        psutool = psutil.disk_partitions()
        discspace_value = dict()
        discspace_message = dict()
        disc_freespace: float
        disc_message: str
        disc_space_level: str = "INFO"

        for drive in psutool:
            disc_space_level = "INFO"
            disc_freespace = psutil.disk_usage(drive.device).percent
            discspace_value.update({drive.device: str(disc_freespace)})
            if soft_max_discspace <= disc_freespace < hard_max_discspace:
                disc_space_level = "WARNING"
                disc_message = msg_config[disc_space_level] + " auf: " + drive.device + " " \
                               + str(round(disc_freespace, 2)) + "% des Speichers belegt "
                discspace_message.update({drive.device: disc_message})
                disc_space_level = "WARNING"
            if disc_freespace > hard_max_discspace:
                disc_space_level = "CRITICAL"
                disc_message = msg_config[disc_space_level] + " auf:" + drive.device + " " \
                               + str(round(disc_freespace, 2)) + "% des Speichers belegt"
                discspace_message.update({drive.device: disc_message})

        monitordata = MonitoringData(values=discspace_value, messages=discspace_message,
                                     soft_threshold=soft_max_discspace,
                                     hard_threshold=hard_max_discspace,
                                     log_level=disc_space_level)
        return monitordata
