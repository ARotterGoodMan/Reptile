# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：start.py
    @Author ：ARotterGoodMan
    @Date ：2022/5/27 15:48
"""
import aiohttp
import asyncio
from lxml import etree
import re
import os

province_list = ["11", "12", "13", "14", "15", "21", "22", "23", "31", "32", "33", "34", "35", "36", "37", "41", "42",
                 "43", "44", "45", "46", "50", "51", "52", "53", "54", "61", "62", "63", "64", "65"]
url_list = []
for province in province_list:
    for i in range(2):
        url_list.append(
            f"https://gaokao.chsi.com.cn/zsgs/zhangcheng/listVerifedZszc--method-index,ssdm-{province},start-{i * 100}.dhtml"
        )

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/102.0.5005.13 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.13 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                    "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          }


async def get_html(url, session):
    async with session.get(url) as resp:
        province_id = re.split(r"ssdm-", url)[1].split(",")[0]
        return province_id, await resp.text()


async def start_session():
    tasks = []
    datas = []
    async with aiohttp.ClientSession() as session:
        for url in url_list:
            tasks.append(asyncio.create_task(get_html(url, session)))
        await asyncio.wait(tasks)
        for task in tasks:
            datas.append(task.result())
    return datas


def parse_html(html):
    html = etree.HTML(html)
    school_name = html.xpath('/html/body/div[3]/table[2]/tbody/tr/td/a/text()')
    school_list = []
    for i in range(len(school_name)):
        school_list.append([school_name[i]])
    return school_list


def write_province(datas):
    for data in datas:
        html = data[1]
        school_list = parse_html(html)
        for school in school_list:
            school_name = school[0].strip()
            if not os.path.exists("Province"):
                os.makedirs("Province")
            with open(f"Province/{data[0]}.txt", "a", encoding="utf-8") as f:
                f.write(school_name + "\n")


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    datas = loop.run_until_complete(start_session())
    write_province(datas)
