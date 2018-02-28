'''解析文本'''

import sys
import re
from handlers import *
from util import *
from rules import *


class Parser(object):
    """解析器父类"""

    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        '''添加规则'''
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        '''添加过滤器'''
        def filter(block, handler):
            # sub(name)返回了一个函数，接收re生成的match.group()对象
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        '''解析'''
        self.handler.start('document')  # 文件头，固定格式
        for block in blocks(file):  # 逐行（块）循环处理
            for filter in self.filters:
                # 进行文本匹配，处理em、url、mail特殊格式（子格式），生成子串
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')  # 文件尾，固定格式


class BasicTextParser(Parser):
    """纯文本解析器"""

    def __init__(self, handler):
        # Parser.__init__(self, handler)
        super(BasicTextParser, self).__init__(handler)
        self.handler = handler
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


def main():
    """
    运行程序:
    运行程序（纯文本文件为 test.txt，生成 HTML 文件为 test.html）：
    python markup.py < test.txt > test.html
    """

    handler = HTMLRenderer()
    parser = BasicTextParser(handler)
    parser.parse(sys.stdin)  # 系统默认输出输出形式或重定向


if __name__ == '__main__':
    main()
