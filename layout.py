from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtWidgets import (QApplication, QGridLayout, QGroupBox,
                             QLabel, QLineEdit, QWidget, QDialogButtonBox)
# from setting import rev1, rev2, rev3, mode1, mode2, mode3


class Window(QWidget):


    def __init__(self):
        super(Window, self).__init__()
        self.settings = QSettings("setting.conf", QSettings.IniFormat)
        rev1 = self.settings.value('label/rev1','')
        rev2 = self.settings.value('label/rev2', '')
        rev3 = self.settings.value('label/rev3', '')

        mode1 = self.settings.value('label/mode1','')
        mode2 = self.settings.value('label/mode2', '')
        mode3 = self.settings.value('label/mode3', '')

        label1Group = QGroupBox("标签1")
        label1_rev = QLabel("REV")
        self.rev1LineEdit = QLineEdit()
        '''self.rev1LineEdit.setFocus()'''
        label1_mode = QLabel("MODE")
        self.mode1LineEdit = QLineEdit()
        self.rev1LineEdit.insert(rev1)
        self.mode1LineEdit.insert(mode1)

        label2Group = QGroupBox("标签2")
        label2_rev = QLabel("REV")
        self.rev2LineEdit = QLineEdit()
        label2_mode = QLabel("MODE")
        self.mode2LineEdit = QLineEdit()
        self.rev2LineEdit.insert(rev2)
        self.mode2LineEdit.insert(mode2)

        label3Group = QGroupBox("标签3")
        label3_rev = QLabel("REV")
        self.rev3LineEdit = QLineEdit()
        label3_mode = QLabel("MODE")
        self.mode3LineEdit = QLineEdit()
        self.rev3LineEdit.insert(rev3)
        self.mode3LineEdit.insert(mode3)


        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        label1Layout = QGridLayout()
        label1Layout.addWidget(label1_rev, 0, 0)
        label1Layout.addWidget(self.rev1LineEdit, 0, 1)
        label1Layout.addWidget(label1_mode, 1, 0)
        label1Layout.addWidget(self.mode1LineEdit, 1, 1)
        label1Group.setLayout(label1Layout)

        label2Layout = QGridLayout()
        label2Layout.addWidget(label2_rev, 0, 0)
        label2Layout.addWidget(self.rev2LineEdit, 0, 1)
        label2Layout.addWidget(label2_mode, 1, 0)
        label2Layout.addWidget(self.mode2LineEdit, 1, 1)
        label2Group.setLayout(label2Layout)

        label3Layout = QGridLayout()
        label3Layout.addWidget(label3_rev, 0, 0)
        label3Layout.addWidget(self.rev3LineEdit, 0, 1)
        label3Layout.addWidget(label3_mode, 1, 0)
        label3Layout.addWidget(self.mode3LineEdit, 1, 1)
        label3Group.setLayout(label3Layout)

        layout = QGridLayout()
        layout.addWidget(label1Group, 0, 0)
        layout.addWidget(label2Group, 0, 1)
        layout.addWidget(label3Group, 1, 0)
        layout.addWidget(buttonBox, 2, 1)
        ''' layout.addWidget(buttonlayout, 1,1) '''
        self.setLayout(layout)

        self.setWindowTitle("label format setting")

        buttonBox.accepted.connect(self.foo)
        buttonBox.rejected.connect(self.bar)

    def foo(self):
        self.settings.setValue("label/rev1", self.rev1LineEdit.text())
        self.settings.setValue("label/rev2", self.rev2LineEdit.text())
        self.settings.setValue("label/rev3", self.rev3LineEdit.text())



    def bar(self):
        print("bar")



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
