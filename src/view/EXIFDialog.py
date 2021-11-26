from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QAbstractItemView, QPushButton, QHBoxLayout, QLabel

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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        if "GPS Coordinates (DD)" in exifData:
            self.linkMappaGPS = QLabel(self)
            self.linkMappaGPS.setObjectName(u"linkMappaGPS")
            self.linkMappaGPS.setAlignment(QtCore.Qt.AlignCenter)
            self.linkMappaGPS.setText("<a href=\'https://www.google.com/maps/search/?api=1&query=" + str(exifData["GPS Coordinates (DD)"]) + "\'>Mappa GPS</a>")
            self.linkMappaGPS.setOpenExternalLinks(True)
            self.horizontalLayout.addWidget(self.linkMappaGPS)

        self.bottoneChiudi = QPushButton(self)
        self.bottoneChiudi.setObjectName(u"bottoneChiudi")
        self.bottoneChiudi.setText("Chiudi")
        self.bottoneChiudi.clicked.connect(self.accept)
        self.horizontalLayout.addWidget(self.bottoneChiudi)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 3, 1)
