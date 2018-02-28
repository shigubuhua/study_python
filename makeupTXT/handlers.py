class Handler(object):
    """文本解析处理程序的父类"""

    def callback(self, prefix, name, *args):
        '''检查函数是否能够被调用，如果可以调用则返回函数调用'''

        # 相当于 slef.prefixname ，如果没有这个属性，则返回None
        # prefix 类似于 start_ end_ sub_，name类似于document
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        '''调用子类具体的开始函数'''
        self.callback('start_', name)

    def end(self, name):
        '''调用子类具体的结束函数'''
        self.callback('end_', name)

    def sub(self, name):
        '''调用子类具体的子部分函数
        生成子串，包含在外标签中的子标签串'''
        def substitution(match):
            result = self.callback('sub_', name, match)  # match是什么？
            if result is None:
                result = match.group(0)  # group() group(0) group(1) 似乎无差别
            return result
        return substitution


class HTMLRenderer(Handler):
    """HTML 处理程序，给文本块加相应的 HTML 标记
    定义开始-结束标记对等"""

    def start_document(self):
        print("<html><head><title>shigubuhua</title></head><body>")

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
        # group() group(0) group(1) 似乎无差别
        return('<em>%s</em>' % match.group(1))

    def sub_url(self, match):
        return '<a target="_blank" style="text-decoration: none;color: #BC1A4B;" \
        href="%s">%s</a>' % (match.group(1), match.group(1))

    def sub_mail(self, match):
        return '<a style="text-decoration: none;color: #BC1A4B;" \
        href="mailto:%s">%s</a>' % (match.group(1), match.group(1))

    def feed(self, data):
        print(data)
