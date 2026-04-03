from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Database setup
engine = create_engine("sqlite:///todos.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Database model
class TodoModel(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    done = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

# Pydantic model
class Todo(BaseModel):
    task: str
    done: bool = False


app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/todos")
def get_todos():
    db = SessionLocal()
    todos = db.query(TodoModel).all()
    db.close()
    return todos

@app.post("/todos")
def add_todo(todo: Todo):
    db = SessionLocal()
    new_todo = TodoModel(task=todo.task, done=todo.done)
    db.add(new_todo)
    db.commit()
    db.close()
    return {"message": "Todo added"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    db = SessionLocal()
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        db.close()
        return {"message": "Todo not found"}
    db.delete(todo)
    db.commit()
    db.close()
    return {"message": "Todo deleted"}