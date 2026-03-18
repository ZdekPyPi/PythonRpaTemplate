import Config as cfg
from bot_lib import logger_class
from elawLib import Elaw
from pathlib import Path



@logger_class()
class ElawModule(Elaw):

    def __init__(self):
        super().__init__(
            user        = cfg.ElawConfig.email,
            password    = cfg.ElawConfig.password,
            driver_path = r"C:\chromedriver-win64\chromedriver.exe",
            logger      = cfg.logger
            )



   