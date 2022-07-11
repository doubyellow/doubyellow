# coding=utf-8
"""
    企业端统计查询
"""
from core.rest_client import RestClient
from config.data import root_api_url


class SunAppStatisticsQueryController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def transfer_page(self, **kwargs):
        # 额度明细列表
        return self.post("/transfer/page", **kwargs)

    def transfer_log(self, **kwargs):
        # 流转记录
        return self.post("/transfer/log", **kwargs)

    def transfer_down(self, **kwargs):
        # 导出签发条额度使用明细
        return self.post("/transfer/down", **kwargs)


SunAppStatisticsQuery = SunAppStatisticsQueryController(root_api_url, "/app/v1/statistics")
