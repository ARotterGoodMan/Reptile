# 这是一个示例 Python 脚本。

from src import FilmLibrary
from src import Download

if __name__ == '__main__':
    FilmLibrary = FilmLibrary.FilmLibrary()
    url = input("请输入要拉取的m3u8文件：")
    FilmLibrary.run(url)
    Download = Download.Download()
    Download.main(url)
