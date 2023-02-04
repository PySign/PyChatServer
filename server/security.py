#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 27-01-2023 06:37 pm
# @Ticket  : EZB-
# @Author  : bhaskar.uprety
# @File    : security.py

"""security File created on 27-01-2023"""
from fastapi import FastAPI, HTTPException, Header, WebSocketDisconnect

from .db import get_totp_secret
from .utils import verify_totp

app = FastAPI()


async def validate_user(username: str = Header(), token: str = Header()):
    """Implemented validate_token"""
    totp_secret = get_totp_secret(username)
    verified = verify_totp(totp_secret, token)
    if verified:
        return username
    else:
        return False
