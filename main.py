from eportal import login
from utils import *

student_id = "学号"
password = "密码"

default_url = "已知重定向URL"


def main():
    is_connected = check_network()

    if is_connected:
        return

    query_string = extract_query_string(
        f"top.self.location.href='{default_url}'" or get_redirect_query_string()
    )

    payload = create_request_data(student_id, password, query_string)

    login_response = login(payload)

    print(login_response.text)


if __name__ == "__main__":
    main()
