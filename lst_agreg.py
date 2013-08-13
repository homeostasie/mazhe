#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools
import plugins_agreg

myRequest = LaTeXparser.PytexTools.Request("mesure")
myRequest.medicament_plugin=plugins_agreg.accept_all_input
myRequest.plugin_list=[plugins_agreg.set_isAgreg,plugins_agreg.remove_parts]
myRequest.original_filename="mes_notes.tex"
