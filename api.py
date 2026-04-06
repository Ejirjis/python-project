from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
# Database setup
engine = create_engine("sqlite:///todos.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

SECRET_KEY = "your-secret-key-keep-it-safe"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



# Database mode
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
def add_todo(todo: Todo, token: str = Depends(oauth2_scheme)):
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except:
        raise HTTPException(status_code=401 , detail="Invalid token")
    
    db = SessionLocal()
    new_todo = TodoModel(
        task=todo.task, 
        done=todo.done)
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
