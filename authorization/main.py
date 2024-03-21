from fastapi import FastAPI

from authorization.auth import auth_router
from authorization.users import users_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(users_router)
