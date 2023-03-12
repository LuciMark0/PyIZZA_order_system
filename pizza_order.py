from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
from pizza_full_database import pizza_Database, addition_Metarial, incoming_pizza_order_database

data1=pizza_Database()
data2=addition_Metarial()
data3=incoming_pizza_order_database()

all_pizza=data1.get_all_pizza()
all_addmade=data2.get_all_addmade()


class Ui_siparis_window(object):
    def setupUi(self, MainWindow):
        data1=pizza_Database()
        data2=addition_Metarial()
        _translate = QtCore.QCoreApplication.translate
        all_pizza=data1.get_all_pizza()
        all_addmade=data2.get_all_addmade()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pizzanamescrollarea = QtWidgets.QScrollArea(self.centralwidget)
        self.pizzanamescrollarea.setAcceptDrops(False)
        self.pizzanamescrollarea.setWidgetResizable(True)
        self.pizzanamescrollarea.setObjectName("pizzanamescrollarea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 261, 603))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.add_all_pizza_name=[]
        for index,i in enumerate(all_pizza):
            pizza= QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setPointSize(13)
            pizza.setFont(font)
            pizza.setObjectName(i[0]+"_radio_button")
            self.gridLayout_2.addWidget(pizza, index, 0, 1, 1)
            pizza.setText(_translate("MainWindow", f"{i[0]}: {i[2]}, {i[1]}$"))
            self.add_all_pizza_name.append(pizza)


#end pizza_name-----------------------------------------

        self.pizzanamescrollarea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.pizzanamescrollarea, 0, 0, 1, 1)
        self.addmade = QtWidgets.QScrollArea(self.centralwidget)
        self.addmade.setWidgetResizable(True)
        self.addmade.setObjectName("addmade")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 278, 406))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)

        self.add_all_made=[]
        for index,i in enumerate(all_addmade):
            addmade = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
            font = QtGui.QFont()
            font.setPointSize(15)
            addmade.setFont(font)
            addmade.setObjectName(i[0]+"_check_box_")
            self.gridLayout_3.addWidget(addmade, index, 0, 1, 1)
            addmade.setText(_translate("MainWindow", f"{i[0]}: {i[2]}, {i[1]}$"))
            self.add_all_made.append(addmade)

#end add_made-----------------------------------------
     
        self.addmade.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.addmade, 0, 1, 1, 1)
        self.sepetigoruntule = QtWidgets.QPushButton(self.centralwidget)
        self.sepetigoruntule.setObjectName("sepeti goruntule")
        self.gridLayout.addWidget(self.sepetigoruntule, 1, 0, 1, 1)
        self.sepeteekle = QtWidgets.QPushButton(self.centralwidget)
        self.sepeteekle.setObjectName("sepeteekle")
        self.gridLayout.addWidget(self.sepeteekle, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.sepeteekle.clicked.connect(lambda: self.sepetigoruntuleeklenecekveriler())
        
        self.sepetigoruntule.clicked.connect(lambda :self.sepetekraniniacma(MainWindow))


    def sepetekraniniacma(self,Mainwindow):
        from pizza_cart import Uİ_pizza_sepet
        self.window = QtWidgets.QMainWindow()
        self.ui = Uİ_pizza_sepet()
        self.ui.setupUi(self.window)
        Mainwindow.hide()
        self.window.show()
        

    def sepetigoruntuleeklenecekveriler(self):
        siparis=[]
        pizza_exist = False
        for index,i in enumerate(self.add_all_pizza_name):
            if(i.isChecked()):
                siparis.append(all_pizza[index])
                pizza_exist = True
      
        for index,i in enumerate(self.add_all_made):
            if(i.isChecked()):
                siparis.append(all_addmade[index])

        
        if not pizza_exist:
            self.message_box_not_selected()
            return False


        siparis_Str=""
        for i in siparis:
            for j in i:
                siparis_Str+=str(j)+"-"

        
        pizza_name=("-".join(siparis_Str.split("-")[:3]))
        pizza_add_names=("-".join(siparis_Str.split("-")[3:-1]))
                
        data3.insert_cart(pizza_name, pizza_add_names)

        for chose_check in self.add_all_made:
            if chose_check.isChecked():
                chose_check.setChecked(False)

    def message_box_not_selected(self):
        dialog=QMessageBox()
        dialog.setText("You must select at least 1 pizza to add!")
        dialog.setWindowTitle("Invalid Action")
        dialog.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Order Select Menu"))
        self.sepetigoruntule.setText(_translate("MainWindow", "Go to cart"))
        self.sepeteekle.setText(_translate("MainWindow", "Add to cart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_siparis_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
