import os
import sys
import time

from datetime import date, datetime, timedelta

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_dir)

from comuns.notification_slack import send_notification, notify_slack_error
from driver.webDriver import webDriver

from dotenv import load_dotenv
load_dotenv()   


def process_filial():
        driver = webDriver()
        driver.get('https://example.com/')

        time.sleep(1000)        

        driver.quit()


if __name__ == "__main__":
        process_filial()
