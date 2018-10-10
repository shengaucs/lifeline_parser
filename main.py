#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file: main.py
@date: 2018/10/10
@author: yujiasheng
"""

import lifeline_praser.story


if __name__ == '__main__':
    filename = './StoryData.txt'
    story_praser = lifeline_praser.story.Story()
    story_praser.read_story(filename)
    pass