import re
import urllib.parse

import requests


def check_network(timeout=10):
    response = requests.get(
        "http://www.msftconnecttest.com/connecttest.txt",
        timeout=timeout,
    )
    return response.status_code == 200 and response.text == "Microsoft Connect Test"


def extract_query_string(text):
    match = re.search(r"top\.self\.location\.href='[^'?]+\?([^']*)'", text)
    return match.group(1) if match else None


def get_redirect_query_string(timeout=10):
    response = requests.get(
        "http://www.msftconnecttest.com/redirect",
        timeout=timeout,
        allow_redirects=True,
    )
    query_string = extract_query_string(response.text)
    return query_string


def create_request_data(student_id, password, query_string):
    return {
        "userId": student_id,
        "password": password,
        "service": "",
        "queryString": urllib.parse.quote(query_string, safe=""),
        "operatorPwd": "",
        "operatorUserId": "",
        "validcode": "",
        "passwordEncrypt": "false",
    }
