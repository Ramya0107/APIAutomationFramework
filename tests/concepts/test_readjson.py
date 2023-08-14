import json
import os

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture()
def load_json_data():
    path = str(os.getcwdb())
    filename = str(os.getenv("load_env"))
    print("Current working directory:", os.getcwdb())
    print("json file name: ", os.getenv("load_env"))
    # "<json directory>" - give the directory where json file is available
    file_name = "<json directory>" + filename
    print(file_name)
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


def test_make_req(load_json_data):
    print(load_json_data)
