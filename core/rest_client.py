# coding=utf-8
from json import JSONDecodeError
import requests
import json as complex_json
from common.logger import Logger

logger = Logger("core").logger


class RestClient:

    def __init__(self, root_url, branch_url, **kwargs):
        self.root_url = root_url
        self.branch_url = branch_url
        self.session = requests.session()
        self.url: str = ""
        self.method: str = ""
        self.headers = dict()
        self.data: str = ""
        self.json = dict()
        self.params = None
        self.files = None
        self.cookies = None
        self.response = None

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "PATCH", data, **kwargs)

    def request(self, leaf_url, method, data: str = None, json: dict = None, **kwargs):
        url = self.root_url + self.branch_url + leaf_url
        print(url)
        if method == "GET":
            self.response = self.session.get(url, **kwargs)
        elif method == "POST":
            self.response = requests.post(url, data, json, **kwargs)
        # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
        elif method == "PUT" and json:
            data = complex_json.dumps(json)
            self.response = self.session.put(url, data, **kwargs)
        elif method == "PATCH" and json:
            data = complex_json.dumps(json)
            self.response = self.session.patch(url, data, **kwargs)
        elif method == "PUT":
            self.response = self.session.put(url, data, **kwargs)
        elif method == "PATCH":
            self.response = self.session.patch(url, data, **kwargs)
        elif method == "DELETE":
            self.response = self.session.delete(url, **kwargs)

        self.url = url
        self.method = method
        self.data = data
        self.json = json
        self.headers = dict(**kwargs).get("headers")
        self.params = dict(**kwargs).get("params")
        self.files = dict(**kwargs).get("files")
        self.cookies = dict(**kwargs).get("cookies")
        self.request_log()
        return self.response

    def request_log(self):
        logger.info("Request Begin ==>>")
        logger.info("请求地址 url ==>> {}".format(self.url))
        logger.info("请求方式 method ==>> {}".format(self.method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("请求头 headers ==>> {}".format(complex_json.dumps(self.headers, indent=4, ensure_ascii=False)))
        logger.info("请求参数 params ==>> {}".format(complex_json.dumps(self.params, indent=4, ensure_ascii=False)))
        logger.info("请求体 data ==>> {}".format(complex_json.dumps(self.data, ensure_ascii=False)))
        logger.info("请求体 json ==>> {}".format(complex_json.dumps(self.json, ensure_ascii=False)))
        logger.info("上传文件 files ==>> {}".format(self.files))
        logger.info("cookies 参数 ==>> {}".format(complex_json.dumps(self.cookies, ensure_ascii=False)))
        logger.info("响应状态码 status_code  ==>> {}".format(self.response.status_code))
        try:
            logger.info("响应结果 response  ==>> \n{}".format(complex_json.dumps(self.response.json(), ensure_ascii=False)))
        except JSONDecodeError as e:
            logger.info("响应结果 response 无法转换成json格式 error:{}".format(str(e)))
            raise Exception("响应结果 response 无法转换成json格式")
        logger.info("<<== Request End")
