# super-portfolio

## Contexto
- Desenvolver uma API para gerenciamento de dados de perfil e projetos em um super portfólio.
- Utilizar Django e Django Rest Framework

## Tecnologias usadas
- Utilizar o Django REST Framework para criar endpoints com entidades aninhadas.
- Utilizar o módulo Simple JWT para implementar autenticação no Django REST Framework.
## Crie o ambiente virtual para o projeto
```
python3 -m venv .venv && source .venv/bin/activate
```
## Instalando Dependências
```
python3 -m pip install -r dev-requirements.txt
```
## Executando o projeto
- Para a realização deste projeto, utilizaremos um banco de dados chamado `super_portfolio_database`.
- Já existe um script de criação do banco pronto no arquivo `database/01_create_database.sql` que será copiado para dentro do container.

* Para rodar o MySQL via Docker execute os seguintes comandos na raiz do projeto
```
docker build -t super-portfolio-db .
docker run -d -p 3306:3306 --name=super-portfolio-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=super_portfolio_database super-portfolio-db
```
* Ao criar/modificar um modelo, é necessário criar as migrações para espelhar as modificações para os bancos de dados, inclusive o banco de testes contam com estas modificações. O comando para gerar a migration a partir dos modelos criados é:
````
python3 manage.py makemigrations
```
## Executando Testes
* executando todos os testes
 ```
 python3 -m pytest
```
* Caso precise executar apenas um arquivo de testes basta executar o comando:
```
python3 -m pytest tests/nomedoarquivo.py
```
## Arquivos desenvolvidos pela Trybe
* src:
  - dev-requirements.txt
  - requirements.txt