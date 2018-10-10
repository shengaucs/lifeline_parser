#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file: story_block.py
@date: 2018/10/10
@author: yujiasheng
"""

import line_conf

class BaseBlock(object) :
    """基础块"""
    def __init__(self, line):
        super(BaseBlock, self).__init__()

    def get_title(self):
        raise NotImplementedError

    def get_content(self):
        raise NotImplementedError

    def operation(self, *args, **kwargs):
        raise NotImplementedError


class TitleBlock(BaseBlock):
    """名字块"""
    def __init__(self, line):
        start_index = line.find(line_conf.START_TITLE) + len(line_conf.START_TITLE)
        self.title = line[start_index : len(line) - 1]
        super(TitleBlock, self).__init__(line)


    def get_title(self):
        return self.title


    def get_content(self):
        return ""


    def operation(self, *args, **kwargs):
        pass


class ContentBlock(BaseBlock):
    """内容块"""
    def __init__(self, line):
        self.content = line[ : len(line) - 1]
        super(ContentBlock, self).__init__(line)


    def get_title(self):
        return ""


    def get_content(self):
        return self.content + "\n"


    def operation(self, *args, **kwargs):
        pass


class GotoBlock(BaseBlock):
    """跳转模块"""
    def __init__(self, line):
        start_index = line.find(line_conf.START_GOTO) + len(line_conf.START_GOTO)
        end_index = line.find(line_conf.END_GOTO)
        self.goto_name = line[start_index : end_index]
        super(GotoBlock, self).__init__(line)

    def get_title(self):
        return ""

    def get_content(self):
        return ""

    def operation(self, *args, **kwargs):
        return self.goto_name


class ChoiceItemBlock(BaseBlock):
    """单个选项"""
    def __init__(self, line):
        start_index = line.find(line_conf.START_CHOICE_ITEM) + len(line_conf.START_CHOICE_ITEM)
        end_index = line.find(line_conf.END_CHOICE_ITEM)
        content = line[start_index : end_index]
        split_content = content.split(line_conf.SPLIT_CHOICE_ITEM)
        if len(split_content) != 2:
            print("ERROR in choice item block. line = %s" %(line))
            return
        self.content = split_content[0]
        self.next_title = split_content[1]
        super(ChoiceItemBlock, self).__init__(line)


    def get_title(self):
        return ""


    def get_content(self):
        return self.content


    def operation(self, *args, **kwargs):
        return self.next_title


class ChoiceBlock(BaseBlock) :
    """选择块"""
    def __init__(self, line):
        self.item = []
        line = line[ : len(line) - 1]
        choice_items = line.split(line_conf.SPLIT_CHOICE)
        for item_line in choice_items:
            tmp_item = ChoiceItemBlock(item_line)
            self.item.append(tmp_item)
        super(ChoiceBlock, self).__init__(line)


    def get_title(self):
        titles = []
        for tmp_item in self.item:
            tmp_title = tmp_item.get_title()
            if tmp_title:
                titles.append(tmp_title)
        return "".join(titles)


    def get_content(self) :
        index = 1
        contents = []
        for tmp_item in self.item:
            tmp_content = tmp_item.get_content()
            if tmp_content:
                contents.append("[%d] %s" % (index, tmp_content))
                index += 1
        return "".join(contents)


    def operation(self, *args, **kwargs):
        select_index = args[0]
        if select_index < len(self.item):
            tmp_item = self.item[select_index]
            return tmp_item.operation(*args, **kwargs)

        return None



class StoryBlock(BaseBlock):
    """故事块"""
    def __init__(self, lines):
        self.inner_block = []

        for line in lines:
            tmp_block = None
            if line.startswith(line_conf.START_TITLE):
                tmp_block = TitleBlock(line)
            elif line.startswith(line_conf.START_GOTO):
                tmp_block = GotoBlock(line)
            elif line.startswith(line_conf.START_CHOICE_ITEM):
                tmp_block = ChoiceItemBlock(line)
            else:
                tmp_block = ContentBlock(line)

            self.inner_block.append(tmp_block)

        super(StoryBlock, self).__init__("")


    def get_title(self):
        titles = []
        for tmp_block in self.inner_block:
            tmp_title = tmp_block.get_title()
            if tmp_title:
                titles.append(tmp_title)

        return "".join(titles)


    def get_content(self):
        contents = []
        for tmp_block in self.inner_block:
            contents.append(tmp_block.get_content())
        return "".join(contents)


    def operation(self, *args, **kwargs):
        rtn = None
        for tmp_block in self.inner_block:
            tmp_rtn = tmp_block.operation(*args, **kwargs)
            if tmp_rtn :
                rtn = tmp_rtn
        return rtn

if __name__ == '__main__':
    pass