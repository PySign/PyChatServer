#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 27-01-2023 05:46 pm
# @Ticket  : EZB-
# @Author  : bhaskar.uprety
# @File    : main.py

"""main File created on 27-01-2023"""
import json
from typing import List

from fastapi import FastAPI, WebSocket

app = FastAPI()


class ConnectionManager:
    """Implemented ConnectionManager"""

    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """Implemented ConnectionManager connect"""
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """Implemented ConnectionManager disconnect"""
        self.active_connections.remove(websocket)

    async def broadcast(self, username: str, message: str, websocket: WebSocket):
        """Implemented ConnectionManager broadcast"""
        data = {
            'user': username,
            'message': message
        }
        raw_data = json.dumps(data)

        for connection in self.active_connections:
            if connection != websocket:
                await connection.send_text(raw_data)
