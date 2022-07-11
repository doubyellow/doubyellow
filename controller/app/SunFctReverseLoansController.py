# coding=utf-8
"""
    融资管理
"""
from core.rest_client import RestClient
from config.data import root_api_url


class SunFctReverseLoansController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def page_ticket(self, **kwargs):
        # 获取融资申请列表
        return self.post("/ticket/page", **kwargs)

    def list_account(self, **kwargs):
        # 获取收款账户列表
        return self.post("/account/list", **kwargs)

    def list_product(self, **kwargs):
        # 获取金融产品列表
        return self.post("/product/list", **kwargs)

    def compute_fct(self, **kwargs):
        # 自动计算融资金额
        return self.get("/compute", **kwargs)

    def add_fct(self, **kwargs):
        # 新增融资申请
        return self.post("/add", **kwargs)

    def page_fct(self, **kwargs):
        # 获取融资审核列表
        return self.post("/page", **kwargs)

    def info_fct(self, **kwargs):
        # 获取融资审核信息
        return self.post("/info", **kwargs)

    def audit_fct(self, **kwargs):
        # 企业端融资审核
        return self.post("/audit", **kwargs)

    def audit_progress(self, **kwargs):
        # 获取审核进度
        return self.post("/audit/progress", **kwargs)

    def apply_invoice_page(self, **kwargs):
        # 申请开票列表
        return self.post("/apply/invoice/page", **kwargs)

    def apply_invoice_export(self, **kwargs):
        # 申请开票导出
        return self.post("/apply/invoice/export", **kwargs)

    def apply_invoice(self, **kwargs):
        # 申请开票
        return self.post("/apply/invoice", **kwargs)

    def list_contract(self, **kwargs):
        # 获取融资合同信息列表
        return self.get("/list/contract", **kwargs)

    def list_invoice(self, **kwargs):
        # 获取融资发票信息列表
        return self.get("/list/invoice", **kwargs)

    def list_file(self, **kwargs):
        # 获取融资其他文件信息列表
        return self.get("/list/file", **kwargs)

    def upload(self, **kwargs):
        # 融资文件上传
        return self.post("/upload", **kwargs)

    def upload_invoices(self, **kwargs):
        # 融资发票上传
        return self.post("/invoices/upload", **kwargs)

    def invoice_add(self, **kwargs):
        # 原发票新增
        return self.post("/invoice/add", **kwargs)

    def list_fct_reverse_invoices(self, **kwargs):
        # 根据发票号码获取发票列表
        return self.get("/invoices/list", **kwargs)

    def full_first(self, **kwargs):
        # 查询融通合作平台标准库
        return self.get("/find/full", **kwargs)

    def category(self, **kwargs):
        # 查询单证标准库
        return self.get("/category", **kwargs)

    def sms_init(self, **kwargs):
        # 发送短信
        return self.post("/sms/init", **kwargs)

    def get_factoring_agent(self, **kwargs):
        # 获取保理业务合同
        return self.get("/factoring/agent/get", **kwargs)

    def get_financing_agent(self, **kwargs):
        # 获取融资服务协议
        return self.get("/financing/agent/get", **kwargs)

    def partner_fct(self, **kwargs):
        # 融通合同平台推送接口
        return self.post("/partner", **kwargs)

    def update_fct(self, **kwargs):
        # 提交融资贸易背景资料
        return self.post("/update", **kwargs)

    def get_product(self, **kwargs):
        # 获取金融产品
        return self.post("/product/get", **kwargs)

    def get_account(self, **kwargs):
        # 获取收款账户
        return self.post("/account/get", **kwargs)

    def request_render_word(self, loan_id, **kwargs):
        # 融资服务协议重新请求
        return self.post(f"/render/word/request/{loan_id}", **kwargs)


SunFctReverseLoans = SunFctReverseLoansController(root_api_url, "/app/v1/fct")
