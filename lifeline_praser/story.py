#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file: story.py
@date: 2018/10/10
@author: yujiasheng
"""

import line_conf
import story_block



class Story(object):
    ''''''
    def __init__(self):
        pass

    def read_story(self, file_name) :
        '''读取故事'''
        self.story_block = {}
        self.param = {}
        self.file_name = file_name
        file = open(self.file_name, "r")

        if not file :
            print("Can not open the file %s" %(file_name))
            return

        # 读取每一行
        line = file.readline()
        lines = []
        while line:
            if line[0 : 2] == line_conf.START_COMMENT: #注释行
                print("commnet is %s" %(line))
            elif line == line_conf.EMPTY_LINE :
                if lines:
                    tmp_story_block = story_block.StoryBlock(lines)
                    self.story_block[tmp_story_block.get_title()] = tmp_story_block
                lines = []
            else:
                lines.append(line)
                
            line = file.readline()

if __name__ == '__main__':
    pass