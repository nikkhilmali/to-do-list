from pydantic import BaseModel


class Tasks(BaseModel):
    title : str
    description:str|None
    is_complete:bool = False
    is_archive:bool = False


