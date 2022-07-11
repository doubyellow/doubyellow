# coding=utf-8
"""
    企业端-银行账户管理
"""
from core.rest_client import RestClient
from config.data import root_api_url


class SunBankAccountManagementController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def save_bank_account(self, **kwargs):
        # 银行账户新增
        return self.post("/saveBankAccount", **kwargs)

    def update_bank_account(self, **kwargs):
        # 银行账户修改
        return self.post("/updateBankAccount", **kwargs)

    def save_small_make_contributions(self, **kwargs):
        # 银行账户-填写小额打款金额
        return self.post("/saveSmallMakeContributions", **kwargs)

    def select_bank_account_list(self, **kwargs):
        # 银行账户管理-查询银行账户信息
        return self.post("/selectBankAccountList", **kwargs)

    def select_account(self, **kwargs):
        # 银行账户管理-查询企业名称
        return self.post("/selectAccount", **kwargs)

    def del_bank_account(self, **kwargs):
        # 银行账户删除
        return self.post("/delBankAccount", **kwargs)


SunBankAccountManagement = SunBankAccountManagementController(root_api_url, "/app/v1/cust/accountManagement")
