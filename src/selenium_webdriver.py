# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：selenium_webdriver.py
    @Author ：ARotterGoodMan
    @Date ：2022/5/27 21:25
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import aiohttp
import asyncio
import aiofiles
from lxml import etree

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/102.0.5005.13 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.13 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                    "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          }


def run():
    driver = webdriver.Chrome()
    with open('AcquiredData/school.csv', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            school, url = line.split(',')
            url = "https://gaokao.chsi.com.cn" + url.strip()
            driver.get(url)
            # 找到页面上的链接的xpath
            links = driver.find_elements(By.XPATH, '/html/body/div[1]/div[4]/div/div/div[2]/table/tbody/tr[1]/td[1]/a')
            # 创建一个文件，写入学校名称
            with open('AcquiredData/school_links.txt', 'a', encoding='utf-8') as f:
                # 如果不存在链接，则写空
                if len(links) == 0:
                    f.write('')
                else:
                    f.write(school + ',')
                    for link in links:
                        f.write(link.get_attribute('href') + '\n')
