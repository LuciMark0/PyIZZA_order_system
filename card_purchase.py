import re
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from pizza_full_database import add_credi_card
from receipt import Ui_Receiptwindow
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget

class Ui_CardPurchasewindow(object):
    def setupUi(self, MainWindow):
        self.addcredicard=add_credi_card()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 250)
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cvv_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cvv_label.setFont(font)
        self.cvv_label.setObjectName("cvv_label")
        self.gridLayout_2.addWidget(self.cvv_label, 0, 0, 1, 1)
        self.cvv_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cvv_line_edit.setFont(font)
        self.cvv_line_edit.setObjectName("cvv_line_edit")
        self.gridLayout_2.addWidget(self.cvv_line_edit, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 2, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.card_no_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.card_no_line_edit.setFont(font)
        self.card_no_line_edit.setObjectName("card_no_line_edit")
        self.gridLayout.addWidget(self.card_no_line_edit, 0, 2, 1, 1)
        self.cord_no_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cord_no_label.setFont(font)
        self.cord_no_label.setObjectName("cord_no_label")
        self.gridLayout.addWidget(self.cord_no_label, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.gridLayout_3.addWidget(self.date_label, 0, 1, 1, 1)
        self.day_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.day_spinbox.setFont(font)
        self.day_spinbox.setMinimum(1)
        self.day_spinbox.setMaximum(12)
        self.day_spinbox.setObjectName("day_spinbox")
        self.gridLayout_3.addWidget(self.day_spinbox, 0, 2, 1, 1)
        self.year_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.year_spinBox.setFont(font)
        self.year_spinBox.setMinimum(23)
        self.year_spinBox.setMaximum(50)
        self.year_spinBox.setProperty("value", 23)
        self.year_spinBox.setObjectName("year_spinBox")
        self.gridLayout_3.addWidget(self.year_spinBox, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 1, 0, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout_4)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.back_to_card_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.back_to_card_button.setFont(font)
        self.back_to_card_button.setObjectName("back_to_card_button")
        self.gridLayout_5.addWidget(self.back_to_card_button, 0, 0, 1, 1)
        self.confirm_purchase_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.confirm_purchase_button.setFont(font)
        self.confirm_purchase_button.setObjectName("confirm_purchase_button")
        self.gridLayout_5.addWidget(self.confirm_purchase_button, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 1, 1, 1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.gridLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 462, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.credi_card_show_window()
        self.confirm_purchase_button.clicked.connect(lambda: self.credi_card_control(MainWindow))
        self.back_to_card_button.clicked.connect(lambda: self.back_to_cart(MainWindow))

    def credi_card_show_window(self):
        with open("currentcustomer.txt","r") as file:
            personal_numb =file.readline()
        if (self.addcredicard.check_creditcard(personal_numb)!=None):
            a,card_no,card_date,d=self.addcredicard.check_creditcard(personal_numb)
            month,year=card_date.split("/")

            self.card_no_line_edit.setText(card_no)
            self.day_spinbox.setValue(int(month))
            self.year_spinBox.setValue(int(year))


    def back_to_cart(self,Mainwindow):
        from pizza_cart import Uİ_pizza_sepet
        self.window=QtWidgets.QMainWindow()
        self.ui=Uİ_pizza_sepet()
        self.ui.setupUi(self.window)
        Mainwindow.hide()
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Card Verify Menu"))
        self.cvv_label.setText(_translate("MainWindow", "cvv :"))
        self.cord_no_label.setText(_translate("MainWindow", "card no :"))
        self.date_label.setText(_translate("MainWindow", "date :"))
        self.back_to_card_button.setText(_translate("MainWindow", "back to cart"))
        self.confirm_purchase_button.setText(_translate("MainWindow", "confirm purchase"))

    def purchase_check(self):
        credit_card_no = self.card_no_line_edit.text()
        if re.search(r"^\d{16}$", credit_card_no):
            pass
        else:
            return False
        
        cvv = self.cvv_line_edit.text()
        if re.search(r"^\d{3}$", cvv):
            pass
        else:
            return False

        card_month = self.day_spinbox.value()
        card_year = self.year_spinBox.value()
        self.card_date = f"{card_month}/{card_year}"
        self.today = datetime.now()
        
        if int(str(self.today.year)[-2:]) < card_year or (int(str(self.today.year)[-2:]) == card_year and int(str(self.today.month)) <= card_month):
            pass
        else:
            return False

        return True
    
    def credi_card_message_box(self):
        dialog=QMessageBox()
        dialog.setText("Wrong credit card number, date or cvv!")
        dialog.setWindowTitle("invalid card information")
        dialog.exec_()
        
    def credi_card_control (self,Mainwindow):
        if (self.purchase_check()):
            with open("currentcustomer.txt","r") as file:
                personal_numb =file.readline()

            if(self.addcredicard.check_creditcard(personal_numb) == None):
                self.addcredicard.insert_credicard(personal_numb, self.card_no_line_edit.text(), self.card_date, self.cvv_line_edit.text())
                
                with open("currentcustomer.txt","a") as file:
                    file.write(f"\n{self.card_no_line_edit.text()}\n")
            else:
                self.addcredicard.update_credicard(personal_numb, self.card_no_line_edit.text(), self.card_date, self.cvv_line_edit.text())
                with open("currentcustomer.txt","a") as file:
                    file.write(f"\n{self.card_no_line_edit.text()}\n")

            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Receiptwindow()
            self.ui.setupUi(self.window)
            Mainwindow.hide()
            self.window.show()
        else:
            self.credi_card_message_box()
        
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CardPurchasewindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
