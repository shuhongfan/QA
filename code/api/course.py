# 课程模块接口封装：核心在于依据接口文档实现接口信息封装、重点关注接口如何被调用
# 接口信息：
# URL：http://kdtx-test.itheima.net/api/clues/course
# 方法：Post
# 请求数据：
# 请求头：{ "Content-Type ":  "application/json ",  "Authorization":  "xxx " }
# 请求体：{ "name": "测试开发提升课01", "subject": "6","price": 899,"applicablePerson": "2",  "info": "测试开发提升课01"}

# 导包
import requests
import config


# 创建接口类
class CourseAPI:
    # 初始化
    def __init__(self):
        # self.url_add_course = "http://kdtx-test.itheima.net/api/clues/course"
        self.url_add_course = config.BASE_URL + "/api/clues/course"
        # self.url_select_course = "http://kdtx-test.itheima.net/api/clues/course/list"
        self.url_select_course = config.BASE_URL + "/api/clues/course/list"

    # 课程添加
    def add_course(self, test_data, token):
        return requests.post(url=self.url_add_course, json=test_data, headers={"Authorization": token})

    # 查询课程列表
    def select_course(self, test_data, token):
        return requests.get(url=self.url_select_course + f"/{test_data}", headers={"Authorization": token})

    # 修改课程
    def update_course(self, test_data, token):
        return requests.put(url=self.url_add_course, json=test_data, headers={"Authorization": token})

    # 删除课程
    def delete_course(self, course_id, token):
        return requests.delete(url=self.url_add_course + f"/{course_id}", headers={"Authorization": token})


