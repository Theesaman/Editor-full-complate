import requests

from environs import Env
# evnironvs kutubxonasidan foydalanish

env = Env()
env.read_env()


def send_message(text):
    BOT_TOKEN = env.str("BOT_TOKEN")
    CHAT_ID = env.str("CHAT_ID")
    PHOTO = "https://help.apple.com/assets/65A999AC13B61AFE4806A611/65A999AE157993C0D60EEF70/en_US/5c55a7fe0ab609058db1fc2bf1a365ee.png"
    TEXT = text
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendphoto?chat_id={CHAT_ID}&photo={PHOTO}&caption={TEXT}"
    response = requests.get(url)
    # print(response.status_code)