import requests
import json


class BaiduFanyi:

    def __init__(self, trans_str):
        # 翻译的数据
        self.trans_str = trans_str

        # 检测语言类型的地址
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"

        # 进行翻译的地址
        self.trans_url = "https://fanyi.baidu.com/basetrans"

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Mobile Safari/537.36"
        }

    def parse(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        return json.loads(response.content.decode())

    def get_ret(self, dict_response):  # 提取翻译的结果
        ret = dict_response['trans'][0]['dst']
        print("result is :",ret)

    def run(self):
        '''
        #1.获取语言类型
        #2.准备post的数据
        #3.获取响应
        #4.提取翻译的结果
        :return:
        '''
        # 用于检测语言类型的数据
        lang_detect_data = {"query": self.trans_str}
        # 调用parse函数获取检测语言的类型
        lang = self.parse(self.lang_detect_url, lang_detect_data)["lan"]
        print('检测语言类型没问题', lang)

        # 准备翻译的数据
        trans_data = {"query": self.trans_str, "from": "zh", "to": "en"} if lang== 'zh' else \
           {"query": self.trans_str, "from": "en", "to": "zh"}

        dict_response = self.parse(self.trans_url, trans_data)
        print(dict_response)
        self.get_ret(dict_response)


if __name__ == '__main__':
    baidufanyi = BaiduFanyi('你好')
    baidufanyi.run()
