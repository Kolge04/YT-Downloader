import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6062022905:AAFjFdASrtYtMokfFwJwvtkgf0rhgG9Nlj0")

    APP_ID = int(os.environ.get("APP_ID", 12210813))

    API_HASH = os.environ.get("API_HASH", "e42eeae11a2f96bcfc5ec3b46a30adad")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "XaosResmii")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "XaosResmii")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
