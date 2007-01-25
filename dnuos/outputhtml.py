#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
# This program is under GPL license. See COPYING file for details.
#
# Copyright 2006
# Mattias Päivärinta <pejve@vasteras2.net>
#
# Authors
# Mattias Päivärinta <pejve@vasteras2.net>

"""
Module for rendering HTML output.
"""


import outputplain


class Renderer(object):
    def __init__(self):
        self.renderer = outputplain.Renderer()

    def __set_format_string(self, format_string):
        self.renderer.format_string = format_string
    format_string = property(fset=__set_format_string)

    def __set_columns(self, columns):
        self.renderer.columns = columns
    columns = property(fset=__set_columns)

    def render(self, dirs, options, data):
        """Render directories as HTML to stdout.

        Directories are rendered like in plain text, but with HTML header
        and footer.
        """
        yield """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Music List</title>
<!-- Generated by dnuos %s -->
<!-- http://aiiie.net/projects/dnuos -->
<style type="text/css"><!--
body { color: %s; background: %s; }
-->
</style>
</head>
<body>
<pre>""" % (data.version['dnuos'], options.text_color, options.bg_color)

        for chunk in self.renderer.render(dirs, options, data):
            yield chunk

        yield "</pre>"
        yield "</body></html>"
