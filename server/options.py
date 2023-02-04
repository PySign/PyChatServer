#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 28-01-2023 08:51 am
# @Ticket  : EZB-
# @Author  : bhaskar.uprety
# @File    : options.py

"""options File created on 28-01-2023"""
from enum import Enum


class Topic(str, Enum):
    """Implemented TopicEnum"""
    message = 'msg'
    activity = 'act'
    command = 'cmd'


class Activity(str, Enum):
    """Implemented Activity"""
    joined = 'in'
    exited = 'out'
