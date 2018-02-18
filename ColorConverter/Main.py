from PyQt5.QtWidgets import QApplication
import sys

from ColorWindowLogic import ColorLogic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = ColorLogic()
    sys.exit(app.exec_())
