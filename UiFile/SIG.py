from PyQt5.QtCore import QObject, pyqtSignal


class MySignals(QObject):
    mclDebug = pyqtSignal(str)


mysig = MySignals()
