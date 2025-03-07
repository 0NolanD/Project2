# Form implementation generated from reading ui file 'MenuProject.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(500, 321)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CheckoutButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.CheckoutButton.setGeometry(QtCore.QRect(0, 210, 120, 70))
        self.CheckoutButton.setObjectName("CheckoutButton")
        self.DrinksButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.DrinksButton.setGeometry(QtCore.QRect(0, 140, 120, 70))
        self.DrinksButton.setObjectName("DrinksButton")
        self.FriesButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.FriesButton.setGeometry(QtCore.QRect(0, 70, 120, 70))
        self.FriesButton.setObjectName("FriesButton")
        self.BurgerButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BurgerButton.setGeometry(QtCore.QRect(0, 0, 120, 70))
        self.BurgerButton.setObjectName("BurgerButton")
        self.Screens = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.Screens.setGeometry(QtCore.QRect(140, 10, 321, 271))
        self.Screens.setObjectName("Screens")
        self.WelcomePage = QtWidgets.QWidget()
        self.WelcomePage.setObjectName("WelcomePage")
        self.WelcomeLabel = QtWidgets.QLabel(parent=self.WelcomePage)
        self.WelcomeLabel.setGeometry(QtCore.QRect(30, 70, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        self.Screens.addWidget(self.WelcomePage)
        self.BurgersPage = QtWidgets.QWidget()
        self.BurgersPage.setObjectName("BurgersPage")
        self.PattyInput = QtWidgets.QLineEdit(parent=self.BurgersPage)
        self.PattyInput.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.PattyInput.setObjectName("PattyInput")
        self.NumOfPatties = QtWidgets.QLabel(parent=self.BurgersPage)
        self.NumOfPatties.setGeometry(QtCore.QRect(20, 50, 101, 21))
        self.NumOfPatties.setObjectName("NumOfPatties")
        self.CheeseButton = QtWidgets.QCheckBox(parent=self.BurgersPage)
        self.CheeseButton.setGeometry(QtCore.QRect(20, 90, 62, 14))
        self.CheeseButton.setObjectName("CheeseButton")
        self.BurgerHeader = QtWidgets.QLabel(parent=self.BurgersPage)
        self.BurgerHeader.setGeometry(QtCore.QRect(90, 0, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.BurgerHeader.setFont(font)
        self.BurgerHeader.setObjectName("BurgerHeader")
        self.MustardBox = QtWidgets.QCheckBox(parent=self.BurgersPage)
        self.MustardBox.setGeometry(QtCore.QRect(30, 120, 62, 14))
        self.MustardBox.setObjectName("MustardBox")
        self.KetchupBox = QtWidgets.QCheckBox(parent=self.BurgersPage)
        self.KetchupBox.setGeometry(QtCore.QRect(110, 120, 62, 14))
        self.KetchupBox.setObjectName("KetchupBox")
        self.OnionBox = QtWidgets.QCheckBox(parent=self.BurgersPage)
        self.OnionBox.setGeometry(QtCore.QRect(190, 120, 62, 14))
        self.OnionBox.setObjectName("OnionBox")
        self.PickleBox = QtWidgets.QCheckBox(parent=self.BurgersPage)
        self.PickleBox.setGeometry(QtCore.QRect(30, 140, 62, 14))
        self.PickleBox.setObjectName("PickleBox")
        self.LettuceBox = QtWidgets.QCheckBox(parent=self.BurgersPage)
        self.LettuceBox.setGeometry(QtCore.QRect(110, 140, 62, 14))
        self.LettuceBox.setObjectName("LettuceBox")
        self.TomatoBox = QtWidgets.QCheckBox(parent=self.BurgersPage)
        self.TomatoBox.setGeometry(QtCore.QRect(190, 140, 62, 14))
        self.TomatoBox.setObjectName("TomatoBox")
        self.CheeseInput = QtWidgets.QLineEdit(parent=self.BurgersPage)
        self.CheeseInput.setGeometry(QtCore.QRect(200, 90, 113, 20))
        self.CheeseInput.setObjectName("CheeseInput")
        self.NumOfSlices = QtWidgets.QLabel(parent=self.BurgersPage)
        self.NumOfSlices.setEnabled(True)
        self.NumOfSlices.setGeometry(QtCore.QRect(110, 90, 71, 16))
        self.NumOfSlices.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.NumOfSlices.setObjectName("NumOfSlices")
        self.BurgerError = QtWidgets.QLabel(parent=self.BurgersPage)
        self.BurgerError.setGeometry(QtCore.QRect(50, 190, 211, 16))
        self.BurgerError.setText("")
        self.BurgerError.setObjectName("BurgerError")
        self.BurgerConfirm = QtWidgets.QPushButton(parent=self.BurgersPage)
        self.BurgerConfirm.setGeometry(QtCore.QRect(120, 210, 71, 21))
        self.BurgerConfirm.setObjectName("BurgerConfirm")
        self.AllButton = QtWidgets.QPushButton(parent=self.BurgersPage)
        self.AllButton.setGeometry(QtCore.QRect(40, 160, 81, 21))
        self.AllButton.setObjectName("AllButton")
        self.NoButton = QtWidgets.QPushButton(parent=self.BurgersPage)
        self.NoButton.setGeometry(QtCore.QRect(150, 160, 81, 21))
        self.NoButton.setObjectName("NoButton")
        self.Screens.addWidget(self.BurgersPage)
        self.FriesPage = QtWidgets.QWidget()
        self.FriesPage.setObjectName("FriesPage")
        self.FriesHeader = QtWidgets.QLabel(parent=self.FriesPage)
        self.FriesHeader.setGeometry(QtCore.QRect(110, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.FriesHeader.setFont(font)
        self.FriesHeader.setObjectName("FriesHeader")
        self.SmallFryButton = QtWidgets.QRadioButton(parent=self.FriesPage)
        self.SmallFryButton.setGeometry(QtCore.QRect(40, 60, 51, 16))
        self.SmallFryButton.setObjectName("SmallFryButton")
        self.MediumFryButton = QtWidgets.QRadioButton(parent=self.FriesPage)
        self.MediumFryButton.setGeometry(QtCore.QRect(120, 60, 71, 16))
        self.MediumFryButton.setObjectName("MediumFryButton")
        self.LargeFryButton = QtWidgets.QRadioButton(parent=self.FriesPage)
        self.LargeFryButton.setGeometry(QtCore.QRect(210, 60, 62, 14))
        self.LargeFryButton.setObjectName("LargeFryButton")
        self.FryConfirm = QtWidgets.QPushButton(parent=self.FriesPage)
        self.FryConfirm.setGeometry(QtCore.QRect(120, 100, 56, 17))
        self.FryConfirm.setObjectName("FryConfirm")
        self.FryError = QtWidgets.QLabel(parent=self.FriesPage)
        self.FryError.setGeometry(QtCore.QRect(90, 80, 151, 16))
        self.FryError.setText("")
        self.FryError.setObjectName("FryError")
        self.Screens.addWidget(self.FriesPage)
        self.DrinksPage = QtWidgets.QWidget()
        self.DrinksPage.setObjectName("DrinksPage")
        self.DrinkHeader = QtWidgets.QLabel(parent=self.DrinksPage)
        self.DrinkHeader.setGeometry(QtCore.QRect(90, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.DrinkHeader.setFont(font)
        self.DrinkHeader.setObjectName("DrinkHeader")
        self.SmallDrinkButton = QtWidgets.QRadioButton(parent=self.DrinksPage)
        self.SmallDrinkButton.setGeometry(QtCore.QRect(40, 60, 61, 16))
        self.SmallDrinkButton.setObjectName("SmallDrinkButton")
        self.MediumDrinkButton = QtWidgets.QRadioButton(parent=self.DrinksPage)
        self.MediumDrinkButton.setGeometry(QtCore.QRect(120, 60, 71, 16))
        self.MediumDrinkButton.setObjectName("MediumDrinkButton")
        self.LargeDrinkButton = QtWidgets.QRadioButton(parent=self.DrinksPage)
        self.LargeDrinkButton.setGeometry(QtCore.QRect(210, 60, 61, 16))
        self.LargeDrinkButton.setObjectName("LargeDrinkButton")
        self.DrinkInput = QtWidgets.QComboBox(parent=self.DrinksPage)
        self.DrinkInput.setGeometry(QtCore.QRect(90, 100, 111, 22))
        self.DrinkInput.setObjectName("DrinkInput")
        self.DrinkInput.addItem("")
        self.DrinkInput.addItem("")
        self.DrinkInput.addItem("")
        self.DrinkInput.addItem("")
        self.DrinkInput.addItem("")
        self.DrinkInput.addItem("")
        self.DietCheck = QtWidgets.QCheckBox(parent=self.DrinksPage)
        self.DietCheck.setGeometry(QtCore.QRect(120, 130, 53, 14))
        self.DietCheck.setObjectName("DietCheck")
        self.DrinkError = QtWidgets.QLabel(parent=self.DrinksPage)
        self.DrinkError.setGeometry(QtCore.QRect(60, 160, 171, 16))
        self.DrinkError.setText("")
        self.DrinkError.setObjectName("DrinkError")
        self.DrinkConfirm = QtWidgets.QPushButton(parent=self.DrinksPage)
        self.DrinkConfirm.setGeometry(QtCore.QRect(110, 200, 56, 17))
        self.DrinkConfirm.setObjectName("DrinkConfirm")
        self.Screens.addWidget(self.DrinksPage)
        self.CheckoutPage = QtWidgets.QWidget()
        self.CheckoutPage.setObjectName("CheckoutPage")
        self.CheckoutDisplay = QtWidgets.QTextBrowser(parent=self.CheckoutPage)
        self.CheckoutDisplay.setGeometry(QtCore.QRect(30, 10, 251, 151))
        self.CheckoutDisplay.setObjectName("CheckoutDisplay")
        self.Tip15Button = QtWidgets.QRadioButton(parent=self.CheckoutPage)
        self.Tip15Button.setGeometry(QtCore.QRect(40, 190, 62, 21))
        self.Tip15Button.setObjectName("Tip15Button")
        self.Tip20Button = QtWidgets.QRadioButton(parent=self.CheckoutPage)
        self.Tip20Button.setGeometry(QtCore.QRect(40, 210, 62, 21))
        self.Tip20Button.setObjectName("Tip20Button")
        self.Tip25Button = QtWidgets.QRadioButton(parent=self.CheckoutPage)
        self.Tip25Button.setGeometry(QtCore.QRect(40, 230, 62, 21))
        self.Tip25Button.setObjectName("Tip25Button")
        self.CustomTipButton = QtWidgets.QRadioButton(parent=self.CheckoutPage)
        self.CustomTipButton.setGeometry(QtCore.QRect(40, 250, 62, 14))
        self.CustomTipButton.setObjectName("CustomTipButton")
        self.CheckoutConfirm = QtWidgets.QPushButton(parent=self.CheckoutPage)
        self.CheckoutConfirm.setGeometry(QtCore.QRect(250, 200, 56, 17))
        self.CheckoutConfirm.setObjectName("CheckoutConfirm")
        self.CheckoutClear = QtWidgets.QPushButton(parent=self.CheckoutPage)
        self.CheckoutClear.setGeometry(QtCore.QRect(250, 230, 56, 17))
        self.CheckoutClear.setObjectName("CheckoutClear")
        self.TipInput = QtWidgets.QLineEdit(parent=self.CheckoutPage)
        self.TipInput.setGeometry(QtCore.QRect(110, 220, 113, 20))
        self.TipInput.setObjectName("TipInput")
        self.PercentagePrompt = QtWidgets.QLabel(parent=self.CheckoutPage)
        self.PercentagePrompt.setGeometry(QtCore.QRect(120, 200, 101, 16))
        self.PercentagePrompt.setObjectName("PercentagePrompt")
        self.CheckoutError = QtWidgets.QLabel(parent=self.CheckoutPage)
        self.CheckoutError.setGeometry(QtCore.QRect(40, 170, 241, 20))
        self.CheckoutError.setText("")
        self.CheckoutError.setObjectName("CheckoutError")
        self.Screens.addWidget(self.CheckoutPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Screens.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ordering System"))
        self.CheckoutButton.setText(_translate("MainWindow", "Checkout"))
        self.DrinksButton.setText(_translate("MainWindow", "Drinks"))
        self.FriesButton.setText(_translate("MainWindow", "Fries"))
        self.BurgerButton.setText(_translate("MainWindow", "Burgers"))
        self.WelcomeLabel.setText(_translate("MainWindow", "Click a tab to begin your order!"))
        self.PattyInput.setText(_translate("MainWindow", "1"))
        self.NumOfPatties.setText(_translate("MainWindow", "Number of Patties:"))
        self.CheeseButton.setText(_translate("MainWindow", "Cheese"))
        self.BurgerHeader.setText(_translate("MainWindow", "Add a Burger"))
        self.MustardBox.setText(_translate("MainWindow", "Mustard"))
        self.KetchupBox.setText(_translate("MainWindow", "Ketchup"))
        self.OnionBox.setText(_translate("MainWindow", "Onion"))
        self.PickleBox.setText(_translate("MainWindow", "Pickle"))
        self.LettuceBox.setText(_translate("MainWindow", "Lettuce"))
        self.TomatoBox.setText(_translate("MainWindow", "Tomato"))
        self.CheeseInput.setText(_translate("MainWindow", "1"))
        self.NumOfSlices.setText(_translate("MainWindow", "Slices:"))
        self.BurgerConfirm.setText(_translate("MainWindow", "Confirm"))
        self.AllButton.setText(_translate("MainWindow", "All Toppings"))
        self.NoButton.setText(_translate("MainWindow", "No Toppings"))
        self.FriesHeader.setText(_translate("MainWindow", "Add Fries"))
        self.SmallFryButton.setText(_translate("MainWindow", "Small"))
        self.MediumFryButton.setText(_translate("MainWindow", "Medium"))
        self.LargeFryButton.setText(_translate("MainWindow", "Large"))
        self.FryConfirm.setText(_translate("MainWindow", "Confirm"))
        self.DrinkHeader.setText(_translate("MainWindow", "Add a Drink"))
        self.SmallDrinkButton.setText(_translate("MainWindow", "Small"))
        self.MediumDrinkButton.setText(_translate("MainWindow", "Medium"))
        self.LargeDrinkButton.setText(_translate("MainWindow", "Large"))
        self.DrinkInput.setItemText(0, _translate("MainWindow", "Select A Drink"))
        self.DrinkInput.setItemText(1, _translate("MainWindow", "Water"))
        self.DrinkInput.setItemText(2, _translate("MainWindow", "Pepsi"))
        self.DrinkInput.setItemText(3, _translate("MainWindow", "Mtn Dew"))
        self.DrinkInput.setItemText(4, _translate("MainWindow", "Root Beer"))
        self.DrinkInput.setItemText(5, _translate("MainWindow", "Iced Tea"))
        self.DietCheck.setText(_translate("MainWindow", "Diet"))
        self.DrinkConfirm.setText(_translate("MainWindow", "Confirm"))
        self.Tip15Button.setText(_translate("MainWindow", "15% Tip"))
        self.Tip20Button.setText(_translate("MainWindow", "20% Tip"))
        self.Tip25Button.setText(_translate("MainWindow", "25% Tip"))
        self.CustomTipButton.setText(_translate("MainWindow", "Custom Tip"))
        self.CheckoutConfirm.setText(_translate("MainWindow", "Confirm"))
        self.CheckoutClear.setText(_translate("MainWindow", "Clear"))
        self.PercentagePrompt.setText(_translate("MainWindow", "Enter Percentage:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
