# -- coding: utf-8 --
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
import requests
import json
from common.test_xlsx import ExcelUtil
from common.log import Log

class Token(unittest.TestCase):

    log = Log()
    def setUp(self):
        self.baseURL="http://10.33.1.182:8081"
        print("\n初始化\n\n")

    def tearDown(self):
        print("测试结束\n")

    def token(self,username,password,hours):
        # 获取token的url地址
        self.baseURL = "http://10.33.1.182:8081"
        url = self.baseURL+"/gateway/risk/authorize/token"

        # 请求参数
        data = {"user_name":username,"password":password,"hours":hours}

        # 转换请求参数格式为json
        jsonpost = json.dumps(data, separators=(',', ':'), ensure_ascii=False)

        # 请求头
        headers = {"Content-Type": "application/json", "charset": "utf-8"}

        # 响应报文
        response = requests.post(url, data=jsonpost.encode('utf-8'), headers=headers)

        # 响应结果转化为json
        status = json.loads(response.content)["status"]

        # 断言结果是否正确
        self.assertEqual(status, "SUCCESS", msg='失败原因是:%s!=SUCCESS' % status)

        print("获取%s token成功\n\n"%username)

        # 获取商户token
        token = json.loads(response.content)['data']['token']
        return token

    def test_token(self):

        self.log.info("---start---")
        # 实例化对象，用于调用token
        testdata = ExcelUtil.test_data()
        # username = testdata[0]["username"]
        for i in range(3):
            username = testdata[1][i]["username"]
            print(username)
            password = testdata[1][i]["password"]
            print(password)
            hours = testdata[1][i]["hours"]
            print(hours)
            token = self.token(username, password, hours)
            if username == 'szqb':
                szqb_test_token = token
            elif username == 'jjgj':
                jjgj_test_token = token
            elif username == 'ymb':
                ymb_test_token = token
            else:
                return
        return [szqb_test_token,jjgj_test_token,ymb_test_token]
        self.log.info("---end---")

if __name__ == "__main__":
    report_path = "C:\\Users\\hx\\PycharmProjects\\interfacefk\\test_report\\test_token.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(Token)
    runer = HTMLTestRunner(title="风控接口自动化测试", description="获取token接口", stream=open(report_path, "wb"), verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)