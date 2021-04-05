#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains view implementation for tpRigToolkit-tools-{{cookiecutter.tool_name}}
"""

from __future__ import print_function, division, absolute_import

from tpDcc.libs.qt.core import base


class {{cookiecutter.tool_class}}View(base.BaseWidget):
    def __init__(self, model, controller, parent=None):

        self._model = model
        self._controller = controller

        super({{cookiecutter.tool_class}}View, self).__init__(parent=parent)

        self.refresh()

    # =================================================================================================================
    # OVERRIDES
    # =================================================================================================================

    def ui(self):
        super({{cookiecutter.tool_class}}View, self).ui()

    # =================================================================================================================
    # BASE
    # =================================================================================================================

    def refresh(self):
        pass
