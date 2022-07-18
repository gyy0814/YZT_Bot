

from PyQt5.QtWidgets import QApplication
import logging
import QFile.Mcl
import Ui
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = Ui.MainWindow()
    MainWindow.show()

    app.exec_()

