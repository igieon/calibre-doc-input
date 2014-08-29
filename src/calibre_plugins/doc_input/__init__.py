#!/usr/bin/env python
# vim:fileencoding=utf-8
from calibre.ptempfile import PersistentTemporaryDirectory
import os
from subprocess import check_call

__license__ = 'GPL v3'
__copyright__ = '2013, David Ignjic <ignjic at gmail.com>'


from calibre.customize.conversion import InputFormatPlugin, OptionRecommendation

from calibre.customize.builtins import plugins
     
class DOCInput(InputFormatPlugin):

    name = 'DOC Input'
    author = 'David Ignjic'
    description = _('Convert DOC files via docx to HTML')
    supported_platforms = ['windows']
    file_types = {'doc'}
    minimum_calibre_version = (1, 15, 0)
    version = (1, 0, 1)

    options = {
        OptionRecommendation(name='wordconv_exe_path', recommended_value='c:\Program Files\Microsoft Office\Office12\Wordconv.exe', 
            help=_('Path where is Wordconv.exe. Usually it is in "c:\Program Files\Microsoft Office\Office12\Wordconv.exe". If you don\'t have it you could download see http://www.microsoft.com/en-us/download/details.aspx?id=3 ')),
        OptionRecommendation(name='docx_no_cover', recommended_value=False,
            help=_('Normally, if a large image is present at the start of the document that looks like a cover, '
                   'it will be removed from the document and used as the cover for created ebook. This option '
                   'turns off that behavior.')),

    }

    recommendations = set([('page_breaks_before', '/', OptionRecommendation.MED)])

    def gui_configuration_widget(self, parent, get_option_by_name,
        get_option_help, db, book_id=None):
        from calibre_plugins.doc_input.doc_input import PluginWidget
        return PluginWidget(parent, get_option_by_name, get_option_help, db, book_id)

    def convert(self, stream, options, file_ext, log, accelerators):
        from calibre.ebooks.docx.to_html import Convert
        doc_temp_directory = PersistentTemporaryDirectory('doc_input')
        log.debug('Convert doc ' + stream.name + ' to docx via ' + options.wordconv_exe_path)
        
        docx_file = os.path.join(doc_temp_directory,os.path.basename( stream.name)+".docx")  
        log.debug('Temp directory '+ doc_temp_directory + ' temp output file'+docx_file)
        stream.close()
        if  not os.path.exists(options.wordconv_exe_path):
            raise ValueError('Not found ' + options.wordconv_exe_path)

        check_call([options.wordconv_exe_path,"-oice","-nme",stream.name,docx_file])        
        if  not os.path.exists(docx_file):
            raise ValueError('Not converted ' + docx_file)
        
        return Convert(docx_file, detect_cover=not options.docx_no_cover, log=log)()

