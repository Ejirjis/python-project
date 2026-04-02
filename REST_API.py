from fastapi import FastAPI
from pydantic import BaseModel

class Todo(BaseModel):
    id:int
    task: str
    done: bool = False

app = FastAPI()

todos = []

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/todos")
def get_todo():
    return todos

@app.post("/todos")
def add_todo(todo: Todo):
    todos.append(todo)
    return {"Message": "Todo added", "todo": todo}


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo Deleted"}
        return {"Message": "Todo not found"}
    