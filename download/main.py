from src import FilmLibrary
from src import Download

if __name__ == '__main__':
    FilmLibrary = FilmLibrary.FilmLibrary()
    url = input("请输入要拉取的m3u8文件：")
    FilmLibrary.run(url)
    video_name = input("请输入下载视频的文件名")
    Download = Download.Download()
    Download.main(url, video_name)
