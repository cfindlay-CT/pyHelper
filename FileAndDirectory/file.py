import os

def OpenFile(filePath: str, accessCode: str):
    return os.open(filePath, accessCode)