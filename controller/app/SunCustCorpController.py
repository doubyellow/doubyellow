# coding=utf-8
"""
    企业用户信息模块
"""
from core.rest_client import RestClient
from config.data import root_api_url


class SunCustCorpController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def cust_register(self, **kwargs):
        # 注册客户
        return self.post("/custRegister", **kwargs)

    def cust_authentication(self, **kwargs):
        # 企业认证
        return self.post("/custAuthentication", **kwargs)

    def upload_contract(self, **kwargs):
        # 企业认证文件上传
        return self.post("/uploadAuthentication", **kwargs)

    def update_info(self, **kwargs):
        # 企业信息修改
        return self.get("/updateCorpInfo", **kwargs)

    def add_small_make_contributions(self, **kwargs):
        # 企业认证-填写小额打款金额
        return self.post("/addSmallMakeContributions", **kwargs)

    def query_cust_corp(self, **kwargs):
        # 企业信息管理--查询
        return self.post("/queryCustCorp", **kwargs)

    def relate_corp_query(self, **kwargs):
        # 企业端关系表新增时公司查询反显
        return self.post("/relateCorpQuery", **kwargs)

    def insert_corp_relate(self, **kwargs):
        # 企业端企业关系表新增
        return self.post("/insertRelate", **kwargs)

    def update_corp_relate(self, **kwargs):
        # 企业端企业关系表修改
        return self.post("/updateRelate", **kwargs)

    def delete_corp_relate(self, **kwargs):
        # 企业端企业关系表删除
        return self.post("/deleteRelate", **kwargs)

    def import_corp_relate(self, **kwargs):
        # 企业端企业关系表导入
        return self.post("/improtRelate", **kwargs)

    def export_relate(self, fileid=None, **kwargs):
        # 企业端企业关系表模板导出
        return self.post("/exprotRelate/{}".format(fileid), **kwargs)

    def list_corp_relate(self, **kwargs):
        # 企业端企业关系表查询
        return self.post("/listRelate", **kwargs)

    def list_relate_download(self, **kwargs):
        # 企业端企业关系表批量导出
        return self.post("/listRelateDownload", **kwargs)

    def export_authorizer(self, **kwargs):
        # 企业授权确认书导出
        return self.post("/exportAuthorizer", **kwargs)

    def register_data(self, **kwargs):
        # 企业注册协议预览地址
        return self.post("/registerData", **kwargs)

    def select_bank_account_list(self, corp_id, **kwargs):
        # 企业认证-查询银行账户信息
        return self.get(f"/selectBankAccountList/{corp_id}", **kwargs)

    def authentication_query(self, **kwargs):
        # 企业认证信息查询
        return self.post("/authenticationQuery", **kwargs)

    def examine_query(self, **kwargs):
        # 企业认证审核状态查询
        return self.post("/examineQuery", **kwargs)

    def query_ticket(self, **kwargs):
        # 企业信息--凭证管理--白条/财务凭证--查询
        return self.post("/queryTicket", **kwargs)

    def download(self, **kwargs):
        # 企业信息--凭证管理--白条凭证--导出
        return self.post("/download", **kwargs)

    def download_accounting(self, **kwargs):
        # 企业信息--凭证管理--财务凭证--导出
        return self.post("/downloadAccounting", **kwargs)

    def batch_download(self, **kwargs):
        # 企业信息--凭证管理--财务凭证/财务凭证下载
        return self.post("/batchDownload", **kwargs)

    def list_corp_for_social_credit_code(self, **kwargs):
        # 通过企业ID获取供应商列表的企业信息
        return self.post("/listCorpForSocialCreditCode", **kwargs)

    def batch_get_download_url(self, **kwargs):
        # 文件批量下载
        return self.post("/batchGet/downloadUrl", **kwargs)


SunCustCorp = SunCustCorpController(root_api_url, "/app/v1/cust/corp")
