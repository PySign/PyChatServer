#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 27-01-2023
# @Time    : 05:52 pm
# @Author  : bhaskar.uprety
# @File    : main.py

"""main.py File created on 27-01-2023"""

from fastapi import Depends, FastAPI, WebSocket, WebSocketDisconnect

from server.db import DBUser, create_user, db, is_available, read_user
from server.manager import ConnectionManager
from server.security import validate_user

app = FastAPI()

manager = ConnectionManager()


@app.on_event('startup')
def connect_and_create_db():
    """Implemented connect_and_create_db"""
    db.connect()
    db.create_tables([DBUser], safe=True)


@app.post("/user")
async def create_user(user_data: dict = Depends(create_user)):
    """It will create a user"""
    return 201, user_data


@app.get("/available/{username}")
async def is_available(available: bool = Depends(is_available)):
    """It will create the user from username"""
    return available


@app.get("/user/{username}")
async def read_user(user: dict = Depends(read_user)):
    """It will create the user from username"""
    return user


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket, username: str = Depends(validate_user)):
    """Implemented websocket_endpoint"""
    if username:
        await manager.connect(username, websocket)
        try:
            while True:
                message = await websocket.receive_text()
                await manager.send_message(username, message)
        except WebSocketDisconnect:
            await manager.disconnect(username)
    else:
        await websocket.accept()
        await websocket.send_text('Invalid token')
        await websocket.close()
