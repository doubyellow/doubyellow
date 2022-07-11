# coding=utf-8
"""
    企业端-发票信息管理
"""
from core.rest_client import RestClient
from config.data import root_api_url


class SunCustCorpInvoiceController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def save_sun_cust_corp_invoice(self, **kwargs):
        # 保存修改发票信息
        return self.post("/save", **kwargs)

    def reverse_sun_cust_corp_list(self, **kwargs):
        # 企业端新增发票-反显企业用户信息
        return self.post("/reversed", **kwargs)


SunCustCorpInvoice = SunCustCorpInvoiceController(root_api_url, "/app/v1/cust/invoice")
