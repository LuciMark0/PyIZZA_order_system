import re
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
from PyQt5 import QtCore, QtWidgets
from validator_collection import validators
from pizza_full_database import Customer_Database

class Ui_register_window(object):
    def setupUi(self, MainWindow):
        self.database_addiation=Customer_Database()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 301)
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 546, 240))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.password_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.password_label.setObjectName("password_label")
        self.gridLayout_2.addWidget(self.password_label, 3, 0, 1, 1)
        self.input_email_line = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.input_email_line.setObjectName("input_email_line")
        self.gridLayout_2.addWidget(self.input_email_line, 4, 1, 1, 1)
        self.input_password_line = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.input_password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password_line.setObjectName("input_password_line")
        self.gridLayout_2.addWidget(self.input_password_line, 3, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.name_label.setObjectName("name_label")
        self.gridLayout_2.addWidget(self.name_label, 2, 0, 1, 1)
        self.input_personal_number_line = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.input_personal_number_line.setObjectName("input_personal_number_line")
        self.gridLayout_2.addWidget(self.input_personal_number_line, 1, 1, 1, 1)
        self.email_password = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.email_password.setObjectName("email_password")
        self.gridLayout_2.addWidget(self.email_password, 4, 0, 1, 1)
        self.personalnumber_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.personalnumber_label.setObjectName("personalnumber_label")
        self.gridLayout_2.addWidget(self.personalnumber_label, 1, 0, 1, 1)
        self.input_name_line = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.input_name_line.setObjectName("input_name_line")
        self.gridLayout_2.addWidget(self.input_name_line, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.new_register_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.new_register_button.setObjectName("new_register_button")
        self.gridLayout_2.addWidget(self.new_register_button, 6, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.new_register_button.clicked.connect(lambda : self.add_data_base_control(MainWindow))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Register Menu"))
        self.password_label.setText(_translate("MainWindow", "Password : "))
        self.name_label.setText(_translate("MainWindow", "Name : "))
        self.email_password.setText(_translate("MainWindow", "E_mail : "))
        self.personalnumber_label.setText(_translate("MainWindow", "Personal id : "))
        self.new_register_button.setText(_translate("MainWindow", "Sign-up"))
    def add_data_base_control(self,Mainwindow):
        self.a_signup=self.sign_up()
        if(type(self.a_signup)==bool):
            self.message_box_succesfull()
            self.database_addiation.insert_customer(self.input_personal_number_line.text(),self.input_name_line.text(),self.input_password_line.text(),self.input_email_line.text())
            from start import Ui_startWindow
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_startWindow()
            self.ui.setupUi(self.window)
            Mainwindow.hide()
            self.window.show()
        else:
            self.message_box_wrong_password(self.a_signup)

    def message_box_wrong_password(self,error):
        dialog=QMessageBox()
        dialog.setText(error)
        dialog.setWindowTitle("Invalid Input")
        dialog.exec_()
    def message_box_succesfull(self):
        dialog=QMessageBox()
        dialog.setText("your register is succesfull")
        dialog.setWindowTitle("succesfull")
        dialog.exec_()

    def sign_up(self):
        errors=""
        while True:
            name = self.input_name_line.text()
            if re.search(r"^[a-zA-Z,ş,ö,ç,ı,ğ,ü,Ş,Ö,Ç,İ,Ğ,Ü,\s]+$",name):
                pass
            else:
                errors+= "Invalid Name!\n"
                
            personal_id = self.input_personal_number_line.text()

            if re.search(r"^\d{11}$",personal_id):
                if (self.database_addiation.personal_number_checked(personal_id)==None):
                    pass
                else:
                    errors+="Invalid Personal ID already exist!\n"
            else:
                errors+="Invalid Personal ID!\n"

            email = self.input_email_line.text()
            try:
                email_address = validators.email(email, allow_empty = True)
                if not email_address == None:
                    pass
                else:
                    errors+= "Invalid e-mail\n"
            except:
                errors+= "Invalid e-mail\n"
            
            password = self.input_password_line.text()
            for check in ["\d", "[A-Z]", "[a-z]", "\W"]:
                if re.findall(r""+check,password):
                    continue
                else:
                    values = {"\d":"Numbers","[A-Z]":"Upper cases","[a-z]":"Lower cases","\W":"special characters"}
                    errors+= f"Weak password, must contain {values[check]}!"
                    break
            if(errors==""):
                return True
            else:
                return errors
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_register_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
