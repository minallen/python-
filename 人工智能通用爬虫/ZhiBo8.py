import requests



class ZhiBo8:

    def run(self):
        responce = requests.get(url='https://www.zhibo8.cc/')
        print(responce.content.decode())

        return responce


if __name__ == '__main__':
    zz = ZhiBo8()
    zz.run()
