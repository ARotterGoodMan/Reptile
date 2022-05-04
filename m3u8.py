import aiohttp
import requests

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/102.0.5005.13 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.13 Safari/537.36"}
lineList = []
with open("index.m3u8", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            continue
        lineList.append(f"https://b3.szjal.cn/20191208/xoWqp5BJ/hls/{line}")
        # print(f"https://b3.szjal.cn/20191208/xoWqp5BJ/hls/{line}")
for url in lineList:
    req = requests.get(url, headers=header)
    filename = url.split("/")[-1]
    with open("addNum.sh", mode="a", encoding="utf-8") as f1:
        f1.write(f"ren {filename} {lineList.index(url)}.ts\n")

    with open(f"video_ts/{filename}", mode="wb") as f:
        f.write(req.content)

    print(f"{filename}   ok!!!!")
print("ok!!!!!")
