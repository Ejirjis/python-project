from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException ,Depends
from fastapi.security import OAuth2PasswordBearer

# Database setup
engine = create_engine("sqlite:///users.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Password hashing
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Database model
class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

Base.metadata.create_all(bind=engine)

# Pydantic model
class User(BaseModel):
    username: str
    password: str

app = FastAPI()

SECRET_KEY = "your-secret-key-keep-it-safe"
ALGORITHM = "HS256"

@app.post("/register")
def register(user: User):
    db = SessionLocal()
    existing_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_user:
        db.close()
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = pwd_context.hash(user.password)
    new_user = UserModel(username=user.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.close()
    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: User):
    db = SessionLocal()
    db_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    db.close()

    if not db_user :
        raise HTTPException(status_code=400, detail="User not found")
    if not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail= "Wrong password")
    
    token = jwt.encode(
        {"sub":user.username, "exp": datetime.utcnow()+timedelta(hours=1)},
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return {"token": token}

@app.get ("/me")
def get_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY , algorithms=[ALGORITHM])
        username = payload.get("sub")
        return {"message":f"Hello {username}, you are logged in!"}
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
