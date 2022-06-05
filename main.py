# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：start.py
    @Author ：ARotterGoodMan
    @Date ：2022/5/27 15:48
"""
from src import replace, selenium_webdriver, start, GitContent, province_start

if __name__ == '__main__':
    start.run()
    selenium_webdriver.run()
    GitContent.run()
    province_start.run()
    replace.run()
