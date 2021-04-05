#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-{{cookiecutter.tool_name}} controller implementation
"""

from __future__ import print_function, division, absolute_import


class {{cookiecutter.tool_class}}Controller(object):
    def __init__(self, model, client):
        super({{cookiecutter.tool_class}}Controller, self).__init__()

        self._client = client
        self._model = model
