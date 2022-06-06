# -*- coding: utf-8 -*-
"""
    @Project ：school
    @File ：Confirm.py
    @Author ：ARotterGoodMan
    @Date ：2022/6/6 14:01
"""


def main(fun, nextfun):
    while True:
        print(f'{fun}完成,是否{nextfun}？(y/n)')
        choice = input()
        if choice == 'y':
            break
        elif choice == 'n':
            exit()
