#!/usr/bin/env python
# vim:fileencoding=utf-8
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__ = 'GPL v3'
__copyright__ = '2013, Kovid Goyal <kovid at kovidgoyal.net>'

from calibre_plugins.doc_input.doc_input_ui import Ui_Form
from calibre.gui2.convert import Widget
from calibre.gui2.preferences.conversion import InputOptions as BaseInputOptions

class PluginWidget(Widget, Ui_Form):

    TITLE = _('DOC Input')
    COMMIT_NAME = 'doc_input'
    ICON = I('mimetypes/docx.png')
    HELP = _('Options specific to the input format.')

    def __init__(self, parent, get_option, get_help, db=None, book_id=None):
        import traceback
        traceback.print_stack()
        Widget.__init__(self, parent,
            ['docx_no_cover', 'wordconv_exe_path'])
        self.initialize_options(get_option, get_help, db, book_id)
