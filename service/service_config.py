import os
import pytest
from common.read_data import *


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 请请求头
header = get_data("api_header.yml")["cope_header"]

if __name__ == '__main__':
    print(header)
