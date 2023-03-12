import sys
from pizza_full_database import incoming_pizza_order_database 
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Uİ_pizza_sepet(object):
    def setupUi(self, MainWindow):
        self.all_pizza_order=incoming_pizza_order_database().all_cart_pizza()
        self.delete_selected_pizza=incoming_pizza_order_database()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 825)
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.button_scrollbar = QtWidgets.QScrollArea(self.centralwidget)
        self.button_scrollbar.setWidgetResizable(True)
        self.button_scrollbar.setObjectName("button_scrollbar")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1025, 764))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.order_scroll_bar = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.order_scroll_bar.setWidgetResizable(True)
        self.order_scroll_bar.setObjectName("order_scroll_bar")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1005, 715))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.all_line_edit_list=[]
        self.all_check_box_list=[]
        total = 0

        with open("currentcustomer.txt","r") as file:
            personal_numb = file.readline()
        
        with open("currentcustomer.txt","w") as file:
                file.write(f"{personal_numb}\n")
        order_details = ""
        for index,i in enumerate(self.all_pizza_order):
            pizza_name = i[1].split("-")[0]
            pizza_cost = float(i[1].split("-")[1])
            first = 0
            components_names=""
            components_prices = ""
            components_names +=" ".join(i[2].split("-")[::3])
            components_prices = sum(list(map(float,i[2].split("-")[1::3])))
            cost_sum = components_prices + pizza_cost
            
            total += cost_sum
            if not components_names:
                components_names = "None"

        
            
            order_details += (pizza_name+", addiation: "+components_names)+f"     {round(cost_sum,2)}$"


            new_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
            font = QtGui.QFont()
            font.setPointSize(20)
            new_line_edit.setFont(font)
            new_line_edit.setObjectName(pizza_name+"order_intel_line")
            new_line_edit.setText((pizza_name+", addiation: "+components_names)+f"     {round(cost_sum,2)}$")
            new_line_edit.setReadOnly(True)
            
            self.gridLayout_3.addWidget(new_line_edit, index, 0, 1, 1)
            new_check_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
            font = QtGui.QFont()
            font.setPointSize(20)
            new_check_box.setFont(font)
            new_check_box.setObjectName("select1_check_box")
            self.gridLayout_3.addWidget(new_check_box, index, 1, 1, 1)
            new_check_box.setText(_translate("MainWindow","select"))
            self.all_check_box_list.append(new_check_box)
        
       
        
        self.order_scroll_bar.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.order_scroll_bar, 1, 0, 1, 6)
        self.seçilipizzayisatinal = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.seçilipizzayisatinal.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.seçilipizzayisatinal, 2, 4, 1, 2)
        self.secilipizzayisil = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.secilipizzayisil.setObjectName("secilipizzayisil")
        self.gridLayout_2.addWidget(self.secilipizzayisil, 2, 2, 1, 2)
        self.pizzasecmeyeri = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pizzasecmeyeri.setObjectName("pizzasecmeyeri")
        self.gridLayout_2.addWidget(self.pizzasecmeyeri, 2, 0, 1, 2)
        self.button_scrollbar.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.button_scrollbar, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.secilipizzayisil.clicked.connect(lambda: self.select_delete_pizza(MainWindow))

        self.seçilipizzayisatinal.clicked.connect(lambda : self.card_puchase_open_window(MainWindow,order_details,total)) 

        self.pizzasecmeyeri.clicked.connect(lambda : self.back_select_pizza(MainWindow))
        

    def back_select_pizza(self,Mainwindow):
        from pizza_order import Ui_siparis_window
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_siparis_window()
        self.ui.setupUi(self.window)
        Mainwindow.hide()
        self.window.show()


    def card_puchase_open_window(self,Mainwindow,order_details,total):
        from card_purchase import Ui_CardPurchasewindow
        if order_details:
            with open("currentcustomer.txt","a") as file:
                file.write(order_details)

            with open("currentcustomer.txt","a") as file:
                file.write("\n")
                file.write(f"{total}")
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_CardPurchasewindow()
            self.ui.setupUi(self.window)
            Mainwindow.hide()
            self.window.show()
        else:
            self.message_box_check_all_find("Cart is Empty!",Mainwindow)
        
    def message_box_check_all_find(self,error,MainWindow):
        dialog=QMessageBox(MainWindow)
        dialog.setText(error)
        dialog.setWindowTitle("error")
        dialog.exec_()


    def select_delete_pizza(self,Mainwindow):
        orders = self.all_pizza_order
        for index,i in enumerate(self.all_check_box_list):
            if(i.isChecked()):
                self.delete_selected_pizza.delete_cart(orders[index][0])

        self.window=QtWidgets.QMainWindow()
        self.uin=Uİ_pizza_sepet()
        self.uin.setupUi(self.window)
        Mainwindow.hide()
        self.window.show()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cart Menu"))
        self.seçilipizzayisatinal.setText(_translate("MainWindow", "Purchase the cart"))
        self.secilipizzayisil.setText(_translate("MainWindow", "Delete selected orders"))
        self.pizzasecmeyeri.setText(_translate("MainWindow", "Back to select order"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Uİ_pizza_sepet()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
