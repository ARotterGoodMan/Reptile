# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：se.py
    @Author ：ARotterGoodMan
    @Date ：2022/5/27 21:25
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


def run():
    driver = webdriver.Chrome()
    with open('../data/school.csv', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            school, url = line.split(',')
            url = "https://gaokao.chsi.com.cn" + url.strip()
            driver.get(url)
            # 找到页面上的链接的xpath
            links = driver.find_elements(By.XPATH, '/html/body/div[1]/div[4]/div/div/div[2]/table/tbody/tr[1]/td[1]/a')
            # 创建一个文件，写入学校名称
            with open('../data/school_links.txt', 'a', encoding='utf-8') as f:
                # 如果不存在链接，则写空
                if len(links) == 0:
                    f.write('')
                else:
                    f.write(school + ',')
                    for link in links:
                        f.write(link.get_attribute('href') + '\n')
