#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 27-01-2023 06:37 pm
# @Ticket  : EZB-
# @Author  : bhaskar.uprety
# @File    : security.py

"""security File created on 27-01-2023"""
from fastapi import FastAPI, HTTPException, Header

app = FastAPI()


async def validate_user(username: str = Header(), token: str = Header()):
    """Implemented validate_token"""
    if token == "invalid_token":
        raise HTTPException(status_code=400, detail="Invalid token")
    return username
