import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from logic import Logic


def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    logic = Logic(ui)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()