from bot_lib import Task,logger


@Task.new(name="TASK_NAME",local=True)
def main():
    logger.info("configuracao feita")

    logger.bind_extra("N Contrato")
    logger.success("2 - STEPS")
    logger.info("passo 2 aqui")

    logger.bind_extra(None)
    logger.success("3 - AVISANDO POR GOOGLE CHAT")



if __name__ ==  "__main__":
    main()



    

    
    


