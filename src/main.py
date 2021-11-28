import sys

from PyQt5.QtWidgets import QApplication

from controller.Controller import Controller
from model.Model import Model
from view.ImageViewer import ImageViewer

app = QApplication(sys.argv)
model = Model()
mainWindow = ImageViewer()
controller = Controller(mainWindow, model)
mainWindow.show()
sys.exit(app.exec_())
