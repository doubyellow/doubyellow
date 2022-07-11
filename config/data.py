# coding=utf-8
import os
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
root_ui_url = data.load_ini(data_file_path)["host"]["ui_root_url"]
root_api_url = data.load_ini(data_file_path)["host"]["api_root_url2"]
