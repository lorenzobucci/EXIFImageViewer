from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QPushButton, QHBoxLayout, QLabel, QDialog, QGridLayout, QTableView

from model.QEXIFModel import QEXIFModel


class EXIFDialog(QDialog):
    def __init__(self, exifData: dict):
        super().__init__()
        self.setObjectName("Dialog")
        self.resize(345, 450)
        self.setWindowTitle("Dati EXIF")

        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.tableView = QTableView(self)
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
            self.GPSMapLink = QLabel(self)
            self.GPSMapLink.setObjectName(u"linkMappaGPS")
            self.GPSMapLink.setAlignment(Qt.AlignCenter)
            self.GPSMapLink.setText("<a href=\'https://www.google.com/maps/search/?api=1&query=" + str(
                exifData["GPS Coordinates (DD)"]) + "\'>Mappa GPS</a>")
            self.GPSMapLink.setOpenExternalLinks(True)
            self.horizontalLayout.addWidget(self.GPSMapLink)

        self.closeBtn = QPushButton(self)
        self.closeBtn.setObjectName(u"bottoneChiudi")
        self.closeBtn.setText("Chiudi")
        self.closeBtn.clicked.connect(self.accept)
        self.horizontalLayout.addWidget(self.closeBtn)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 3, 1)
