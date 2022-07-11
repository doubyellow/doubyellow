# coding=utf-8
"""
    企业端-企业证书管理
"""
from core.rest_client import RestClient
from config.data import root_api_url


class SunAppCustCorpCasController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def get_cust_corp_cas(self, **kwargs):
        # 获取企业证书信息-授权人信息
        return self.post("/get", **kwargs)

    def save_authorized(self, **kwargs):
        # 新增授权人
        return self.post("/save", **kwargs)

    def add_cas_id(self, **kwargs):
        # 新增主授权人的软银证书
        return self.post("/saveCasId", **kwargs)

    def reverse_cust_cas(self, **kwargs):
        # 企业端新增授权人时用户角色查询
        return self.post("/reverse", **kwargs)

    def cancel_authorization(self, **kwargs):
        # 企业端企业证书管理取消授权
        return self.post("/cancel", **kwargs)

    def get_transactor_id(self, **kwargs):
        # 通过uid查询经办人id
        return self.post("/transactor", **kwargs)


SunAppCustCorp = SunAppCustCorpCasController(root_api_url, "/app/v1/sys/cust/cas")
