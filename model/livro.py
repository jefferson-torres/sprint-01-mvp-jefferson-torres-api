from sqlalchemy import Column, Integer, String, BigInteger, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Livro(Base):
    __tablename__ = 'livro'

    codigo = Column(BigInteger, primary_key=True, default=Sequence('livro_codigo_seq'))
    titulo = Column(String, nullable=False)
    sinopse = Column(String, nullable=False)
    autores = Column(String, nullable=False)
    editora = Column(String, nullable=False)
    edicao = Column(Integer, nullable=False)
    genero = Column(String, nullable=False)
    numero_paginas = Column(String, nullable=False)

    def __init__(self, titulo, sinopse, autores, editora, edicao, genero, numero_paginas, codigo=None):
        self.codigo = codigo
        self.titulo = titulo
        self.sinopse = sinopse
        self.autores = autores
        self.editora = editora
        self.edicao = edicao
        self.genero = genero
        self.numero_paginas = numero_paginas