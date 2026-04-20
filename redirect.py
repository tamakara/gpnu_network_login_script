import re

import requests

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