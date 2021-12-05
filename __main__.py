# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Pictures\Projects\Python\epam_progects\Enigma\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#

import os
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from enigma_console import text_crypt, com_k, show_st, Switch, key, com_key, rot_key

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 921, 691))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sourceTextBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.sourceTextBrowser.setReadOnly(False)
        self.sourceTextBrowser.setObjectName("sourceTextBrowser")
        self.verticalLayout.addWidget(self.sourceTextBrowser)
        self.readCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.readCheckBox.setObjectName("readCheckBox")
        self.verticalLayout.addWidget(self.readCheckBox)
        self.outputTextBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.outputTextBrowser.setReadOnly(False)
        self.outputTextBrowser.setObjectName("outputTextBrowser")
        self.verticalLayout.addWidget(self.outputTextBrowser)
        self.cryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.cryptButton.setGeometry(QtCore.QRect(940, 10, 91, 51))
        self.cryptButton.setObjectName("cryptButton")
        self.transcrButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.transcrButton_2.setGeometry(QtCore.QRect(940, 70, 91, 51))
        self.transcrButton_2.setObjectName("transcrButton_2")
        self.writeCheckBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.writeCheckBox_2.setGeometry(QtCore.QRect(10, 700, 921, 21))
        self.writeCheckBox_2.setObjectName("writeCheckBox_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(940, 250, 91, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(940, 350, 91, 111))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(940, 230, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(940, 310, 101, 41))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(940, 180, 89, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(940, 150, 51, 21))
        self.label.setObjectName("label")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(940, 480, 91, 23))
        self.saveButton.setObjectName("saveButton")
        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(940, 510, 91, 23))
        self.showButton.setObjectName("showButton")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(940, 540, 91, 21))
        self.generateButton.setObjectName("generateButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1044, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # *
        self.add_functions()
        # *

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Enigma", "Enigma"))
        self.sourceTextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Text or .txt file path</p></body></html>"))
        self.readCheckBox.setText(_translate("MainWindow", "Read from file"))
        self.outputTextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Crypted text output or path to .txt file</p></body></html>"))
        self.cryptButton.setText(_translate("MainWindow", "Crypt"))
        self.transcrButton_2.setText(_translate("MainWindow", "Transcrypt"))
        self.writeCheckBox_2.setText(_translate("MainWindow", "Save into file"))
        self.label_2.setText(_translate("MainWindow", "Key"))
        self.label_3.setText(_translate("MainWindow", "Letter replacements"))
        self.label.setText(_translate("MainWindow", "Rotors"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.showButton.setText(_translate("MainWindow", "Show"))
        self.generateButton.setText(_translate("MainWindow", "Generate"))

    # *
    def add_functions(self):
        self.cryptButton.clicked.connect(lambda :self.crypt_txt(transcr=False))
        self.transcrButton_2.clicked.connect(lambda :self.crypt_txt(transcr=True))
        self.showButton.clicked.connect(self.show)
        self.saveButton.clicked.connect(self.save)
        self.generateButton.clicked.connect(self.generate)


    def setup(self):
        '''Reads new key from key text fields so that
         it can be used for encryption/decryption.
         '''
        rot_key = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        com_key = self.textEdit_3.toPlainText()

        # parse rot_key
        if all([isinstance(rot_key, str), len(rot_key) == 3, rot_key.isdigit()]):
            rot_key = list(rot_key)
        else:
            self.error_message('Invalid rotor key')
            return
        # parse key
        if not all([isinstance(key, str), len(key) == 3, key.isalpha()]):
            self.error_message('Invalid key')
            return
        # parse com_key
        if com_key:
            com_key = com_key.split(' ')
            if all(
                map(
                    lambda x: (len(x) == 2 and x.isalpha), com_key
                )
            ):
                com_key = {symbs[0] : symbs[1] for symbs in com_key}
            else:
                self.error_message('Invalid  letter replacement')
                return
        else:
            com_key = {}

        return rot_key, key, com_key

    @classmethod
    def error_message(cls, text: str):
        '''Shows error message with given text.
        '''
        cls.error = QMessageBox()
        cls.error.setWindowTitle('Error')
        cls.error.setIcon(QMessageBox.Warning)
        cls.error.setStandardButtons(QMessageBox.Ok)
        cls.error.setText(text)
        cls.error.exec_()

    @classmethod
    def file(cls, path:str, flag:str, text:str = '') -> str:
        '''Reads from file if flag = 'r'.
         Writes into file if flag = 'w'

            First argument is a file path.
           If flag = 'w' the recorded text should be passed as an third argument
           '''
        try:
            if flag == 'r':
                if not os.path.exists(path):
                    return
                with open(path, 'r') as file:
                    text = ''
                    for line in file:
                        text += line
                return text

            elif flag == 'w':
                with open(path, 'w') as file:
                    file.write(text)
        except Exception as e:
            cls.error_message(f'Error: {e}')   # 1


    def crypt_txt(self, transcr = False):
        '''Crypts text using a given key and source.

        If transcr = True performs decryption.'''
        # setup
        global rot_key
        global key
        global com_key
        try:
            if all([self.textEdit.toPlainText(),
                       self.textEdit_2.toPlainText()]):
                print('setup')
                keys = self.setup()
                if keys:
                    rot_key, key, com_key = keys
                    print(keys)
                else:
                    return None

            # crypt
            text = self.sourceTextBrowser.toPlainText()
            if self.readCheckBox.isChecked():
                text = self.file(text, 'r')
            if text:
                cr_text = text_crypt(text, key, com_key, transcript=transcr)
                #print(key, com_key, rot_key)
            else:
                self.error_message('Empty field or file not found')
                return
            if self.writeCheckBox_2.isChecked():
                self.file(self.outputTextBrowser.toPlainText(), 'w', cr_text)
            else:
                self.outputTextBrowser.setText(cr_text)
        except Exception as e:
            self.error_message(f'Error: {e}')


    def show(self):
        '''Shows current key in the text fields.'''
        global rot_key
        global key
        global com_key

        rot_key_show = ''
        com_key_show = ''

        for i in rot_key:
            rot_key_show += i

        for i, j in com_key.items():
            com_key_show += i + j + ' '

        self.textEdit.setText(str(rot_key_show))
        self.textEdit_2.setText(key)
        self.textEdit_3.setText(str(com_key_show[:-1]))

    def save(self):
        '''Saves current key.'''
        global rot_key
        global key
        global com_key

        rot_key, key, com_key = self.setup()
        save = [rot_key, key, com_key]
        with open('enigma_data.pickle', 'wb') as f:
            pickle.dump(save, f)
        print('data saved')

    def generate(self):
        '''Generates random key.'''
        import random
        eng = list('abcdefghijklmnopqrstuvwxyz')
        rot_key = ''
        key = ''
        com_key = ''

        for i in range(3):
            rot_key += str(random.randint(1,6))
            key += random.choice(eng)
            com_key += eng.pop(random.randint(0, len(eng)-1)) + eng.pop(random.randint(0, len(eng)-1)) + ' '

        self.textEdit.setText(str(rot_key))
        self.textEdit_2.setText(key)
        self.textEdit_3.setText(str(com_key[:-1]))

    # *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
