#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-{{cookiecutter.tool_name}} model implementation
"""

from __future__ import print_function, division, absolute_import

from Qt.QtCore import QObject


class {{cookiecutter.tool_class}}Model(QObject):
    def __init__(self):
        super({{cookiecutter.tool_class}}Model, self).__init__()
