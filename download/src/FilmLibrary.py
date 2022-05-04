import requests
import time


class FilmLibrary(object):
    def __init__(self):
        self.name = None
        self.header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/102.0.5005.13 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.13 Safari/537.36"}

    def req_start(self, url):
        req = requests.get(url, headers=self.header)
        req.encoding = "utf-8"
        self.name = url.split("/")[-1]
        return req.content

    def save_m3u8(self, con):
        with open("index.m3u8", "wb") as f:
            f.write(con)

    def run(self, url):
        con = self.req_start(url)
        self.save_m3u8(con)
        print("index.m3u8 拉取成功开始下载视频片段！！！！")
        time.sleep(2)
