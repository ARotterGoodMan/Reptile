# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：start.py
    @Author ：ARotterGoodMan
    @Date ：2022/5/27 15:48
"""
import aiohttp
import asyncio
import requests
import os
from lxml import etree
from tqdm import tqdm

url_list = []
for i in range(28):
    url_list.append(
        f"https://gaokao.chsi.com.cn/zsgs/zhangcheng/listVerifedZszc--method-index,lb-1,start-{i * 100}.dhtml"
    )

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/102.0.5005.13 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.13 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                    "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          }

req = requests.get(url="https://gaokao.chsi.com.cn/zsgs/zhangcheng/listVerifedZszc--method-index,lb-1,start-0.dhtml",
                   headers=header)
dirs = ["AcquiredData", "html", "Province"]


async def get_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()


# 将返回值使用xpath解析
def parse_html(html):
    html = etree.HTML(html)
    # 获取所有的tr里td的a标签的内容
    school_name = html.xpath('/html/body/div[3]/table[2]/tbody/tr/td/a/text()')
    school_href = html.xpath('/html/body/div[3]/table[2]/tbody/tr/td/a/@href')
    # 将school_name和school_href创建成数组
    school_list = []
    for i in range(len(school_name)):
        school_list.append([school_name[i], school_href[i]])
    return school_list


def parse_html_have(html):
    html = etree.HTML(html)
    school_name = html.xpath('/html/body/div[3]/table[2]/tbody/tr/td/a[not(@style)]/text()')
    school_list = []
    for i in range(len(school_name)):
        school_list.append([school_name[i]])
    return school_list


def write_school_name(htmls):
    for html in tqdm(htmls):
        school_list = parse_html(html)
        school_list_have = parse_html_have(html)
        for school in school_list:
            school_name = school[0].strip()
            school_href = school[1].strip()
            if not os.path.exists("AcquiredData"):
                os.makedirs("AcquiredData")
            with open("AcquiredData/school.csv", "a", encoding="utf-8") as f:
                f.write(school_name + "," + school_href + "\n")
        for school in school_list_have:
            school_name = school[0].strip()
            if not os.path.exists("AcquiredData"):
                os.makedirs("AcquiredData")
            with open("AcquiredData/school_have.txt", "a", encoding="utf-8") as f:
                f.write(school_name + "\n")


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [get_html(url) for url in url_list]
    htmls = loop.run_until_complete(asyncio.gather(*tasks))
    write_school_name(htmls)
