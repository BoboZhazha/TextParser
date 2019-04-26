#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Handler:

    def callback(self,prefix, name, *args):
        # gerattr()函数则是返回一个对象的属性值。举例来说，getattr(x, 'foo', None) 就相当于是 x.foo，而如果没有这个属性值foo，则返回我们设定的默认值None
        method = getattr(self, prefix + name, None)

        # callable() 函数能够检查一个函数是否能够被调用。如果能够被调用返回True
        if callable(method):
            return method(*args)


    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None: result = match.group(0)
            return result
        return substitution



class HTMLRenderer(Handler):
    """
       HTML处理程序,给文本块加相应的HTML标记
       """

    def start_document(self):
        print('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>解析器制作</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p style="color: #444;">')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2 style="color: #68BE5D;">')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul style="color: #363736;">')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1 style="color: #1ABC9C;">')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return ('<em>%s</em>' % match.group(1))

    def sub_url(self, match):
        return ('<a target="_blank" style="text-decoration: none;color: #BC1A4B;" href="%s">%s</a>' % (
        match.group(1), match.group(1)))

    def sub_mail(self, match):
        return ('<a style="text-decoration: none;color: #BC1A4B;" href="mailto:%s">%s</a>' % (
        match.group(1), match.group(1)))

    def feed(self, data):
        print(data)
if __name__ == '__main__':
    h = Handler()
    h.callback('')
