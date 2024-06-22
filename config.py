import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("6404071975:AAEbK9IjI7bA2GtTc3cx_kH0BtRy3okBK8Y", "")

    APP_ID = int(os.environ.get("APP_ID", 21627756))

    API_HASH = os.environ.get("API_HASH", "fe77fbf0cae9f7f5ece37659e2466cf1")
