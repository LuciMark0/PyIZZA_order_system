import re
from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow, QMessageBox,
                             QScrollArea, QDesktopWidget, QWidget, QGridLayout,
                             QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy)
from PyQt5.QtCore import QCoreApplication, QRect
from validator_collection import validators
from pizza_full_database import Customer_Database

class UiRegisterWindow(object):
    def __init__(self):
        self.database_addition = Customer_Database()

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(566, 301)
        qr = main_window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        main_window.move(qr.topLeft())

        central_widget = QWidget(main_window)
        central_widget.setObjectName("centralwidget")
        main_layout = QGridLayout(central_widget)
        main_layout.setObjectName("gridLayout")

        scroll_area = self.create_scroll_area(central_widget)
        scroll_area_widget = QWidget()
        scroll_area.setWidget(scroll_area_widget)
        scroll_layout = QGridLayout(scroll_area_widget)
        scroll_layout.setObjectName("gridLayout_2")

        personal_num_label = QLabel(scroll_area_widget)
        personal_num_label.setObjectName("personalnumber_label")
        scroll_layout.addWidget(personal_num_label, 1, 0, 1, 1)

        self.input_personal_num_line = QLineEdit(scroll_area_widget)
        self.input_personal_num_line.setObjectName("input_personal_number_line")
        scroll_layout.addWidget(self.input_personal_num_line, 1, 1, 1, 1)

        name_label = QLabel(scroll_area_widget)
        name_label.setObjectName("name_label")
        scroll_layout.addWidget(name_label, 2, 0, 1, 1)

        self.input_name_line = QLineEdit(scroll_area_widget)
        self.input_name_line.setObjectName("input_name_line")
        scroll_layout.addWidget(self.input_name_line, 2, 1, 1, 1)

        password_label = QLabel(scroll_area_widget)
        password_label.setObjectName("password_label")
        scroll_layout.addWidget(password_label, 3, 0, 1, 1)

        self.input_password_line = QLineEdit(scroll_area_widget)
        self.input_password_line.setEchoMode(QLineEdit.Password)
        self.input_password_line.setObjectName("input_password_line")
        scroll_layout.addWidget(self.input_password_line, 3, 1, 1, 1)

        email_label = QLabel(scroll_area_widget)
        email_label.setObjectName("email_label")
        scroll_layout.addWidget(email_label, 4, 0, 1, 1)

        self.input_email_line = QLineEdit(scroll_area_widget)
        self.input_email_line.setObjectName("input_email_line")
        scroll_layout.addWidget(self.input_email_line, 4, 1, 1, 1)

        spacer_item1 = self.create_spacer_item()
        scroll_layout.addItem(spacer_item1, 0, 1, 1, 1)

        spacer_item2 = self.create_spacer_item()
        scroll_layout.addItem(spacer_item2, 5, 1, 1, 1)

        new_register_button = QPushButton(scroll_area_widget)
        new_register_button.setObjectName("new_register_button")
        new_register_button.clicked.connect(lambda: self.add_database_control(main_window))
        scroll_layout.addWidget(new_register_button, 6, 1, 1, 1)

        main_layout.addWidget(scroll_area, 0, 0, 1, 1)
        main_window.setCentralWidget(central_widget)

        menubar = main_window.menuBar()
        menubar.setGeometry(QRect(0, 0, 566, 21))
        menubar.setObjectName("menubar")
        main_window.setMenuBar(menubar)

        self.statusbar = QMainWindow.statusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)
        QCoreApplication.instance().setStyleSheet("QPushButton {background-color: #008CBA; color: white;}")

    def create_scroll_area(self, widget):
        scroll_area = QScrollArea(widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName("scrollArea")
        return scroll_area

    def create_spacer_item(self):
        return QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

    def retranslate_ui(self, main_window):
        translation = QCoreApplication.translate
        main_window.setWindowTitle(translation("MainWindow", "Register Menu"))
        personal_number_label = main_window.findChild(QLabel, "personalnumber_label")
        personal_number_label.setText(translation("MainWindow", "Personal ID: "))
        name_label = main_window.findChild(QLabel, "name_label")
        name_label.setText(translation("MainWindow", "Name: "))
        password_label = main_window.findChild(QLabel, "password_label")
        password_label.setText(translation("MainWindow", "Password: "))
        email_label = main_window.findChild(QLabel, "email_label")
        email_label.setText(translation("MainWindow", "E-mail: "))
        new_register_button = main_window.findChild(QPushButton, "new_register_button")
        new_register_button.setText(translation("MainWindow", "Sign-up"))

    def add_database_control(self, main_window):
        try:
            self.signup()

            self.database_addition.insert_customer(self.input_personal_num_line.text(),
                                                    self.input_name_line.text(),
                                                    self.input_password_line.text(),
                                                    self.input_email_line.text())
            self.message_box_successful()

            from start import Ui_startWindow
            start_window = QMainWindow()
            start_ui = Ui_startWindow()
            start_ui.setupUi(start_window)

            main_window.hide()
            start_window.show()

        except Exception as e:
            self.message_box_error(str(e))

    def message_box_error(self, error_message):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Critical)
        dialog.setText(error_message)
        dialog.setWindowTitle("Error")
        dialog.exec_()

    def message_box_successful(self):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Information)
        dialog.setText("Your registration is successful.")
        dialog.setWindowTitle("Success")
        dialog.exec_()

    def signup(self):
        name = self.input_name_line.text()
        if not re.match("^[A-Za-zşöçığüŞÖÇİĞÜ\s]+$", name):
            raise ValueError("Invalid name.")

        personal_id = self.input_personal_num_line.text()
        if not re.match("^\d{11}$", personal_id):
            raise ValueError("Invalid personal ID.")
        if self.database_addition.personal_number_checked(personal_id) is not None:
            raise ValueError("Personal ID already exists.")

        email = self.input_email_line.text()
        if email.strip() != "" and not validators.email(email):
            raise ValueError("Invalid email.")

        password = self.input_password_line.text()
        if not re.match("^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
            raise ValueError("Weak password. Password must contain at least 8 characters with 1 uppercase letter, 1 lowercase letter, 1 number and 1 special character.")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = UiRegisterWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
