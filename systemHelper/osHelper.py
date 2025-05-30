import os
from dotenv import load_dotenv


load_dotenv()

def getEnvValue(key: str):

    if key == '':
        return ''

    return os.getenv(key)
