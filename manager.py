# -*- coding:utf-8 -*-
# @author: kayb
# @file: manager.py
# @time: 2021/4/14 下午10:31


from flask import Flask

from apps.order import order_bp

# 创建flask
app = Flask(__name__)

# 注册蓝图
app.register_blueprint(order_bp)


app.run()







