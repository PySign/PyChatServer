#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 27-01-2023
# @Time    : 05:52 pm
# @Author  : bhaskar.uprety
# @File    : main.py

"""main.py File created on 27-01-2023"""

from fastapi import Depends, FastAPI, WebSocket, WebSocketDisconnect

from server.manager import ConnectionManager
from server.security import validate_user

app = FastAPI()

manager = ConnectionManager()


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket, username: str = Depends(validate_user)):
    """Implemented websocket_endpoint"""
    await manager.connect(websocket)
    message = 'Joined the chat room'
    await manager.broadcast(username, message, websocket)
    try:
        while True:
            message = await websocket.receive_text()
            await manager.broadcast(username, message, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        message = 'Left the chat room'
        await manager.broadcast(username, message, websocket)
