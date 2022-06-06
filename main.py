# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：start.py
    @Author ：ARotterGoodMan
    @Date ：2022/5/27 15:48
"""
from src import start, Confirm, selenium_webdriver, GitContent, province_start, replace

if __name__ == '__main__':
    input('请输入任意键开始')
    start.main()
    Confirm.main("链接获取", "进行内容链接获取")
    selenium_webdriver.main()
    Confirm.main("内容链接获取", "进行内容链接获取")
    GitContent.main()
    Confirm.main("继续内容链接获取", "进行省份院校分类文件写入")
    province_start.main()
    Confirm.main("获取省份院校分类", "进行更改文件名")
    replace.main()
    input("完成,按回车退出")
    exit()
