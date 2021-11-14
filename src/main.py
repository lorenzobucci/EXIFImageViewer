import sys

from PyQt5 import QtWidgets

from src.controller.Controller import Controller
from src.view.ImageViewer import ImageViewer

app = QtWidgets.QApplication(sys.argv)
mainWindow = ImageViewer()
controller = Controller(mainWindow)
mainWindow.show()
sys.exit(app.exec_())
