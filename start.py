from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget

from pizza_full_database import (
    Customer_Database, 
    incoming_pizza_order_database,
    pizza_Database,
    addition_Metarial
)

from register import UiRegisterWindow
from forgot_password import Ui_forgetmypassword
from pizza_order import Ui_siparis_window

import sys


def main():
    # Set default menu
    set_default_menu()

    # Create QApplication instance
    app = QtWidgets.QApplication(sys.argv)

    # Create and show main window
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_startWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Start the application event loop
    sys.exit(app.exec_())


def set_default_menu():
    pizza_db = pizza_Database()
    component_db = addition_Metarial()

    class Pizza():
        def __init__(self, name, description, cost):
            self._description = description
            self._cost = cost
            self._name = name
        
        def __str__(self):
            return self._name

        def get_description(self):
            return self._description
        
        def get_cost(self):
            return self._cost

    class Standart_Pizza(Pizza):
        def __init__(self, name, description, cost):
            super().__init__(name, description, cost)
        
    class Dominos_Pizza(Pizza):
        def __init__(self, name, description, cost):
            super().__init__(name, description, cost)
        
    class Margherita_Pizza(Pizza):
        def __init__(self, name, description, cost):
            super().__init__(name, description, cost)
            
    class Turkish_Pizza(Pizza):
        def __init__(self, name, description, cost):
            super().__init__(name, description, cost)

    class BBQ_Pizza(Pizza):
        def __init__(self, name, description, cost):
            super().__init__(name, description, cost)

    # Decorator Part----
    class Decorator(Pizza):
        def __init__(self, name, description, cost):
            super().__init__(name, description, cost)

    class Mushroom(Decorator):
        def __init__(self, name, description, cost):
            super().__init__(name, description, cost)

    class Sausage(Decorator):
        def __init__(self, name, description, cost):
            super().__init__(name, description, cost)

    class Olive(Decorator):
        def __init__(self, name, description, cost):
            super().__init__(name, description, cost)

    class Corn(Decorator):
        def __init__(self, name, description, cost):
            super().__init__(name, description, cost)

    class Nugget(Decorator):
        def __init__(self, name, description, cost):
            super().__init__(name, description, cost)


    pizzas = [
        Standart_Pizza("Standart Pizza", "literally normal", "2.49"),
        Margherita_Pizza("Margherita Pizza", "cheesy", "3.99"),
        Dominos_Pizza("Dominos Pizza", "can be cause of domino effect", "4.99"),
        Turkish_Pizza("Turkish Pizza", "Best Turkish kebab", "4.99"),
        BBQ_Pizza("BBQ Pizza", "BBQ sauce with chicken nuggets", "4.99")
    ]

    for pizza in pizzas:
        pizza_db.insert_pizza(str(pizza), pizza.get_cost(), pizza.get_description())

    components = [
        Mushroom("Mushroom", "it tastes like a meat", "0.30"),
        Sausage("Sausage", "%100 cow meat", "0.35"),
        Nugget("Nugget", "Chicken nuggets", "0.25"),
        Olive("Olive", "from the branch", "0.20"),
        Corn("Corn", "with the cob", "0.25")
    ]

    for component in components:
        component_db.insert_addmade(str(component), component.get_cost(), component.get_description())
    
class Ui_startWindow(object):

    def setupUi(self, MainWindow):
        self.incoming_pizza_order = incoming_pizza_order_database()
        self.customerdatabasechecklogin = Customer_Database() 

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 317)

        # Center the window on the screen
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())

        # Create the main widget and layouts
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        # Create the UI elements and add them to the layout
        self.namelabelisnull = QtWidgets.QLabel(self.centralwidget)
        self.namelabelisnull.setObjectName("namelabelisnull")
        self.gridLayout.addWidget(self.namelabelisnull, 0, 0, 1, 1)

        self.inputnamelabel = QtWidgets.QLineEdit(self.centralwidget)
        self.inputnamelabel.setObjectName("inputnamelabel")
        self.gridLayout.addWidget(self.inputnamelabel, 0, 1, 1, 2)

        self.paswordlabelnull = QtWidgets.QLabel(self.centralwidget)
        self.paswordlabelnull.setObjectName("paswordlabelnull")
        self.gridLayout.addWidget(self.paswordlabelnull, 1, 0, 1, 1)

        self.inputpasswordlabel = QtWidgets.QLineEdit(self.centralwidget)
        self.inputpasswordlabel.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputpasswordlabel.setObjectName("inputpasswordlabel")
        self.gridLayout.addWidget(self.inputpasswordlabel, 1, 1, 1, 2)

        self.newregisterbutton = QtWidgets.QPushButton(self.centralwidget)
        self.newregisterbutton.setObjectName("newregisterbutton")
        self.gridLayout.addWidget(self.newregisterbutton, 2, 0, 1, 1)

        self.forgetmypasswordbutton = QtWidgets.QPushButton(self.centralwidget)
        self.forgetmypasswordbutton.setObjectName("forgetmypasswordbutton")
        self.gridLayout.addWidget(self.forgetmypasswordbutton, 2, 1, 1, 1)

        self.loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loginbutton.setObjectName("loginbutton")
        self.gridLayout.addWidget(self.loginbutton, 2, 2, 1, 1)

        # Add the layout to the main layout
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        # Set the main widget and menu bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Set the status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Connect the buttons to their respective functions
        self.loginbutton.clicked.connect(lambda: self.check_login_reading(MainWindow))
        self.newregisterbutton.clicked.connect(lambda: self.new_register_open_window(MainWindow))
        self.forgetmypasswordbutton.clicked.connect(lambda: self.new_forget_my_password(MainWindow))

        # Set the UI strings
        self.retranslateUi(MainWindow)


    def new_register_open_window(self, main_window):
        self.register_window = QtWidgets.QMainWindow()
        self.register_ui = UiRegisterWindow()
        self.register_ui.setup_ui(self.register_window)
        main_window.hide()
        self.register_window.show()


    def new_forget_my_password(self, main_window):
        self.forgot_password_window = QtWidgets.QMainWindow()
        self.forgot_password_ui = Ui_forgetmypassword()
        self.forgot_password_ui.setupUi(self.forgot_password_window)
        main_window.hide()
        self.forgot_password_window.show()


    def check_login_reading(self, MainWindow):
        username = self.inputnamelabel.text()
        password = self.inputpasswordlabel.text()

        try:
            personal_numb = self.customerdatabasechecklogin.check_login(username, password)
        except Exception as e:
            self.message_box_wrong_password()
            return

        if personal_numb:
            with open("currentcustomer.txt", "w") as file:
                file.write(f"{personal_numb}")
            self.incoming_pizza_order.all_order_database_delete()
            self.order_open_window(MainWindow)


    def message_box_wrong_password(self):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Critical)
        dialog.setText(f"Invalid username or password!")
        dialog.setWindowTitle("Error")
        dialog.setStandardButtons(QMessageBox.Ok)
        dialog.exec_()


    def order_open_window(self, Mainwindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_siparis_window()
        self.ui.setupUi(self.window)
        Mainwindow.hide()
        self.window.show()

    # This is where you can change the UI strings
    def retranslateUi(self, MainWindow):
        self.translations = {
            "window_title": "Login Menu",
            "register_button": "Sign-up",
            "password_label": "Password:",
            "email_label": "E-mail:",
            "forgot_password_button": "Forgot Password?",
            "login_button": "Sign-in"
        }

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.translations["window_title"]))
        self.newregisterbutton.setText(_translate("MainWindow", self.translations["register_button"]))
        self.paswordlabelnull.setText(_translate("MainWindow", self.translations["password_label"]))
        self.namelabelisnull.setText(_translate("MainWindow", self.translations["email_label"]))
        self.forgetmypasswordbutton.setText(_translate("MainWindow", self.translations["forgot_password_button"]))
        self.loginbutton.setText(_translate("MainWindow", self.translations["login_button"]))


if __name__ == "__main__":
    main()
