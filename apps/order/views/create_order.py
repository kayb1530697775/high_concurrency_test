# -*- coding:utf-8 -*-
# @author: kayb
# @file: create_order.py
# @time: 2021/4/14 下午10:44


from apps.order.views.base_views import OrderBaseView


class CreateOrderView(OrderBaseView):
    def get(self):

        print("hello flask")

        return "ok"