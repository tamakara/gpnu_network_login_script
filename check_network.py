import requests


def check_network(timeout=10):
    response = requests.get(
        "http://www.msftconnecttest.com/connecttest.txt",
        timeout=timeout,
    )
    return response.status_code == 200 and response.text == "Microsoft Connect Test"


is_connected = check_network()

print(f"网络连接状态: {'已连接' if is_connected else '未连接'}")
