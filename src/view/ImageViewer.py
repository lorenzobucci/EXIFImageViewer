from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QStyle


class ImageViewer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("ImageViewer")
        self.resize(1022, 616)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.immagine = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.immagine.sizePolicy().hasHeightForWidth())
        self.immagine.setSizePolicy(sizePolicy)
        self.immagine.setAlignment(QtCore.Qt.AlignCenter)
        self.immagine.setObjectName("immagine")
        self.gridLayout.addWidget(self.immagine, 0, 0, 1, 7)

        spacerSx = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerSx, 1, 0, 1, 1)

        spacerDx = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerDx, 1, 6, 1, 1)

        self.bottoneTagEXIF = QtWidgets.QPushButton(self.centralwidget)
        self.bottoneTagEXIF.setMinimumSize(QSize(50, 50))
        self.bottoneTagEXIF.setMaximumSize(QSize(50, 50))
        self.bottoneTagEXIF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bottoneTagEXIF.setObjectName("BottoneTagEXIF")
        self.bottoneTagEXIF.setToolTip("Visualizza tag EXIF")
        self.bottoneTagEXIF.setIcon(self.bottoneTagEXIF.style().standardIcon(QStyle.SP_MessageBoxInformation))
        self.bottoneTagEXIF.setIconSize(QSize(24, 24))
        self.gridLayout.addWidget(self.bottoneTagEXIF, 1, 1, 1, 1)

        self.bottoneImmaginePrecedente = QtWidgets.QPushButton(self.centralwidget)
        self.bottoneImmaginePrecedente.setMinimumSize(QSize(50, 50))
        self.bottoneImmaginePrecedente.setMaximumSize(QSize(50, 50))
        self.bottoneImmaginePrecedente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bottoneImmaginePrecedente.setObjectName("BottoneImmaginePrecedente")
        self.bottoneImmaginePrecedente.setToolTip("Immagine precedente")
        self.bottoneImmaginePrecedente.setIcon(self.bottoneImmaginePrecedente.style().standardIcon(QStyle.SP_ArrowLeft))
        self.bottoneImmaginePrecedente.setIconSize(QSize(24, 24))
        self.gridLayout.addWidget(self.bottoneImmaginePrecedente, 1, 2, 1, 1)

        self.bottoneImmagineSuccessiva = QtWidgets.QPushButton(self.centralwidget)
        self.bottoneImmagineSuccessiva.setMinimumSize(QSize(50, 50))
        self.bottoneImmagineSuccessiva.setMaximumSize(QSize(50, 50))
        self.bottoneImmagineSuccessiva.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bottoneImmagineSuccessiva.setObjectName("BottoneImmagineSuccessiva")
        self.bottoneImmagineSuccessiva.setToolTip("Immagine successiva")
        self.bottoneImmagineSuccessiva.setIcon(
            self.bottoneImmagineSuccessiva.style().standardIcon(QStyle.SP_ArrowRight))
        self.bottoneImmagineSuccessiva.setIconSize(QSize(24, 24))
        self.gridLayout.addWidget(self.bottoneImmagineSuccessiva, 1, 3, 1, 1)

        self.bottoneRuotaAntiorario = QtWidgets.QPushButton(self.centralwidget)
        self.bottoneRuotaAntiorario.setMinimumSize(QSize(50, 50))
        self.bottoneRuotaAntiorario.setMaximumSize(QSize(50, 50))
        self.bottoneRuotaAntiorario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bottoneRuotaAntiorario.setObjectName("BottoneRuotaAntiorario")
        self.bottoneRuotaAntiorario.setToolTip("Ruota immagine in senso antiorario")
        iconaAntiorario = QIcon()
        iconaAntiorario.addFile(u"res/icons/rotate_left_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bottoneRuotaAntiorario.setIconSize(QSize(24, 24))
        self.bottoneRuotaAntiorario.setIcon(iconaAntiorario)
        self.gridLayout.addWidget(self.bottoneRuotaAntiorario, 1, 4, 1, 1)

        self.bottoneRuotaOrario = QtWidgets.QPushButton(self.centralwidget)
        self.bottoneRuotaOrario.setMinimumSize(QSize(50, 50))
        self.bottoneRuotaOrario.setMaximumSize(QSize(50, 50))
        self.bottoneRuotaOrario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bottoneRuotaOrario.setObjectName("BottoneRuotaOrario")
        self.bottoneRuotaOrario.setToolTip("Ruota immagine in senso orario")
        iconaOrario = QIcon()
        iconaOrario.addFile(u"res/icons/rotate_right_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bottoneRuotaOrario.setIcon(iconaOrario)
        self.bottoneRuotaOrario.setIconSize(QSize(24, 24))
        self.gridLayout.addWidget(self.bottoneRuotaOrario, 1, 5, 1, 1)

        self.setCentralWidget(self.centralwidget)

    def setImage(self, path):
        pixmap = QPixmap(path)
        pixmap.scaled(self.immagine.width(), self.immagine.height(), QtCore.Qt.KeepAspectRatio)
        self.immagine.setPixmap(pixmap)

    def autoresizeImage(self):
        pixmap = self.immagine.pixmap().scaled(self.immagine.width(), self.immagine.height(), QtCore.Qt.KeepAspectRatio)
        self.immagine.setPixmap(pixmap)
