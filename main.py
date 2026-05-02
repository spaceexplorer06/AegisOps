from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

tasks = []
class Task(BaseModel):
    id: int
    title: str
    completed:bool = False
@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message" : "Task Created" , "task" : task}
@app.get("/tasks")
def get_tasks():
    return tasks
