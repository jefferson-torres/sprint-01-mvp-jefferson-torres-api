from typing import List

from pydantic import BaseModel, validator

from model import Livro

def not_blank(cls, value: str, field_name: str):
    if value is None or value.strip() == "":
        raise ValueError(f"{field_name} é obrigatório.")
    return value

def greater_than_zero(cls, value: int, field_name: str):
    if value <= 0:
        raise ValueError(f"{field_name} deve ser maior que zero.")
    return value


class LivroCadastroSchema(BaseModel):
    """ Define como um novo livro a ser inserido deve ser representado
    """
    titulo: str
    sinopse: str
    autores: str
    editora: str
    edicao: int
    genero: str
    numero_paginas: int

    _titulo = validator("titulo", allow_reuse=True)(lambda cls, v: not_blank(cls, v, "Título"))
    _sinopse = validator("sinopse", allow_reuse=True)(lambda cls, v: not_blank(cls, v, "Sinopse"))
    _autores = validator("autores", allow_reuse=True)(lambda cls, v: not_blank(cls, v, "Autores"))
    _editora = validator("editora", allow_reuse=True)(lambda cls, v: not_blank(cls, v, "Editora"))
    _genero = validator("genero", allow_reuse=True)(lambda cls, v: not_blank(cls, v, "Gênero"))
    _edicao = validator("edicao", allow_reuse=True)(lambda cls, v: greater_than_zero(cls, v, "Edição"))
    _numero_paginas = validator("numero_paginas", allow_reuse=True)(lambda cls, v: greater_than_zero(cls, v, "Número de páginas"))

    class Config:
        schema_extra = {
            "example": {
                "titulo": "Título do livro",
                "sinopse": "Sinopse do livro",
                "autores": "Nomes dos autores",
                "editora": "Nome da editora",
                "edicao": 1,
                "genero": "Gênero do livro",
                "numero_paginas": 100
            }
        }

class LivroSchema(BaseModel):
    """ Define como um livro será retornado
    """
    codigo: int
    titulo: str
    sinopse: str
    autores: str
    editora: str
    edicao: int
    genero: str
    numero_paginas: int

    class Config:
        schema_extra = {
            "example": {
                "codigo": 1,
                "titulo": "Título do livro",
                "sinopse": "Sinopse do livro",
                "autores": "Nomes dos autores",
                "editora": "Nome da editora",
                "edicao": 1,
                "genero": "Gênero do livro",
                "numero_paginas": 100
            }
        }


class LivroDelSchema(BaseModel):
    """ Define o código do livro que será removido
    """
    codigo: int

    class Config:
        schema_extra = {
            "example": {
                "codigo": 1,
            }
        }
class ListagemLivrosSchema(BaseModel):
    """ Define como uma listagem de livros será retornada.
    """
    livros:List[LivroSchema]
def apresenta_livro(livro: Livro):
    """ Retorna uma representação do livro seguindo o schema definido em
        LivroSchema.
    """
    return {
        "codigo": livro.codigo,
        "titulo": livro.titulo,
        "sinopse": livro.sinopse,
        "autores": livro.autores,
        "editora": livro.editora,
        "edicao": livro.edicao,
        "genero": livro.genero,
        "numero_paginas": livro.numero_paginas,
    }

def apresenta_livros(livros: List[Livro]):
    """ Retorna uma representação do livro seguindo o schema definido em
        LivroSchema.
    """
    result = []
    for livro in livros:
        result.append(
            apresenta_livro(livro)
        )

    return {"livros": result}