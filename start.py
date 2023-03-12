from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
from pizza_full_database import Customer_Database, incoming_pizza_order_database


def main():
    import sys
    set_default_menu()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_startWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


def set_default_menu():
    from pizza_full_database import pizza_Database,addition_Metarial 

    pizza_db = pizza_Database()
    component_db = addition_Metarial()

    class Pizza():
        def __init__(self, name, description, cost) -> None:
            self._description = description
            self._cost = cost
            self._name = name
        
        def __str__(self) -> str:
            return self._name


        def get_description(self):
            return self._description
        

        def get_cost(self):
            return self._cost

    class Standart_Pizza(Pizza):
        def __init__(self, name, description, cost) -> None:
            super().__init__(name, description, cost)
        
    class Dominos_Pizza(Pizza):
        def __init__(self, name, description, cost) -> None:
            super().__init__(name, description, cost)
        
    class Margherita_Pizza(Pizza):
        def __init__(self, name, description, cost) -> None:
            super().__init__(name, description, cost)
            
    class Turkish_Pizza(Pizza):
        def __init__(self, name, description, cost) -> None:
            super().__init__(name, description, cost)

    class BBQ_Pizza(Pizza):
        def __init__(self, name, description, cost) -> None:
            super().__init__(name, description, cost)
        

    # Decorator Part----
    class Decorator(Pizza):
        def __init__(self, name, description, cost) -> None:
            super().__init__(name, description, cost)


    class Mushroom(Decorator):
        def __init__(self, name, description, cost) -> None:
            super().__init__(name, description, cost)

    class Sausage(Decorator):
        def __init__(self, name, description, cost) -> None:
            super().__init__(name, description, cost)

    class Olive(Decorator):
        def __init__(self, name, description, cost) -> None:
            super().__init__(name, description, cost)

    class Corn(Decorator):
        def __init__(self, name, description, cost) -> None:
            super().__init__(name, description, cost)

    class Nugget(Decorator):
        def __init__(self, name, description, cost) -> None:
            super().__init__(name, description, cost)


    pizzas = []
    pizzas.append(Standart_Pizza("Standart Pizza", "literally normal", "2.49"))
    pizzas.append(Margherita_Pizza("Margherita Pizza", "cheesy", "3.99"))
    pizzas.append(Dominos_Pizza("Dominos Pizza", "can be cause of domino effect", "4.99"))
    pizzas.append(Turkish_Pizza("Turkish Pizza", "Best Turkish kebab", "4.99"))
    pizzas.append(BBQ_Pizza("BBQ Pizza", "BBQ sauce with chicken nuggets", "4.99"))

    for pizza in pizzas:
        pizza_db.insert_pizza(str(pizza), pizza.get_cost(), pizza.get_description())


    components = []
    components.append(Mushroom("Mushroom", "it tastes like a meat", "0.30"))
    components.append(Sausage("Sausage", "%100 cow meat", "0.35"))
    components.append(Nugget("Nugget", "Chicken nuggets", "0.25"))
    components.append(Olive("Olive", "from the branch", "0.20"))
    components.append(Corn("Corn", "with the cob", "0.25"))

    for component in components:
        component_db.insert_addmade(str(component), component.get_cost(), component.get_description())
    
class Ui_startWindow(object):

    def setupUi(self, MainWindow):
        self.incoming_pizza_order=incoming_pizza_order_database()
        self.customerdatabasechecklogin=Customer_Database() 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 317)
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.newregisterbutton = QtWidgets.QPushButton(self.centralwidget)
        self.newregisterbutton.setObjectName("newregisterbutton")
        self.gridLayout.addWidget(self.newregisterbutton, 2, 0, 1, 1)
        self.paswordlabelnull = QtWidgets.QLabel(self.centralwidget)
        self.paswordlabelnull.setObjectName("paswordlabelnull")
        self.gridLayout.addWidget(self.paswordlabelnull, 1, 0, 1, 1)
        self.namelabelisnull = QtWidgets.QLabel(self.centralwidget)
        self.namelabelisnull.setObjectName("namelabelisnull")
        self.gridLayout.addWidget(self.namelabelisnull, 0, 0, 1, 1)
        self.forgetmypasswordbutton = QtWidgets.QPushButton(self.centralwidget)
        self.forgetmypasswordbutton.setObjectName("forgetmypasswordbutton")
        self.gridLayout.addWidget(self.forgetmypasswordbutton, 2, 1, 1, 1)
        self.inputpasswordlabel = QtWidgets.QLineEdit(self.centralwidget)
        self.inputpasswordlabel.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputpasswordlabel.setObjectName("inputpasswordlabel")
        self.gridLayout.addWidget(self.inputpasswordlabel, 1, 1, 1, 2)
        self.inputnamelabel = QtWidgets.QLineEdit(self.centralwidget)
        self.inputnamelabel.setObjectName("inputnamelabel")
        self.gridLayout.addWidget(self.inputnamelabel, 0, 1, 1, 2)
        self.loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loginbutton.setObjectName("loginbutton")
        self.gridLayout.addWidget(self.loginbutton, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.loginbutton.clicked.connect(lambda : self.check_login_reading(MainWindow))
        self.newregisterbutton.clicked.connect(lambda :self.new_register_open_window(MainWindow))
        self.forgetmypasswordbutton.clicked.connect(lambda: self.new_forget_my_password(MainWindow))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def new_register_open_window(self,Mainwindow):
        from register import Ui_register_window
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_register_window()
        self.ui.setupUi(self.window)
        Mainwindow.hide()
        self.window.show()

    def new_forget_my_password(self,Mainwindow):
        from forgot_password import Ui_forgetmypassword
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_forgetmypassword()
        self.ui.setupUi(self.window)
        Mainwindow.hide()
        self.window.show()


    def check_login_reading(self, MainWindow):
        try:
            if personal_numb:=self.customerdatabasechecklogin.check_login(self.inputnamelabel.text(),self.inputpasswordlabel.text()):
                with open("currentcustomer.txt","w") as file:
                    file.write(f"{personal_numb}")
                self.incoming_pizza_order.all_order_database_delete()
                self.order_open_window(MainWindow)
        except Exception as e:
            self.message_box_wrong_password()


    def message_box_wrong_password(self):
        dialog=QMessageBox()
        dialog.setText("wrong e-mail or password!")
        dialog.setWindowTitle("Invalid Input")
        dialog.exec_()


    def order_open_window(self,Mainwindow):
        from pizza_order import Ui_siparis_window
        self.window=QtWidgets.QMainWindow()
        self.uin=Ui_siparis_window()
        self.uin.setupUi(self.window)
        Mainwindow.hide()
        self.window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Menu"))
        self.newregisterbutton.setText(_translate("MainWindow", "Sign-up"))
        self.paswordlabelnull.setText(_translate("MainWindow", "Password : "))
        self.namelabelisnull.setText(_translate("MainWindow", "E_mail :"))
        self.forgetmypasswordbutton.setText(_translate("MainWindow", "Forgot Password?"))
        self.loginbutton.setText(_translate("MainWindow", "Sign-in"))


if __name__ == "__main__":
    main()
