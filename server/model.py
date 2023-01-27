#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 27-01-2023 05:50 pm
# @Ticket  : EZB-
# @Author  : bhaskar.uprety
# @File    : model.py

"""model File created on 27-01-2023"""
from pydantic import BaseModel


class Connection(BaseModel):
    """Added connection model"""
    username: str
    totp: int
