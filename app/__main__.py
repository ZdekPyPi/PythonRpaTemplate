import Config as cfg
from bot_lib import Task,terminal_opt
from Modules.elaw import ElawModule
from Modules.db import DbModule

# from Models import *

@Task.config(task_name="TASK_NAME",local=True)
def main():
    elaw,db = ElawModule(),DbModule()

    cfg.logger.success("1 - Verificando Lista de Tarefas no ELAW")
    cfg.logger.info("\tLogin Elaw")
    elaw.start_elaw()
    cfg.logger.info("\tLendo Tarefas")
    #elaw.captura_tarefas()

    cfg.logger.success("2 - Capturando tarefas Pendentes")
    jobs = db.jobs_pendentes()


    cfg.logger.info("configuracao feita")

    cfg.logger.bind_extra("N Contrato")
    cfg.logger.success("2 - STEPS")
    cfg.logger.info("passo 2 aqui")

    cfg.logger.bind_extra(None)
    cfg.logger.success("3 - AVISANDO POR GOOGLE CHAT")


if __name__ ==  "__main__":
    terminal_opt()



    

    
    


