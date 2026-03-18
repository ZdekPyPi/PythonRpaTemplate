from sheets_lib import SheetsLib
from bot_lib import logger_class
from dateUts import *
import Config as cfg


@logger_class()
class Sheets(SheetsLib):
    ultima_linha = None

    def __init__(self):
        cfg.logger.success("==== INIT SHEETS ====")
        self.connectDrive(authDict=cfg.GoogleServiceVault.__dict__,isServiceAccount=True)

    def UPDATE_SHEETS(self,df):
        cfg.logger.info("\tINSERINDO DADOS")
        self.ultima_linha = len(df)
        df = df.values.tolist()
        self.setRange(cfg.SheetsConfig.ID,f"Processamento!D2:D{self.ultima_linha}",df,mode="ROWS")