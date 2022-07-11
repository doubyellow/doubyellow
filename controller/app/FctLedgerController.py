# coding=utf-8
"""
    融资台账管理
"""
from config.data import root_api_url
from core.rest_client import RestClient


class FctLedgerController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def page_fct_ledger(self, **kwargs):
        # 获取融资台账列表（分页）
        return self.post("/page", **kwargs)

    def export_fct_ledger(self, **kwargs):
        # 导出融资台账列表
        return self.post("/export", **kwargs)

    def export_trans_detail(self, **kwargs):
        # 导出融资交易明细列表
        return self.post("/trans/export", **kwargs)

    def list_supplier_financing(self, **kwargs):
        # 供应商融资查询
        return self.post("/listSupplierFinancing", **kwargs)

    def supplier_financing_download(self, **kwargs):
        # 供应商融资导出
        return self.post("/supplierFinancingDownload", **kwargs)

    def details_supplier_financing(self, **kwargs):
        # 供应商融资详情查询
        return self.post("/detailsSupplierFinancing", **kwargs)

    def detail_factoring_list_download(self, **kwargs):
        # 多个供应商融资详情导出
        return self.post("/detailFactoringListDownload", **kwargs)


FctLedger = FctLedgerController(root_api_url, "/app/v1/fct/ledger")
