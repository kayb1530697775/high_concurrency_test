# -*- coding:utf-8 -*-
# @author: kayb
# @file: create_order.py
# @time: 2021/4/14 下午10:44

from flask import request


from apps.order.views.base_views import OrderBaseView
from common.common_config import ResponseStatusCode


class CreateOrderView(OrderBaseView):
    def get(self):

        print(request)

        print("hello flask")

        return "ok"

    def post(self):

        goods_id = request.form.get("goods_id", "")

        return_data = {
            "status": ResponseStatusCode.Fail["code"]
        }
        if not goods_id:
            return_data["msg"] = "param error"
            return self.generate_data(return_data)

        return_data["status"] = ResponseStatusCode.Success["code"]

        return self.generate_data(return_data)




