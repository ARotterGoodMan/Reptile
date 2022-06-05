# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：selenium_webdriver.py
    @Author ：ARotterGoodMan
    @Date ：2022/5/27 21:25
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/102.0.5005.13 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.13 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                    "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          }



def get_url():
    school_list = [];
    url_list = [];
    with open('AcquiredData/school.csv', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            school, url = line.split(',')
            url = "https://gaokao.chsi.com.cn" + url.strip()
            school_list.append(school)
            url_list.append(url)
    return school_list, url_list


def write_links(driver, school_list, url_list):
    for i in range(len(url_list)):
        driver.get(url_list[i])
        links = driver.find_elements(By.XPATH, '/html/body/div[1]/div[4]/div/div/div[2]/table/tbody/tr[1]/td[1]/a')
        with open('AcquiredData/school_links.txt', 'a', encoding='utf-8') as f:
            if len(links) == 0:
                f.write('')
            else:
                f.write(school_list[i] + ', ')
                for link in links:
                    f.write(link.get_attribute('href') + '\n')


def main():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome()
    datas = get_url()
    write_links(driver, datas[0], datas[1])
