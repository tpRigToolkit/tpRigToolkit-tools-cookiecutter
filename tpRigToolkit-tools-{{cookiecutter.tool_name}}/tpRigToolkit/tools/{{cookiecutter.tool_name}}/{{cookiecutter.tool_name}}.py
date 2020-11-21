#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
{{cookiecutter.tool_description}}
"""

from __future__ import print_function, division, absolute_import

from tpDcc.core import tool
from tpDcc.libs.qt.widgets import toolset

# Defines ID of the tool
TOOL_ID = 'tpRigToolkit-tools-{{cookiecutter.tool_name}}'


class {{cookiecutter.tool_class}}Tool(tool.DccTool, object):
    def __init__(self, *args, **kwargs):
        super({{cookiecutter.tool_class}}Tool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = tool.DccTool.config_dict(file_name=file_name)
        tool_config = {
            'name': '{{cookiecutter.tool_nice_name}}',
            'id': TOOL_ID,
            'supported_dccs': {{cookiecutter.supported_dccs}},
            'icon': '{{cookiecutter.tool_icon}}',
            'tooltip': '{{cookiecutter.tool_description}}',
            'tags': {{cookiecutter.tool_tags}},
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': '{{cookiecutter.tool_nice_name}}', 'load_on_startup': False, 'color': '', 'background_color': ''},
        }
        base_tool_config.update(tool_config)

        return base_tool_config

    def launch(self, *args, **kwargs):
        return self.launch_frameless(*args, **kwargs)


class {{cookiecutter.tool_class}}Toolset(toolset.ToolsetWidget, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super({{cookiecutter.tool_class}}Toolset, self).__init__(*args, **kwargs)

    def contents(self):
        return []
