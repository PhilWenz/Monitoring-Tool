from alarm import *
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import configparser


class EmailAlarm(Alarm):
    
    login: str
    host: str
    target_addr: str
    password: str
    ssl_port = 465
    logger: LogAlarm

    # Lade configdatei
    config = configparser.ConfigParser()
    config.read('config.ini')
    default_config = config["DEFAULT"]
    email_config = config["email"]

    def __init__(self, logger: LogAlarm) -> None:
        super()
        self.logger = logger
        self.host = self.email_config["host"]
        self.login = self.email_config["login"]
        self.password = self.email_config["password"]
        self.target_addr = self.email_config["target_email"]

    def build_message(self, msg):
        message = MIMEMultipart('mixed')
        message['From'] = 'Contact <{sender}>'.format(sender=self.login)
        message['To'] = self.target_addr
        message['Subject'] = msg
        msg_content = f'<h4>ACHTUNG: Ein harter Schwellenwert wurde überschritten<br> {msg}</h4>\n'
        body = MIMEText(msg_content, 'html')
        message.attach(body)
        logfile = self.default_config["logfileURL"]
        try:
            with open(logfile, "rb") as attachment:
                p = MIMEApplication(attachment.read(), _subtype="pdf")
                p.add_header('Content-Disposition', "attachment; filename= %s" % logfile.split("/")[-1])
                message.attach(p)
        except Exception as e:
            print(str(e))
        return message.as_string()

    def send(self, message: str) -> None:
        context = ssl.create_default_context()

        with smtplib.SMTP(host=self.host, port=25) as server:
            try:
                server.ehlo()
                #server.starttls(context=context)
                #server.ehlo()
                #server.login(user=self.login, password=self.password)
                #server.ehlo()
                server.sendmail(self.login, self.target_addr, message)

            except Exception as e:
                raise e
            finally:
                server.quit()

    def log(self, level, message, value, soft_threshold, hard_threshold) -> None:
        if value >= hard_threshold:
            self.logger.log(level="CRITICAL", message=message)
            try:
                attachment = open("logs/monitor.log")
                #self.send(f"Subject: Kritische Warnung vom Server\n\n{message}")
                self.send(self.build_message(message))
                self.logger.log(level="INFO", message="Email versendet.")
            except Exception as e:
                self.logger.log(level="ERROR", message="Die Email konnte nicht verschickt werden.")

        elif value >= soft_threshold:
            self.logger.log(level="WARNING", message=message)
        else:
            self.logger.log(level=level, message=message)
