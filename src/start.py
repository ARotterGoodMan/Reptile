# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：start.py
    @Author ：ARotterGoodMan
    @Date ：2022/6/6 16:35
"""
from src import school_start, selenium_webdriver, GetContent, province_start, replace


class Start:
    def __init__(self):
        self.GetContent = GetContent.GetContent()
        self.SchoolStart = school_start.SchoolStart()
        self.ProvinceStart = province_start.ProvinceStart()
        self.SeleniumWebdriver = selenium_webdriver.SeleniumWebdriver()
        self.Replace = replace.Replace()

    def school_start(self):
        self.SchoolStart.main()

    def province_start(self):
        self.ProvinceStart.main()

    @staticmethod
    def confirm(title, content):
        while True:
            print(f'{title}完成,是否{content}？(y/n)')
            choice = input()
            if choice == 'y':
                break
            elif choice == 'n':
                exit()

    def selenium_webdriver(self):
        self.SeleniumWebdriver.main()

    def get_content(self):
        self.GetContent.main()

    def replace(self):
        self.Replace.main()

    def run(self):
        input('请输入任意键开始')
        self.school_start()
        self.confirm("链接获取", "进行内容链接获取")
        self.selenium_webdriver()
        self.confirm("内容链接获取", "进行内容链接获取")
        self.get_content()
        self.confirm("继续内容链接获取", "进行省份院校分类文件写入")
        self.province_start()
        self.confirm("获取省份院校分类", "进行更改文件名")
        self.replace()
        input("完成,按回车退出")
        exit()
