import os

def OpenFileRead(filePath: str, fileCode: str):
    return open(filePath, fileCode)

def getBaseName(path: str):
    return os.path.basename(path)