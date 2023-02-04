#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-02-2023 10:02 am
# @Author  : bhaskar.uprety
# @File    : utils

"""utils File created on 04-02-2023"""
import base64
import string as __string

from pyotp import TOTP, random_base32


def random_totp_key(length):
    """random_string generator"""
    letters = __string.ascii_lowercase + __string.digits
    return random_base32(length, letters).upper()


def verify_totp(key: str, value: str):
    """Implemented verify_totp"""
    totp_key = base64.b32encode(key.encode()).decode()
    totp = TOTP(totp_key)
    ok = totp.verify(value)
    return ok
