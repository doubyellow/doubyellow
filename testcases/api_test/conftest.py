import pytest
import os
from common.read_data import data


# @pytest.fixture(scope="function")
# def testcase_data(request):
#     testcase_name = request.function.__name__
#     return fct_ledger_data.get(testcase_name)


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


BASE_PATH =os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
fct_ledger_data = get_data("FctLedgerData.yml")
if __name__ == '__main__':
    print(fct_ledger_data)
