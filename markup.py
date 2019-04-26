#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re
from handers import *
from util import *
from rules import *

class Parser:

    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []


    def addRule(self, rule):
        self.rules.append(rule)


    def addFilter(self, pattern, name):
        def filter(block, handler):
            a = re.sub(pattern, handler.sub(name), block)
            return a
        self.filters.append(filter)


    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
        self.handler.end('document')



class BasicTextParser(Parser):
    """
    纯文本解析器
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

"""
运行程序
"""
if __name__ == '__main__':
    f = open('test.txt',encoding='utf8')
    handler = HTMLRenderer()
    parser = BasicTextParser(handler)
    parser.parse(f)