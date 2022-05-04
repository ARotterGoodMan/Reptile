import requests


class Test(object):
    def __init__(self):
        self.url = None
        self.header = None
        self.kw = None
        self.search = None
        self.file_path = "index.html"

    def get_url_list(self):
        # self.search = input("请输入要搜索的内容：")
        self.kw = {"wd": self.search}
        self.header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/102.0.5005.13 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.13 Safari/537.36"}
        self.url = "https://v.qq.com/x/cover/m441e3rjq9kwpsc.html"

    def parse_url(self):
        # req = requests.get(self.url, params=self.kw, headers=self.header)
        req = requests.get(self.url)
        req.encoding = "utf-8"
        print(req.url)
        return req.text

    def save_html(self, text):
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(text)

    def run(self):
        self.get_url_list()
        text = self.parse_url()
        self.save_html(text)
