# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：replace.py
    @Author ：ARotterGoodMan
    @Date ：2022/5/28 11:27
"""
import re
import os


def alter(file, old_str, new_str):
    with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(re.sub(old_str, new_str, line))
    os.remove(file)
    os.rename("%s.bak" % file, file)


def read_csv():
    with open("AcquiredData/school.csv", "r", encoding="utf-8") as f:
        number = 0
        with open("AcquiredData/school_need.bat", "a", encoding="utf-8") as f1:
            f1.write("chcp 65001\n")
            f1.write("cd html\n")
            for line in f:
                # 以,分割每一行
                f1.write(f"ren {line.split(',')[0]}.html {number}.html\n")
                number += 1
        os.system("AcquiredData/school_need.bat")


def run():
    for file in os.listdir("html"):
        # 获取文件名
        file_name = os.path.join("html", file)
        file_name = file_name.replace("../", "")
        file_name = file_name.replace(r"\\", "/")
        # 获取文件内容
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
        #     # 将文件中的/zsgs/zhangcheng/listVerifedZszc--method-index,lb-\d{1,10}.dhtml替换为/school
        alter(file_name, r"/zsgs/zhangcheng/listVerifedZszc--method-index,lb-\d{1,10}.dhtml", r"/school")
        #     # 将文件中的/zsgs/zhangcheng/listZszc--schId-5410609.dhtml替换为空
        alter(file_name, r"/zsgs/zhangcheng/listZszc--schId-\d{1,10}.dhtml", "")
    read_csv()
