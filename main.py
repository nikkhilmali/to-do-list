from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://admin:admin@todo-cluster.jxivs.mongodb.net/to_do_db")


@app.get("/",response_class=HTMLResponse)
async def read_items(request:Request):
    queryset = conn.to_do_db.to_do_list.find()
    return templates.TemplateResponse(
        "index.html", {"request": request, "to_dos": queryset}
    )



@app.get("/items/{q}")
def get_items(item_id: int | None, q: str | None):
    return {"item_id": item_id, "q": q}
