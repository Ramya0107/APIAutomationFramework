import json

import requests


def get_request(url, auth, in_json):
    get_response_data = requests.get(url=url, auth=auth)
    if in_json is True:
        return get_response_data.json()
    return get_response_data


def post_request(url, auth, headers, payload, in_json):
    post_response_data = requests.post(url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return post_response_data.json()
    return post_response_data


def patch_request(url, headers, auth, payload, in_json):
    patch_response_data = requests.post(url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def delete_request(url, headers, auth, payload, in_json):
    delete_response_data = requests.post(url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data