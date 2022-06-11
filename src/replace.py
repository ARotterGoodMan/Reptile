# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：replace.py
    @Author ：ARotterGoodMan
    @Date ：2022/5/28 11:27
"""
import re
import os
from tqdm import tqdm


class Replace:
    def __init__(self):
        pass

    @staticmethod
    def alter(file, old_str, new_str):
        with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
            for line in f1:
                f2.write(re.sub(old_str, new_str, line))
        os.remove(file)
        os.rename("%s.bak" % file, file)

    @staticmethod
    def read_csv():
        with open("AcquiredData/school.csv", "r", encoding="utf-8") as f:
            nums = len(f.readlines())

        with open("AcquiredData/school.csv", "r", encoding="utf-8") as f:
            with open("AcquiredData/school_need.bat", "a", encoding="utf-8") as f1:
                f1.write("chcp 65001\n")
                f1.write("cd html\n")
                for i in range(nums):
                    line = f.readline()
                    f1.write(f"ren {line.split(',')[0]}.html {i}.html\n")
        os.system(".\\AcquiredData\\school_need.bat")

    def main(self):
        for file in tqdm(os.listdir("html")):
            # for file in os.listdir("html"):
            file_name = os.path.join("html", file)
            file_name = file_name.replace("../", "")
            file_name = file_name.replace(r"\\", "/")
            self.alter(file_name, r"/zsgs/zhangcheng/listVerifedZszc--method-index,lb-\d{1,10}.dhtml", r"/school")
            self.alter(file_name, r"/zsgs/zhangcheng/listZszc--schId-\d{1,10}.dhtml", "")
        self.read_csv()
