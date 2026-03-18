import Config as cfg
from bot_lib import logger_class,Singleton
from bot_lib.database.db import DbBot


@logger_class()
class DbModule(metaclass=Singleton):

    def jobs_pendentes(self):
        pass

