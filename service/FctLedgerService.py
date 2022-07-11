# coding=utf-8
"""
    融资台账管理
"""
from controller.app.FctLedgerController import FctLedger
from core.result_base import ResultBase
from service.service_config import header
from common.logger import Logger


logger = Logger("service").logger


def page_fct_ledger(financing_name="", start_amt="", end_amt="", start_date="", end_date="",
                    current=1, seller_name="", size=10, fct_status="0"):
    """
    获取融资台账列表（分页）
    """
    result = ResultBase()
    res = FctLedger.page_fct_ledger(headers=header, json={
        "current": current,
        "size": size,
        "startDate": start_date,
        "endDate": end_date,
        "financingName": financing_name,
        "startAmt": start_amt,
        "endAmt": end_amt,
        "sellerName": seller_name,
        "fctStatus": fct_status
    })
    if res.status_code == 200:
        result.msg = res.json().get("msg")
        result.code = res.json().get("code")
        result.data = res.json().get("data")
        result.status = res.json().get("status")
        result.success = res.json().get("success")

    else:
        result.error = "接口返状态是 【 {} 】, 返回信息：{} ".format(res.status_code, res.json())
    result.response = res
    return result


def export_fct_ledger(financing_name="", start_amt="", end_amt="", start_date="", end_date="",
                      current=1, seller_name="", size=10, fct_status="0"):
    """
    获取融资台账列表（分页）
    """
    result = ResultBase()
    res = FctLedger.export_fct_ledger(headers=header, json={
        "current": current,
        "size": size,
        "startDate": start_date,
        "endDate": end_date,
        "financingName": financing_name,
        "startAmt": start_amt,
        "endAmt": end_amt,
        "sellerName": seller_name,
        "fctStatus": fct_status
    })
    if res.status_code == 200:
        result.msg = res.json().get("msg")
        result.code = res.json().get("code")
        result.data = res.json().get("data")
        result.status = res.json().get("status")
        result.success = res.json().get("success")

    else:
        result.error = "接口返状态是 【 {} 】, 返回信息：{} ".format(res.status_code, res.json())
    result.response = res
    return result


def list_supplier_financing(current=1, size=10, supplier_name=""):
    # logger.info("供应商融资查询 supplierName:{}".format(supplier_name))
    """
    供应商融资查询
    """
    result = ResultBase()
    res = FctLedger.list_supplier_financing(headers=header, json={
        "current": current,
        "size": size,
        "supplierName": supplier_name
    })
    if res.status_code == 200:
        result.msg = res.json().get("msg")
        result.code = res.json().get("code")
        result.data = res.json().get("data")
        result.status = res.json().get("status")
        result.success = res.json().get("success")

    else:
        result.error = "接口返状态是 【 {} 】, 返回信息：{} ".format(res.status_code, res.json())
    result.response = res
    return result


if __name__ == '__main__':
    print(export_fct_ledger().response.request)
    pass
    # json_res = page_fct_ledger().response.json()['data']['records']
    # json_txt = json.dumps(json_res)
    # dataframe = pd.read_json(json_txt, orient="records")
    # print(dataframe)
    # export_fct_ledger()



