# 需求：登录成功

# 导包
import requests

# 发送请求
url = "http://kdtx-test.itheima.net/api/login"
header_data = {
    "Content-Type": "application/json"
}
login_data = {
    "username": "admin",
    "password": "admin123",
    "code": 2,
    "uuid": "f3334fd726bf4155b787198c701786b6"
}
response = requests.post(url=url, headers=header_data, json=login_data)

# 查看响应
print(response.status_code)
print(response.json())

