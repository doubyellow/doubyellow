# coding=utf-8
"""
    企业端-节假日
"""
from core.rest_client import RestClient
from config.data import root_api_url


class SunSysHolidaysController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def query_sun_sys_holiday(self, **kwargs):
        # 查询节假日
        return self.post("/querySunSysHoliday", **kwargs)


SunSysHolidays = SunSysHolidaysController(root_api_url, "/app/v1/holiday")
