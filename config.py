import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5812040555:AAGigOnZCAZHJDkLoOolrAq6CV5d5ZoP6JA")

    APP_ID = int(os.environ.get("APP_ID", " 22140808"))

    API_HASH = os.environ.get("API_HASH", "72e39b383c4655d957f67d4ab94cb3aa")
