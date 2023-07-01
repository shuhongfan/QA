# 导包
from api.login import LoginAPI
from api.course import CourseAPI


# 创建测试类
class TestCourseAPI:
    # 初始化
    TOKEN = None

    # 前置处理
    def setup(self):
        # 初始化接口类
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        # 登录成功
        # 获取验证码
        res_v = self.login_api.get_verify_code()
        # 登录
        login_data = {
            "username": "admin",
            "password": "admin123",
            "code": "2",
            "uuid": res_v.json().get("uuid")
        }
        res_l = self.login_api.login(test_data=login_data)
        # 提取登录成功的token数据并保存
        TestCourseAPI.TOKEN = res_l.json().get("token")
        print(TestCourseAPI.TOKEN)

    # 课程删除成功
    def test01_delete_success(self):
        response = self.course_api.delete_course(course_id=110, token=TestCourseAPI.TOKEN)
        print(response.json())
        # 断言响应状态码
        assert 200 == response.status_code
        # 断言返回消息
        assert "成功" in response.text
        # 断言code值
        assert 200 == response.json().get("code")

    # 课程删除失败（课程id不存在）
    def test02_delete_fail_id_not_exist(self):
        response = self.course_api.delete_course(course_id=666, token=TestCourseAPI.TOKEN)
        print(response.json())
        # 断言响应状态码
        assert 200 == response.status_code
        # 断言返回消息
        assert "失败" in response.text
        # 断言code值
        assert 500 == response.json().get("code")

    # 课程删除失败（用户未登录）
    def test03_delete_fail(self):
        response = self.course_api.delete_course(course_id=110, token="xxx")
        print(response.json())
        # 断言响应状态码
        assert 200 == response.status_code
        # 断言返回消息
        assert "认证失败" in response.text
        # 断言code值
        assert 401 == response.json().get("code")
