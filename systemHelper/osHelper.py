import os
from dotenv import load_dotenv


load_dotenv()

def GetEnvValue(key: str):
    return os.getenv(key)
