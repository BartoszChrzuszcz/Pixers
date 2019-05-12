import os


class ChromedriverPath:
    absFilePath = os.path.abspath(__file__)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    CHROMEDRIVER_PATH = os.path.join(parentDir, 'chromedriver.exe')
