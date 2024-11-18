import time
import json
import os
from .sensor import IMAGE_SAVE_DIR
from sensor import get_cpu_temperature, get_sensor_data
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from jose import jwt, JWTError
from pydantic import BaseModel
import asyncio
import psutil

app = FastAPI()
templates = Jinja2Templates(directory="templates")



SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
TOKEN_EXPIRATION = 3600
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


app.mount("/static", StaticFiles(directory=IMAGE_SAVE_DIR), name="static")

CREDENTIALS_FILE = "credentials.json"

class TokenData(BaseModel):
    username: str

def load_credentials(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading credentials: {e}")
        return None

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return TokenData(username=username)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")