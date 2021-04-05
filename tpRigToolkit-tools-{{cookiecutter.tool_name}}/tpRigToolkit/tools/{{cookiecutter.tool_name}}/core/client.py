#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-{{cookiecutter.tool_name}} client implementation
"""

from tpDcc.core import client


class {{cookiecutter.tool_class}}Client(client.DccClient, object):

    PORT = {{cookiecutter.client_port}}
