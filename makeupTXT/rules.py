class Rule(object):
    """
    规则父类，规则：判断每个文本块交给处理程序要加上什么标记
    以下的condition和action的返回值都是布尔值，
    用于判断标签添加适用规则和循环
    """

    def action(self, block, handler):
        '''加标记'''

        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    """1#标题规则 <h2>"""
    type = "heading"

    def condition(self, block):
        '''判断文本块是否符合规则'''
        # 没有换行 且 长度不大于70 且 最后字符不是冒号
        return "\n" not in block and len(block) <= 70 and not block[-1] == ":"


class TitleRule(HeadingRule):
    """2#标题规则 <h1>"""
    type = "title"
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False  # 不能第二次出现
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):
    """列表项li规则"""

    type = 'listitem'

    def condition(self, block):
        return block[0] == "-"  # 以“-”开头

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(ListItemRule):
    """列表ul规则，处理li嵌套"""
    type = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ParagraphRule(Rule):
    """段落规则"""
    type = 'paragraph'

    def condition(self, block):
        return True
