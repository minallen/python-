import requests, json


class Fanyi:

    def __init__(self, trans_str):
        self.trans_str = trans_str

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Mobile Safari/537.36"
        }
        # 检测url
        self.url_jiance = "https://fanyi.baidu.com/langdetect"

        # 翻译url
        self.url_fanyi = "https://fanyi.baidu.com/basetrans"

    def parse(self, url, data):
        response1 = requests.post(url, data=data, headers=self.headers)
        # 需要返回的是字典类型，所以需要用json
        response2 = json.loads(response1.content.decode())
        return response2

    def fetch_data(self, data):
        # response4 = data["trans"][0]["dst"]
        # print('结果是：', response4)
        print(data)

    def run(self):
        '''
        1.进行语言类型检测
        2.发送post请求,获取响应
        3.提取数据

        '''

        # 检测语言类型时准别的数据
        jiance_data = {"query": self.trans_str}
        # 获取语言类型
        lang = self.parse(self.url_jiance, jiance_data)["lan"]
        # 准备翻译的数据
        fanyi_data = {"query": self.trans_str, "from": "zh", "to": "en"} if lang == 'zh' else \
            {"query": self.trans_str, "from": "en", "to": "zh"}
        # 翻译完返回的数据response3
        response3 = self.parse(self.url_fanyi, fanyi_data)
        # 提取数据
        self.fetch_data(response3)


if __name__ == '__main__':
    fanyi = Fanyi('你好')
    fanyi.run()
