import sys

from PyQt5 import QtWidgets

from src.controller.Controller import Controller
from src.model.Model import Model
from src.view.ImageViewer import ImageViewer

app = QtWidgets.QApplication(sys.argv)
model = Model()
mainWindow = ImageViewer()
controller = Controller(mainWindow, model)
mainWindow.show()
sys.exit(app.exec_())
