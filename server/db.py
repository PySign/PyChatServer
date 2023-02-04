#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-02-2023 10:15 am
# @Author  : bhaskar.uprety
# @File    : db

"""db File created on 04-02-2023"""
from fastapi import Body
from fastapi.exceptions import HTTPException
from peewee import CharField, IntegrityError, Model, SqliteDatabase, TextField

from server.model import User
from server.utils import random_totp_key

db = SqliteDatabase('user_info.db')


class DBUser(Model):
    """Implemented User DB Model"""
    username = CharField(unique=True)
    totp_code = CharField()
    public_key = TextField()

    class Meta:
        """Implemented Meta Class"""
        database = db


def create_user(user: User = Body()):
    """It will create a user"""
    username = user.username
    totp_code = random_totp_key(32)
    public_key = user.public_key
    try:
        dbuser = DBUser(username=username, totp_code=totp_code, public_key=public_key)
        dbuser.save()
        return {"user": username, 'totp_code': totp_code}
    except IntegrityError:
        raise HTTPException(406, "Username already taken")


def is_available(username: str):
    """It will create the user from username"""
    try:
        DBUser.get(username == username)
        return False
    except DBUser.DoesNotExist:
        return True


def read_user(username: str):
    """It will create the user from username"""
    try:
        dbuser = DBUser.get(username=username)
        return {'username': dbuser.username, 'totp_code': dbuser.totp_code}
    except DBUser.DoesNotExist:
        raise HTTPException(404, 'User not found')


def get_totp_secret(username: str):
    """It will create the user from username"""
    try:
        dbuser = DBUser.get(username=username)
        return dbuser.totp_code
    except DBUser.DoesNotExist:
        raise HTTPException(401, 'Please signup')
