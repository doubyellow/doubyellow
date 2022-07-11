import pytest
from service.FctLedgerService import *
from testcases.api_test.conftest import fct_ledger_data
from common.logger import Logger
import allure

logger = Logger("testcases").logger


@allure.step("使用”海尔集团公司 13758237929 123456“登录企业端")
def step_1():
    logger.info("步骤1 ==>> 在企业端登录核心企业账号")


@allure.step("进入签发功能-统计查询-供应商融资查询")
def step_2():
    logger.info("步骤2 ==>>  进入签发功能-统计查询-供应商融资查询")


@allure.step("输入供应商名称-点击查询")
def step_3():
    logger.info("步骤3 ==>>  输入供应商名称-点击查询")


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("融资台账管理")
class TestFctLedger:
    """融资台账管理"""

    @allure.story("供应商融资查询测试用例")
    @allure.issue("http://172.1.2.112:10071/zentao/", name="点击，跳转到禅道登录页面")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.single
    @pytest.mark.parametrize("current, size,supplier_name, except_status, except_msg, except_code, except_success",
                             fct_ledger_data["list_supplier_financing"])
    def test_list_supplier_financing(self, current, size, supplier_name,
                                     except_status, except_msg, except_code, except_success):
        step_1()
        step_2()
        step_3()
        logger.info("*************** 开始执行用例 ***************")
        list_supplier_financing_result = list_supplier_financing(current, size, supplier_name)
        assert list_supplier_financing_result.response.status_code == 200, list_supplier_financing_result.error
        assert list_supplier_financing_result.status == 0
        assert list_supplier_financing_result.success is True
        assert list_supplier_financing_result.code == "10000"
        assert list_supplier_financing_result.msg == "处理成功"
        for item in list_supplier_financing_result.data["records"]:
            assert supplier_name in item["supplierName"]
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(10000, list_supplier_financing_result.code))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_FctLedger.py"])
