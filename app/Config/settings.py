from bot_lib import botConfig
from iniUts import *

#===================== POPULA AS CLASSES DE CONFIGURACAO 
ini =  IniUts(
    "./app/Config/ini/configs_prd.ini",
    "./app/Config/ini/configs_dev.ini",
    in_prd         = botConfig.is_in_prd,
    encryption_key = os.getenv('ENCRIPTION_KEY')
    )

@ini.link("ELAW")
class ElawConfig:
    email :str
    password :str


pass