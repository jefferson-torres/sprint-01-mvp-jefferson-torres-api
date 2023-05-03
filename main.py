from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from sqlalchemy.exc import NoResultFound

from flask_cors import CORS

from model import Livro, Session
from schemas.error import ErrorSchema
from schemas.livro import LivroCadastroSchema, apresenta_livro, ListagemLivrosSchema, apresenta_livros, LivroSchema, \
    LivroDelSchema

from logger import logger

info = Info(title="MVP Spring 01 Jefferson Torres - API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
livro_tag = Tag(name="Livro", description="Adição, visualização e remoção de livro à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/livros', tags=[livro_tag],
          responses={"200": LivroCadastroSchema, "409": ErrorSchema, "400": ErrorSchema})
def adicionar_livro(form: LivroCadastroSchema):
    """Adiciona um novo livro no banco de dados
    Retorna uma representação do livro adicionado
    """
    livro = Livro(
        titulo=form.titulo,
        sinopse=form.sinopse,
        autores=form.autores,
        editora=form.editora,
        edicao=form.edicao,
        genero=form.genero,
        numero_paginas=form.numero_paginas
    )

    try:
        session = Session()
        session.add(livro)
        session.commit()
        return apresenta_livro(livro), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar o novo livro"
        logger.error(e)
        return {"mesage": error_msg}, 400

@app.get('/livros', tags=[livro_tag],
         responses={"200": ListagemLivrosSchema, "404": ErrorSchema})
def listar_livros():
    """Faz a busca por todos os livros cadastrados
    Retorna uma representação da listagem de livros.
    """
    session = Session()
    produtos = session.query(Livro).all()

    if not produtos:
        return {"livros": []}, 200
    else:
        return apresenta_livros(produtos), 200

@app.delete('/livros', tags=[livro_tag],
            responses={"204": None, "404": ErrorSchema})
def deletar_livro(query: LivroDelSchema):
    """Remove o livro com o código informado
    Não retorna conteúdo
    """
    try:
        session = Session()
        livro = session.query(Livro).filter(Livro.codigo == query.codigo).first()
        if livro:
            session.delete(livro)
            session.commit()
            return "", 204
        else:
            error_msg = "Livro não encontrado na base de dados"
            return {"message": error_msg}, 404

    except Exception as e:
        error_msg = "Não foi possível deletar o livro"
        logger.error(e)
        return {"message": error_msg}, 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)