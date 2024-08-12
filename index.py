from fastapi import FastAPI
from routes.tasks import ToDo
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")


app = FastAPI()


app.include_router(ToDo)
# app.include_router(Pending)
