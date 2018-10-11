#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file: line_conf.py
@date: 2018/10/10
@author: yujiasheng
"""

EMPTY_LINE        = "\n"

START_COMMENT     = "//"
START_BLOCK        = ":: "
START_TITLE        = ":: "


START_SILENTLY    = "<<silently>>"
END_SILENTLY      = "<<endsilently>>"

START_SET_VAR   = "<<set "
END_SET_VAR     = ">>"
SPLIT_SET_VAR   = " = "

START_GOTO        = "[["
END_GOTO          = "]]"

START_CHOICE      = "<<choice "
END_CHOICE        = ">>"
SPLIT_CHOICE      = " | "
START_CHOICE_ITEM = "[["
END_CHOICE_ITEM   = "]]"
SPLIT_CHOICE_ITEM = "|"


START_SELECT      = "<<if"
END_SELECT        = "<<endif>>"
START_SELECT_ITEM = ""
END_SELECT_ITEM   = ">>"




if __name__ == '__main__':
    pass