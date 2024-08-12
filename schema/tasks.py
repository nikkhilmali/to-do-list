from configs.db import connection
from model.tasks import Tasks

def get_data():
    # query_set = conn.
    query_set = connection.to_do_db.to_do_list.find()
    return query_set


def get_pending_todos_data():
    # query_set = conn.
    query_set = connection.to_do_db.to_do_list.find({"is_complete":False})
    for document in query_set:
        print(document)
    return query_set


def create_task(data:Tasks):
    """"""
    inserted_task = connection.to_do_db.to_do_list.insert_one(dict(data))
    return inserted_task
