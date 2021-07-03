import sys
from PyQt5.QtWidgets import QWidget, QApplication, QAction, QFormLayout, QVBoxLayout, QHBoxLayout, QMainWindow, QGridLayout, QTabBar, QLabel
from PyQt5.QtGui import QIcon

__appname__ = 'Kespers Grimoire'


class HomeScreen(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(__appname__)
        self.setWindowIcon(QIcon('../package-assets/kesp-icon.png'))
        self.resize(1080, 720)

        # Tab Bar
        ms_tb = QTabBar()
        ms_tb.addTab('New Asset')
        ms_tb.addTab('All Assets')
        self.setCentralWidget(ms_tb)


def main():
    app = QApplication(sys.argv)
    win = HomeScreen()
    app.setApplicationName(__appname__)
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
