import json
import os

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture()
def load_json_data():
    print("Current working directory:", os.getcwd())
    file_name = os.path.join(os.getcwd(), os.getenv("load_env"))
    print(file_name)
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


def test_make_req(load_json_data):
    print(load_json_data)
