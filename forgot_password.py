import re
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
from PyQt5 import QtCore, QtWidgets
from pizza_full_database import Customer_Database

class Ui_forgetmypassword(object):
    def setupUi(self, MainWindow):
        self.data_password_update=Customer_Database()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 467)
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 700, 406))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ner_password_2_line = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ner_password_2_line.setObjectName("ner_password_2_line")
        self.gridLayout_2.addWidget(self.ner_password_2_line, 4, 0, 1, 1)
        self.input_personal_number = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.input_personal_number.setObjectName("input_personal_number")
        self.gridLayout_2.addWidget(self.input_personal_number, 1, 1, 1, 1)
        self.personal_number_line = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.personal_number_line.setObjectName("personal_number_line")
        self.gridLayout_2.addWidget(self.personal_number_line, 1, 0, 1, 1)
        self.e_mail_number_line = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.e_mail_number_line.setObjectName("e_mail_number_line")
        self.gridLayout_2.addWidget(self.e_mail_number_line, 2, 0, 1, 1)
        self.input_new_password_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.input_new_password_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_new_password_1.setObjectName("input_new_password_1")
        self.gridLayout_2.addWidget(self.input_new_password_1, 3, 1, 1, 1)
        self.input_e_mail_number = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.input_e_mail_number.setObjectName("input_e_mail_number")
        self.gridLayout_2.addWidget(self.input_e_mail_number, 2, 1, 1, 1)
        self.input_new_password_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.input_new_password_2.setObjectName("input_new_password_2")
        self.input_new_password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout_2.addWidget(self.input_new_password_2, 4, 1, 1, 1)
        self.new_password_1_line = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.new_password_1_line.setObjectName("new_password_1_line")
        self.gridLayout_2.addWidget(self.new_password_1_line, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 1, 1, 1)
        self.update_password_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.update_password_button.setObjectName("update_password_button")
        self.gridLayout_2.addWidget(self.update_password_button, 6, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.update_password_button.clicked.connect(lambda : self.update_password_database(MainWindow))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_password_database(self,Mainwindow):
        if(type(self.new_password_control())==bool):
            self.succes_message_box(Mainwindow)
            self.data_password_update.update_password(self.input_new_password_1.text(),self.input_personal_number.text(),self.input_e_mail_number.text())
            from start import Ui_startWindow
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_startWindow()
            self.ui.setupUi(self.window)
            Mainwindow.hide()
            self.window.show()
       
        else:
            self.message_box_check_all_find(self.new_password_control(),Mainwindow)



    def message_box_check_all_find(self,error,MainWindow):
        dialog=QMessageBox(MainWindow)
        dialog.setText(error)
        dialog.setWindowTitle("error")
        dialog.exec_()

    def succes_message_box(self,MainWindow):
        dialog=QMessageBox(MainWindow)
        dialog.setText("succesfull change password")
        dialog.setWindowTitle("Succesful action!")
        dialog.exec_()



    def new_password_control(self):        
        if (self.data_password_update.forget_password_check_func(self.input_personal_number.text(),self.input_e_mail_number.text())!=None):
            if(self.input_new_password_1.text()==self.input_new_password_2.text()):
                password = self.input_new_password_1.text()
                for check in ["\d", "[A-Z]", "[a-z]", "\W"]:
                    if re.findall(r""+check,password):
                        continue
                    else:
                        values = {"\d":"Numbers","[A-Z]":"Upper cases","[a-z]":"Lower cases","\W":"special characters"}
                        return f"Weak password, must contain {values[check]}!"
                return True
            else:
                return "Passwords are not equal"
        else:
            return "User not found!"

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ner_password_2_line.setText(_translate("MainWindow", "Repeat password : "))
        self.personal_number_line.setText(_translate("MainWindow", "Personal id : "))
        self.e_mail_number_line.setText(_translate("MainWindow", "E-mail : "))
        self.new_password_1_line.setText(_translate("MainWindow", "New Password : "))
        self.update_password_button.setText(_translate("MainWindow", "Update Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_forgetmypassword()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
