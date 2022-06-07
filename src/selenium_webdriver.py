# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：selenium_webdriver.py
    @Author ：ARotterGoodMan
    @Date ：2022/5/27 21:25
"""

from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumWebdriver:
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

    @staticmethod
    def write_links(driver, school, url):
        driver.get(url)
        links = driver.find_elements(By.XPATH, '/html/body/div[1]/div[4]/div/div/div[2]/table/tbody/tr[1]/td[1]/a')
        with open('AcquiredData/school_links.txt', 'a', encoding='utf-8') as f:
            if len(links) == 0:
                f.write('')
            else:
                f.write(school + ', ')
                for link in links:
                    f.write(link.get_attribute('href') + '\n')

    def main(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver = webdriver.Chrome()
        self.get_url()
        for i in tqdm(range(0, len(self.url_list))):
            self.write_links(driver, self.school_list[i], self.url_list[i])
