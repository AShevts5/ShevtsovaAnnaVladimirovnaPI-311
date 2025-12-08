from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

list_tasks = {}

class Task(BaseModel):
    ID: int
    Name: str
    Description: str

@app.get("/all_tasks")
async def get_all_tasks():
    return list_tasks

@app.get("/get_task/{task_id}")
async def get_task(task_id: int):
    try:
        return list_tasks[task_id]
    except:
        return {"Error": "Task does not exist."}

@app.post("/new_task/{task_id}")
async def new(task_id: int, new_task: Task):
    if task_id in list_tasks:
        return {"Error": "Task already exists!"}
    if task_id > 10 or task_id < 1:
        return {"Error": "Task ID out of range!"}
    list_tasks[task_id] = new_task
    return list_tasks[task_id]

class UpdateTask(BaseModel):
    ID: Optional[int] = None
    Name: Optional[str] = None
    Description: Optional[str] = None

@app.put('/update_task/{task_id}')
async def update_task(task_id: int, upd_task: UpdateTask):
   if task_id not in list_tasks:
       return {"Error": "Task ID doesn't exists"}
   if upd_task.ID != None:
       list_tasks[task_id].ID = upd_task.ID
   if upd_task.Name != None:
       list_tasks[task_id].Name = upd_task.Name
   if upd_task.Description != None:
       list_tasks[task_id].Description = upd_task.Description

# создаём DELETE-эндпойнт:
@app.delete('/delete_task/{task_id}')
def delete_task(task_id: int):
   if task_id not in list_tasks:
       return {"Error": "Task ID doesn't exists"}
   del list_tasks[task_id]
   return {'Done': 'The task successfully deleted'}