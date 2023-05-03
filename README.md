# Back-end de um sistema de cadastro de livros(MVP - Sprint 1 - Jefferson de Oliveira Torres)

Esse é o projeto do back-end que fornece uma API Python para cadastro de livros

---

## Como executar

### Importando o arquivo de dump no PostgreSQL

Siga as instruções abaixo para importar o arquivo `mvp-sprint-01-jefferson-torres.sql` no PostgreSQL usando diferentes ferramentas:

* Crie a base de dados `mvp-sprint-01-jefferson-torres`.
* Importe o arquivo `mvp-sprint-01-jefferson-torres.sql`.

### Configurando a conexão com o banco de dados
Será necessário alterar dados de conexão com o banco de dados.
  * Entre na pasta model
  * Edite o arquivo __init__.py, informando seu usuário, senha e outros parametros caso seja necessário na linha abaixo
  * ```
    db_url = 'postgresql://USUARIO:SENHA@localhost:5432/mvp-sprint-01-jefferson-torres'
    ```
    
### Buildando e levantando o projeto
Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Para instalar as dependências/bibliotecas, descritas no arquivo requirements.txt, execute o seguinte comando:
```
(env)$ pip install -r requirements.txt
```

Para executar a API, siga os passos abaixo:

* Vá até o diretório raiz do projeto pelo terminal.
* Ative o ambiente virtual (se estiver usando virtualenv).
* Execute o comando:
* ```
  (env)$ flask --app main run --debug --port 8000
  ```
  
* Abra o [http://localhost:8000/](http://localhost:8000/) no navegador para verificar o status da API em execução.
