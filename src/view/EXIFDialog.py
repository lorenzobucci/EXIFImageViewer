from PyQt5 import QtCore, QtWidgets

from src.model import QEXIFModel


class EXIFDialog(QtWidgets.QDialog):
    def __init__(self, exifData: dict):
        super().__init__()
        self.setObjectName("Dialog")
        self.resize(330, 390)
        self.setWindowTitle("Dati EXIF")

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setObjectName("tableView")
        self.tableView.setModel(QEXIFModel.QEXIFModel(exifData))
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Close).setText("Chiudi")
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
