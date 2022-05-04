import time
import aiohttp
import aiofiles
import progressbar
import asyncio
import os


class GetM3u8(object):
    def __init__(self):
        self.download_num = 0
        self.download_over_num = 0
        self.bar = progressbar.ProgressBar(maxval=self.download_num)

    async def structure_url(self):
        tasks, indexes = [], []
        header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/102.0.5005.13 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.13 Safari/537.36"}
        async with aiohttp.ClientSession(headers=header) as session:  # 提前准备好session
            async with aiofiles.open("index.m3u8", mode="r", encoding='utf-8') as f:
                async for line in f:
                    if line.startswith("#"):
                        continue
                    line = line.strip()  # 去掉没用的空格和换行
                    indexes.append(line)
                    index = indexes.index(line)
                    # 拼接真正的ts路径
                    ts_url = line
                    task = asyncio.create_task(self.send_request(ts_url, session))  # 创建任务
                    tasks.append(task)
                await asyncio.wait(tasks)

            # await asyncio.wait(tasks)  # 等待任务结束
            self.download_num = len(indexes)

    async def send_request(self, ts_url, session):
        name = ts_url.split("/")[-1]
        async with session.request("get", ts_url) as resp:
            async with aiofiles.open(f"video_ts/{name}", "wb") as f:
                await f.write(await resp.content.read())
            print(f"{name}   ok!!!")

    async def merge_ts_bat(self):
        # mac: cat 1.ts 2.ts 3.ts > xxx.mp4
        # windows: copy /b 1.ts+2.ts+3.ts xxx.mp4
        async with aiofiles.open("video_ts\\merge.bat", mode="a", encoding="utf-8") as merge:
            await merge.write("copy /b ")
            with open("index.m3u8", mode="r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("#"):
                        continue
                    line = line.strip()
                    file_name = line.split("/")[-1]
                    await merge.write(f'{file_name}+')
            await merge.write(" movie.mp4")
        self.update_merge_bat()

    def update_merge_bat(self):
        merge_read = open("video_ts\\merge.bat", mode="r", encoding="utf-8")
        line2 = merge_read.read().replace("+ movie.mp4", " movie.mp4")
        merge_read.close()
        merge_update = open("video_ts\\merge.bat", mode="w", encoding="utf-8")
        merge_update.write(line2)
        merge_update.write('\nmkdir movie\n')
        merge_update.write('move movie.mp4 movie\n')

        merge_update.close()
        run_merge = open("run.bat", "w")
        run_merge.write("cd video_ts\n")
        run_merge.write("merge.bat\n")
        run_merge.close()

    def run_bat(self):
        os.system("run.bat")
        os.system('del video_ts\\*.* /Q')
        os.system("del run.bat index.m3u8")
        print("OK!!!!!!!")

    def main(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.structure_url())
        print("视频片段下载完成开始合并视频！！！！")
        time.sleep(2)
        loop.run_until_complete(self.merge_ts_bat())
        # asyncio.run(self.structure_url())
        # asyncio.run(self.merge_ts_bat())
        self.run_bat()
