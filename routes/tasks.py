from fastapi.responses import HTMLResponse 
from fastapi import APIRouter, Request
from schema.tasks import get_data, get_pending_todos_data
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")

ToDo = APIRouter()


@ToDo.get("/")
@ToDo.get("/all_tasks")
async def get_all_todos(request:Request):
    data = get_data()
    # return {"message": "all_tasks"}
    return templates.TemplateResponse(
        "index.html", {"request": request, "to_dos": data}
    )


@ToDo.get("/pending")
async def get_pending_todos(request: Request):
    data = get_pending_todos_data()
    # return {"message": "pending"}
    return templates.TemplateResponse(
        "index.html", {"request": request, "to_dos": data}
    )


@ToDo.get("/completed")
async def get_completed_todos(request: Request):
    # data = tasks_converter()
    return {"message": "completed"}


@ToDo.get("/archived")
async def get_archived_todos(request: Request):
    # data = tasks_converter()
    return {"message": "archived"}


# @ToDo.post("/create-task")
# def get_items(request:Request):
#     data=""
#     response = create_task(data)
#     return {"item_id": item_id, "q": q}
