import sys

from PyQt5 import QtWidgets

from src.view.ImageViewer import ImageViewer

app = QtWidgets.QApplication(sys.argv)
mainWindow = ImageViewer()
mainWindow.setImage("res/images/sample.jpg")
mainWindow.show()
sys.exit(app.exec_())