import requests


def get_online_user_info(user_index: str, user_name: str, password: str):
    url = "http://10.0.6.247/eportal/InterFace.do?method=getOnlineUserInfo"
    payload = {"userIndex": user_index}
    headers = {
        "Cookie": f"EPORTAL_COOKIE_USERNAME={user_name};EPORTAL_COOKIE_PASSWORD={password}"
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    response.encoding = response.apparent_encoding
    return response


def login(payload):
    login_response = requests.post(
        "http://10.0.6.247/eportal/InterFace.do?method=login",
        data=payload,
    )
    login_response.encoding = login_response.apparent_encoding
    return login_response
