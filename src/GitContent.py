# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：GitContent.py
    @Author ：ARotterGoodMan
    @Date ：2022/5/27 22:27
"""
import asyncio
import aiohttp
import aiofiles
import os
import requests
import re


# 获取网页内容
async def get_html(school, url):
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/102.0.5005.13 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.13 Safari/537.36",
              }
    obj = re.compile(r'<div class="container zszc">(?P<content>.*?)</div>', re.S)
    if url == "https://gaokao.chsi.com.cn":
        return None
    async with aiohttp.ClientSession(headers=header) as session:
        async with session.get(url, headers=header) as resp:
            if resp.status == 200:
                html = await resp.text()
                result = obj.finditer(html)
                for it in result:
                    content = it.group("content")
                    async with aiofiles.open(f'html/{school}.html',
                                             'a', encoding='utf-8') as f:
                        head = f"""<!DOCTYPE html>
                        <html lang="zh">
                            <head>
                                 <meta charset="UTF-8">
                                 <title>{school}</title>
                                 <link rel="stylesheet" href="/css/bootstrap.min.css">
                                 <link rel="stylesheet" href="/css/school.css">
                            </head>
                            <body>
                                <div class="container">
                                                     """
                        end = """
                                        </div>
                                    </div>
                                </div>
                            </body>
                        </html>
                                                    """
                        await f.write(head)
                        await f.write(content)
                        await f.write(end)


def run():
    os.system("chcp 65001\nmkdir html")
    loop = asyncio.get_event_loop()
    tasks = []
    with open('AcquiredData/school_links.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            lines = line.split(',')
            school = lines[0].strip()
            url = lines[1].strip() + "," + lines[2].strip() + "," + lines[3].strip()
            tasks.append(get_html(school, url))
    loop.run_until_complete(asyncio.wait(tasks))
