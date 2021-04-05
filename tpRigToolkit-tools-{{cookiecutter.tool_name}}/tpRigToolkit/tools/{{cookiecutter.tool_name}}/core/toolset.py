#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains toolset implementation for tpRigToolkit-tools-{{cookiecutter.tool_name}}
"""

from __future__ import print_function, division, absolute_import


from tpDcc.libs.qt.widgets import toolset


class {{cookiecutter.tool_class}}Toolset(toolset.ToolsetWidget, object):
    def __init__(self, *args, **kwargs):
        super({{cookiecutter.tool_class}}Toolset, self).__init__(*args, **kwargs)

    def contents(self):
        return []
