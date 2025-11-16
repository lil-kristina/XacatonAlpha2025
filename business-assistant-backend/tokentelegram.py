from dotenv import load_dotenv
import os
from os.path import join, dirname

def get_from_env(key):
    dotenv_path = join(dirname(__file__), 'token_env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)

token ="YOUR_TELEGRAM_BOT_TOKEN_HERE"
