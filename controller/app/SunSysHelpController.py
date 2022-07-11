# coding=utf-8
"""
    帮助文档表  前端控制器
"""
from core.rest_client import RestClient
from config.data import root_api_url


class SunSysHelpController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def get_help(self, **kwargs):
        # 帮助文档
        return self.post("/helps", **kwargs)


SunSysHelp = SunSysHelpController(root_api_url, "/app/v1/sys/help")
