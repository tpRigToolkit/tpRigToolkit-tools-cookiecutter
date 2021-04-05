#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains toolset implementation for tpRigToolkit-tools-{{cookiecutter.tool_name}}
"""

from __future__ import print_function, division, absolute_import


from tpDcc.libs.qt.widgets import toolset

from tpRigToolkit.tools.{{cookiecutter.tool_name}}.core import model, view, controller


class {{cookiecutter.tool_class}}Toolset(toolset.ToolsetWidget, object):
    def __init__(self, *args, **kwargs):
        super({{cookiecutter.tool_class}}Toolset, self).__init__(*args, **kwargs)

    def contents(self):
        tool_model = model.{{cookiecutter.tool_class}}Model()
        tool_controller = controller.{{cookiecutter.tool_class}}Controller(model=tool_model, client=self.client)
        tool_view = view.{{cookiecutter.tool_class}}View(model=tool_model, controller=tool_controller, parent=self)

        return [tool_view]
