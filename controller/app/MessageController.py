# coding=utf-8
"""
    企业端消息管理
"""
from core.rest_client import RestClient
from config.data import root_api_url


class MessageController(RestClient):

    def __init__(self, root_url, branches_url):
        super().__init__(root_url, branches_url)

    def list_sys_message(self, **kwargs):
        # 获取站内信列表
        return self.post("/sys/list", **kwargs)

    def page_all_message(self, **kwargs):
        # 登录获取公告列表
        return self.post("/sys/all/page", **kwargs)

    def count_sys_personal_message(self, **kwargs):
        # 登录获取私信
        return self.post("/sys/personal/count", **kwargs)

    def read_message(self, **kwargs):
        # 消息记录已读
        return self.post("/sys/read", **kwargs)

    def del_message(self, **kwargs):
        # 消息记录删除
        return self.post("/sys/del", **kwargs)


Message = MessageController(root_api_url, "/app/message/manager")
