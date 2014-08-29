# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc_input.ui'
#
# Created: Sat Dec 14 13:31:59 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

try:
    from PyQt5 import Qt as QtGui
    from PyQt5 import QtCore
    from PyQt5.Qt import QFileDialog
except ImportError as e:
    from PyQt4 import QtCore, QtGui
    from PyQt4.Qt import QFileDialog

from calibre.gui2 import SanitizeLibraryPath
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(518, 353)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.opt_wordconv_exe_path = QtGui.QLineEdit(Form)
        self.opt_wordconv_exe_path.setObjectName(_fromUtf8("opt_wordconv_exe_path"))
        self.hboxlayout.addWidget(self.opt_wordconv_exe_path)
        self.fileChoose = QtGui.QPushButton(Form)
        self.fileChoose.setObjectName(_fromUtf8("fileChoose"))
        self.fileChoose.clicked.connect(self.fileSearch)
        self.hboxlayout.addWidget(self.fileChoose)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.opt_docx_no_cover = QtGui.QCheckBox(Form)
        self.opt_docx_no_cover.setObjectName(_fromUtf8("opt_docx_no_cover"))
        self.verticalLayout.addWidget(self.opt_docx_no_cover)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def fileSearch(self):
        use_native_dialog = 'CALIBRE_NO_NATIVE_FILEDIALOGS' not in os.environ
        filterString = 'wordconv.exe (wordconv.exe)'

        with SanitizeLibraryPath():
            opts = QFileDialog.Option()
            if not use_native_dialog:
                opts |= QFileDialog.DontUseNativeDialog
            selectedFile = QFileDialog.getOpenFileName(parent=self, caption=_('Find wordconv.exe'),directory = self.opt_wordconv_exe_path.text(),filter = filterString,options=opts)
            if selectedFile:
                selectedFile = selectedFile[0] if isinstance(selectedFile, tuple) else selectedFile
                if selectedFile and os.path.exists(selectedFile):
                    self.opt_wordconv_exe_path.setText(selectedFile)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p>Microsoft conversion program Wordconv.exe.Usually is placed in &quot;c:\\Program Files (x86)\\Microsoft Office\\Office12\\Wordconv.exe&quot;. You can dowload from <a href=\"http://www.microsoft.com/en-us/download/details.aspx?id=3\"><span style=\" text-decoration: underline; color:#0000ff;\">microsoft page.</span></a></p></body></html>", None))
        self.fileChoose.setText(_translate("Form", "...", None))
        self.opt_docx_no_cover.setText(_translate("Form", "Do not try to autodetect a &cover from images in the document", None))

