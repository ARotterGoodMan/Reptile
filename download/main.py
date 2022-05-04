# 这是一个示例 Python 脚本。

from src import pianku1
from src import m3u8class

if __name__ == '__main__':
    FilmLibrary = pianku1.FilmLibrary()
    url = input("请输入要拉取的m3u8文件：")
    FilmLibrary.run(url)
    GetM3u8 = m3u8class.GetM3u8()
    GetM3u8.main()
