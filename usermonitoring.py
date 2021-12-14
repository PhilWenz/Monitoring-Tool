import psutil
from monitoring_data import MonitoringData


class UserMonitoring:

    @staticmethod
    def get_logged_in_users() -> MonitoringData:
        users = psutil.users()
        values = {}
        messages = {}
        for user in users:
            messages[user.name] = f"name='{user.name}', terminal='{user.terminal}', host='{user.host}', started={user.started}, pid={user.pid}"

        data = MonitoringData(values=values, messages=messages)
        return data
