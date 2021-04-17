# -*- coding:utf-8 -*-
# @author: kayb
# @file: __init__.py.py
# @time: 2021/4/14 下午10:42


from flask import Blueprint


order_bp = Blueprint('order', __name__)

from .views.order_views import CreateOrderView


order_bp.add_url_rule('/order', view_func=CreateOrderView.as_view('/order'))


