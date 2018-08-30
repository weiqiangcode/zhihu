#encoding: utf-8
from functools import wraps
from flask import session, redirect, url_for

# 登录限制装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            # 传进来的函数得再return出去,否则不会显示结果
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper