# coding=utf-8
"""
    企业端额度设置
"""
from core.rest_client import RestClient
from config.data import root_api_url


class SunAppLmtController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def list_lmt(self, **kwargs):
        # 获取融资台账列表（分页）
        return self.post("/list", **kwargs)

    def list_child_lmt(self, **kwargs):
        # 获取企业分配的额度配置列表
        return self.post("/child/list", **kwargs)

    def list_temp_lmt(self, **kwargs):
        # 获取额度配置审核列表
        return self.post("/temp/list", **kwargs)

    def info(self, comp_id, **kwargs):
        # 额度配置信息
        return self.get("/listSupplierFinancing/{}".format(comp_id), **kwargs)

    def list_child_core(self, **kwargs):
        # 下级核心企业列表
        return self.post("/core/child/list", **kwargs)

    def add_lmt(self, **kwargs):
        # 新增额度配置
        return self.post("/add", **kwargs)

    def modify_lmt(self, **kwargs):
        # 修改额度配置
        return self.post("/modify", **kwargs)

    def freeze_lmt(self, **kwargs):
        # 审核额度冻结
        return self.post("/freeze", **kwargs)

    def unfreeze_lmt(self, **kwargs):
        # 审核额度解冻
        return self.post("/unfreeze", **kwargs)

    def recycle_lmt(self, **kwargs):
        # 释放额度申请
        return self.post("/recycle", **kwargs)

    def audit_batch_agree_lmt(self, **kwargs):
        # 额度配置批量审核同意
        return self.post("/batch/audit/agree", **kwargs)

    def audit_rollback_lmt(self, **kwargs):
        # 额度配置批量审核拒绝
        return self.post("/batch/audit/disagree", **kwargs)

    def audit_disagree_lmt(self, **kwargs):
        # 额度配置批量审核回退
        return self.post("/batch/audit/rollback", **kwargs)

    def download(self, **kwargs):
        # 融资额度管理导出文件
        return self.post("/download", **kwargs)

    def temp_export(self, **kwargs):
        # 融资额度已审核导出文件
        return self.post("/temp/export", **kwargs)

    def download_child(self, **kwargs):
        # 分配融资额度导出文件
        return self.post("/child/download", **kwargs)

    def download_child_lmt(self, **kwargs):
        # 额度分配查询已生效导出
        return self.post("/child2/download", **kwargs)


SunAppLmt = SunAppLmtController(root_api_url, "/app/v1/sys/lmt")
