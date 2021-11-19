from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QAbstractItemView

from src.model import QEXIFModel


class EXIFDialog(QtWidgets.QDialog):
    def __init__(self, exifData: dict):
        super().__init__()
        self.setObjectName("Dialog")
        self.resize(345, 450)
        self.setWindowTitle("Dati EXIF")

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setObjectName("tableView")
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(150)
        self.tableView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView.verticalHeader().setDefaultSectionSize(10)
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
