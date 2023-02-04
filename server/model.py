#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 27-01-2023 05:50 pm
# @Ticket  : EZB-
# @Author  : bhaskar.uprety
# @File    : model.py

"""model File created on 27-01-2023"""
from pydantic import BaseModel


class User(BaseModel):
    """Added connection model"""
    username: str
    public_key: str
