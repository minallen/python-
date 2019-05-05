import json


class FetchColumn:
    """
    爬虫实现：从爬取的json文件中提取需要的字段
    """

    def __init__(self, file_path, fetch_file_name):
        self.file_path = file_path
        self.fetch_file_name = fetch_file_name

    def run(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = f.read()
            # 把字符串变成字典形式
            data = json.loads(data)
            # 提取key 为 subjects 的值
            data = data["subjects"]
            # 遍历subjects对应值的列表
            # for i in data:
            #     for key, content in i.items():
            #         if key == 'title' or key == 'url':
            #             # title = key
            #             content = content
            #             # print(content)
            #只打开一次文件，可以进行代码优化
            with open(self.fetch_file_name, 'a+', encoding='utf-8') as f:
                # 遍历subjects对应值的列表
                for i in data:
                    for key, content in i.items():
                        if key == 'title' or key == 'url':
                            # title = key
                            content = content
                            # print(content)
                            f.write(content + '\n')


if __name__ == '__main__':
    fc = FetchColumn('E:\pycharmcode\pachong\人工智能通用爬虫\韩剧.json', '韩剧.csv')
    fc.run()
