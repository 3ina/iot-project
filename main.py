import time
import json
import cv2
import base64
from sensor import IMAGE_SAVE_DIR,cap
from sensor import get_cpu_temperature, get_sensor_data
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Depends, HTTPException
from fastapi.websockets import WebSocketState
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

def load_credentials(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading credentials: {e}")
        return None


class TokenData(BaseModel):
    username: str

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = time.time() + TOKEN_EXPIRATION
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return TokenData(username=username)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_token(token)


@app.post("/login")
async def login(data: dict):
    user = load_credentials(CREDENTIALS_FILE)
    if not user:
        raise Exception("Failed to load user credentials. Ensure the file exists and is valid.")
    if data.get("username") == user["username"] and data.get("password") == user["password"]:
        token = create_access_token({"username": data["username"]})
        return JSONResponse(content={"access_token": token})
    raise HTTPException(status_code=401, detail="Incorrect username or password")




@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_sensor_endpoint(websocket: WebSocket):
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close(code=1008, reason="Missing authentication token")
        return

    try:
        user = verify_token(token)
    except HTTPException as e:
        await websocket.close(code=1008, reason="Invalid authentication token")
        return

    await websocket.accept()
    try:
        while True:
            data = await get_sensor_data()
            if data:
                await websocket.send_json(data)
            await asyncio.sleep(0.5)
    except WebSocketDisconnect:
        print("WebSocket disconnected from /ws")
    except Exception as e:
        print(f"Sensor WebSocket connection error: {e}")
    finally:
        await websocket.close()

@app.websocket("/ws/status")
async def websocket_status_endpoint(websocket: WebSocket):
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close(code=1008, reason="Missing authentication token")
        return

    try:
        user = verify_token(token)
    except HTTPException as e:
        await websocket.close(code=1008, reason="Invalid authentication token")
        return

    await websocket.accept()
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            uptime = time.time() - psutil.boot_time()
            cpu_temp = get_cpu_temperature()

            status_data = {
                "cpu_usage": cpu_usage,
                "memory_percent": memory_info.percent,
                "uptime_seconds": uptime,
                "cpu_temp_c": cpu_temp,
            }

            await websocket.send_json(status_data)
            await asyncio.sleep(5)
    except WebSocketDisconnect:
        print("WebSocket disconnected from /ws/status")
    except Exception as e:
        print(f"Status WebSocket connection error: {e}")
    finally:
        await websocket.close()


@app.websocket("/ws/camera")
async def websocket_camera_endpoint(websocket: WebSocket):
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close(code=1008, reason="Missing authentication token")
        return

    try:
        user = verify_token(token)
    except HTTPException as e:
        await websocket.close(code=1008, reason="Invalid authentication token")
        return

    await websocket.accept()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                await websocket.send_json({"error": "Camera read failed"})
                continue

            _, buffer = cv2.imencode(".jpg", frame)
            jpg_as_text = base64.b64encode(buffer).decode("utf-8")

            await websocket.send_json({"frame": jpg_as_text})
            await asyncio.sleep(0.05)
    except WebSocketDisconnect:
        print("WebSocket disconnected from /ws/camera")
    except Exception as e:
        print(f"Camera WebSocket connection error: {e}")
    finally:
        if websocket.client_state == WebSocketState.CONNECTED:
            await websocket.close()