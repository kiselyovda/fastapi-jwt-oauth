# Simple OAuth authentication with FastAPI

## Stack

- [Python 3.12](https://github.com/python/cpython)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Poetry](https://github.com/python-poetry/poetry)
- [PyJWT](https://github.com/jpadilla/pyjwt)
- [bcrypt](https://github.com/pyca/bcrypt)

## What i`ve done

- [x] Release JWT Token on endpoint `/auth/login`.
- [x] Get current user on endpoint `/users/me`.
- [x] Get username of user on endpoint `/users/username`.

## In the future
- [ ] `PostgreSQL` connection with [SQLAlchemy 2.0+](https://github.com/sqlalchemy/sqlalchemy).
- [ ] [Alembic](https://github.com/sqlalchemy/alembic) migrations.
- [ ] Full `CRUD` operations `(CREATE, READ, UPDATE, DELETE)` with `/users` endpoint.
- [ ] `Dockerfile`.
- [ ] `docker-compose.yaml`.


> [!NOTE]
> To launch app you should run:
> ```bash
> mv .env.example .env
> python3 -m venv venv
> source venv/bin/activate
> (venv) pip install poetry
> (venv) poetry install
> (venv) uvicorn authorization.main:app --host localhost --port 8000 --reload
> ```

> [!NOTE]
> To make private and public keys check up [this file](./authorization//auth/README.md).
