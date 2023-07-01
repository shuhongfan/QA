# 获取图片验证码

# 导包
import requests

# 发送请求
response = requests.get(url="http://kdtx-test.itheima.net/api/captchaImage")

# 查看响应
print(response.status_code)
print(response.text)

