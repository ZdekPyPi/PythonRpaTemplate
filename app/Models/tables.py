import sqlalchemy as sa
from bot_lib.database.base import Base

class Tarefa(Base):
    __tablename__ = 'minha_tabela'
    # __table_args__ = {"schema": 'python'}

    id_pasta    = sa.Column(sa.String(40))
    empresa     = sa.Column(sa.String(150))
    ramo        = sa.Column(sa.String(20))
    analista    = sa.Column(sa.String(150))
    id_tarefa   = sa.Column(sa.String(40))
    responsavel = sa.Column(sa.String(40))
    tipo        = sa.Column(sa.String(40))
    sub_tipo    = sa.Column(sa.String(120))
    data        = sa.Column(sa.Date())
    status      = sa.Column(sa.String(40))
    observacao  = sa.Column(sa.String(512))

    def __init__(self,id_pasta,empresa,ramo,analista,id_tarefa,responsavel,tipo,sub_tipo,data,status,observacao):
        self.id_pasta    = id_pasta
        self.empresa     = empresa
        self.ramo        = ramo
        self.analista    = analista
        self.id_tarefa   = id_tarefa
        self.responsavel = responsavel
        self.tipo        = tipo
        self.sub_tipo    = sub_tipo
        self.data        = data
        self.status      = status
        self.observacao  = observacao


        
