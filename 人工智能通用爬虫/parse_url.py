import requests

from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}


@retry(stop_max_attempt_number=3)  # 意思是最多可以尝试3次请求，retry 是用来捕获异常的
def _parse_url(url, method, data, proxies):
    print("*" * 10)
    if method == 'POST':
        requests.post(url, proxies, data=data, headers=headers, )
    else:
        response = requests.get(url, proxies, headers=headers, timeout=3)

    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method="GET", data=None, proxies={}):
    try:
        html_str = _parse_url(url, method, data, proxies)
    except Exception as e:
        html_str = None

    return html_str


if __name__ == '__main__':
    url = 'www.baidu.com'
    print(parse_url(url))



