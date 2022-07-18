import logging
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QObject, pyqtSignal, Qt
from concurrent.futures import ThreadPoolExecutor
from QFile.Mcl import MCL
from UiFile import Ui1, SIG

pool = ThreadPoolExecutor(max_workers=50)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.result = None
        self.ui = Ui1.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        self.setMouseTracking(True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 添加阴影
        self.effect_shadow = QGraphicsDropShadowEffect(self)
        self.effect_shadow.setOffset(0, 0)  # 偏移
        self.effect_shadow.setBlurRadius(10)  # 阴影半径
        self.effect_shadow.setColor(Qt.gray)  # 阴影颜色
        self.setGraphicsEffect(self.effect_shadow)

        self.connected()

        self.mcl = None

    def connected(self):
        SIG.mysig.mclDebug.connect(self.mclDebugShow)
        self.ui.mclStop.clicked.connect(self.btn_mclStop_bg)
        self.ui.mclRun.clicked.connect(self.btn_mclRun_bg)
        self.ui.closeWindow.clicked.connect(self.btn_closeWindow_bg)
        self.ui.miniWindow.clicked.connect(self.btn_miniWindow_bg)

    def mclDebugShow(self, msg):
        # print(msg)
        self.ui.mcl_output.append(msg)
        self.ui.mcl_output.ensureCursorVisible()

    def btn_mclRun_bg(self):
        logging.debug("btn_mclRun_bg run!")
        self.mcl = MCL()
        self.ui.mclRun.setEnabled(False)
        self.ui.mclStop.setEnabled(True)
        pool.submit(self.mcl.readLine)
        pass

    def btn_mclStop_bg(self):
        logging.debug("btn_mclStop_bg run!")
        if self.mcl:
            self.mcl.stop()

    def btn_closeWindow_bg(self):
        logging.debug("btn_mclStop_bg run!")
        self.close()
        pass

    def btn_miniWindow_bg(self):
        logging.debug("btn_mclRun_bg run!")
        pass
