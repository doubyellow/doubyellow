# coding=utf-8
"""
    企业端-首页
"""
from core.rest_client import RestClient
from config.data import root_api_url


class SunBusinessStatisticController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def total_amount(self, **kwargs):
        # 各项金额统计
        return self.post("/totalAmount", **kwargs)

    def get_announcement(self, **kwargs):
        # 公告
        return self.post("/announcement", **kwargs)

    def get_recommend(self, **kwargs):
        # 为你推荐
        return self.post("/recommend", **kwargs)


SunBusinessStatistic = SunBusinessStatisticController(root_api_url, "/app/v1/cust/BustotalAmount")
