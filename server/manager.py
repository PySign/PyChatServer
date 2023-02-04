#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 27-01-2023 05:46 pm
# @Ticket  : EZB-
# @Author  : bhaskar.uprety
# @File    : main.py

"""main File created on 27-01-2023"""
import json
from typing import Dict

from fastapi import FastAPI, WebSocket

from server.options import Activity, Topic

app = FastAPI()


class ConnectionManager:
    """Implemented ConnectionManager"""

    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, username: str, websocket: WebSocket):
        """Implemented ConnectionManager connect"""
        if username in self.active_connections.keys():
            old_soc: WebSocket = self.active_connections.get(username)
            await old_soc.close(reason='Another client is connected')

        await websocket.accept()
        await self.broadcast(username, Activity.joined, Topic.activity)
        self.active_connections[username] = websocket

    async def disconnect(self, username: str):
        """Implemented ConnectionManager disconnect"""
        self.active_connections.pop(username)
        await self.broadcast(username, Activity.exited, Topic.activity)

    async def send_message(self, username: str, message: str):
        """Implemented ConnectionManager.send_message"""
        await self.broadcast(username, message, Topic.message)

    async def broadcast(self, username: str, message: str, topic):
        """Implemented ConnectionManager broadcast"""
        data = {
            'user': username,
            'message': message,
            'topic': topic
        }
        for user, connection in self.active_connections.items():
            if user != username:
                await connection.send_json(data)
