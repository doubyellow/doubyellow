# coding=utf-8
"""
    企业端协议管理
"""
from core.rest_client import RestClient
from config.data import root_api_url


class SunAppAgreeController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def list_agree(self, **kwargs):
        # 获取协议列表
        return self.post("/list", **kwargs)

    def get_download_url(self, **kwargs):
        # 获取下载URL
        return self.post("/getDownloadUrl", **kwargs)

    def batch_download(self, **kwargs):
        # 协议文件下载
        return self.post("/batchDownload", **kwargs)


SunAppAgree = SunAppAgreeController(root_api_url, "/app/v1/sys/agree")
