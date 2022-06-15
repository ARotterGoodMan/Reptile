# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：asyncio_webdriver.py
    @Author ：ARotterGoodMan
    @Date ：2022/6/15 11:42
"""
import asyncio
import aiohttp
import aiofiles
from tqdm import tqdm
from lxml import etree


class AsyncioWebdriver:
    def __init__(self):
        self.school_list = []
        self.url_list = []
        self.header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/102.0.5005.13 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.13 Safari/537.36",
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                                 "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                       }

    def get_url(self):
        with open('AcquiredData/school.csv', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                school, url = line.split(',')
                url = "https://gaokao.chsi.com.cn" + url.strip()
                self.school_list.append(school)
                self.url_list.append(url)

    async def start_session(self):
        tasks = []
        async with aiohttp.ClientSession(headers=self.header) as session:
            for i in tqdm(range(0, len(self.url_list))):
                tasks.append(asyncio.create_task(self.get_links(session, self.school_list[i], self.url_list[i])))
                await asyncio.sleep(0.01)
            await asyncio.wait(tasks)

    async def get_links(self, session, school, url):
        async with session.get(url) as response:
            html = await response.text()
            tree = etree.HTML(html)
            links = tree.xpath('/html/body/div[1]/div[4]/div/div/div[2]/table/tr[1]/td[1]/a/@href')
            self.write_links(school, links)
            self.write_have(school, links)

    @staticmethod
    def write_links(school, links):
        with open('AcquiredData/school_links.txt', 'a', encoding='utf-8') as f:
            if len(links) != 0:
                f.write(school + ', ')
                for link in links:
                    link = "https://gaokao.chsi.com.cn" + link.strip()
                    f.write(link + '\n')
            else:
                f.write('')

    @staticmethod
    def write_have(school, links):
        with open('AcquiredData/school_have.txt', 'a', encoding='utf-8') as f:
            if len(links) == 0:
                f.write('')
            else:
                f.write(school + '\n')

    def main(self):
        self.get_url()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start_session())
