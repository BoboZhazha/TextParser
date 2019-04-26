#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-26 15:13
# @Author  : zhangshanbo
# @File    : util.py
# @Remark:


def lines(file):
    for line in file:
        yield line
        yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.split():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


