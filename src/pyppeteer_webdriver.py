# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：pyppeteer_webdriver.py
    @Author ：ARotterGoodMan
    @Date ：2022/6/8 12:28
"""
import asyncio
import pyppeteer
import aiofiles
from lxml import etree
from tqdm import tqdm


class PyppeteerWebdriver:
    def __init__(self):
        self.school_list = []
        self.url_list = []

    def get_url(self):
        with open('AcquiredData/school.csv', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                school, url = line.split(',')
                url = "https://gaokao.chsi.com.cn" + url.strip()
                self.school_list.append(school)
                self.url_list.append(url)

    async def get_links(self, page, school, url):
        await page.goto(url, {'timeout': 1000 * 90})
        page_content = await page.content()
        html = etree.HTML(page_content)
        links = html.xpath('/html/bo'
                           'dy/div[1]/div[4]/div/div/div[2]/table/tbody/tr[1]/td[1]/a/@href')
        self.write_links(school, links)

    @staticmethod
    def write_links(school, links):
        with open('AcquiredData/school_links.txt', 'a', encoding='utf-8') as f:
            if len(links) == 0:
                f.write('')
            else:
                f.write(school + ', ')
                for link in links:
                    link = "https://gaokao.chsi.com.cn" + link.strip()
                    f.write(link + '\n')

    async def run(self):
        browser = await pyppeteer.launch({'headless': True})
        page = await browser.newPage()
        for i in tqdm(range(0, len(self.url_list))):
            await self.get_links(page, self.school_list[i], self.url_list[i])
        await browser.close()

    def main(self):
        self.get_url()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run())
