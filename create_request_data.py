import urllib.parse

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
