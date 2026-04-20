from create_request_data import create_request_data
from eportal import login
from redirect import extract_query_string, get_redirect_query_string
from check_network import check_network

student_id = "学号"
password = "密码"

default_url = "默认重定向URL"


def main():
    is_connected = check_network()

    if is_connected:
        return

    query_string = get_redirect_query_string() or extract_query_string(
        f"top.self.location.href='{default_url}'"
    )

    payload = create_request_data(student_id, password, query_string)

    login_response = login(payload)

    print(login_response.text)


if __name__ == "__main__":
    main()
