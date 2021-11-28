import sys
from pathlib import Path

from PyQt5.QtCore import QSize, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QIcon, QKeySequence, QCursor, QTransform
from PyQt5.QtWidgets import QStyle, QMainWindow, QWidget, QGridLayout, QSpacerItem, QSizePolicy, QPushButton

from view.ImageWidget import ImageWidget


class ImageViewer(QMainWindow):
    pixmap = None

    imageResized = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setObjectName("ImageViewer")
        self.resize(1020, 620)
        self.setMinimumHeight(200)

        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("centralWidget")

        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.immagine = ImageWidget(self.centralWidget)
        self.immagine.imageResized.connect(lambda: self.imageResized.emit())
        self.gridLayout.addWidget(self.immagine, 0, 0, 1, 7)

        spacerSx = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerSx, 1, 0, 1, 1)

        spacerDx = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerDx, 1, 6, 1, 1)

        self.bottoneTagEXIF = QPushButton(self.centralWidget)
        self.bottoneTagEXIF.setMinimumSize(QSize(50, 50))
        self.bottoneTagEXIF.setMaximumSize(QSize(50, 50))
        self.bottoneTagEXIF.setCursor(QCursor(Qt.PointingHandCursor))
        self.bottoneTagEXIF.setObjectName("BottoneTagEXIF")
        self.bottoneTagEXIF.setToolTip("Visualizza tag EXIF")
        self.bottoneTagEXIF.setIcon(self.bottoneTagEXIF.style().standardIcon(QStyle.SP_MessageBoxInformation))
        self.bottoneTagEXIF.setIconSize(QSize(24, 24))
        self.gridLayout.addWidget(self.bottoneTagEXIF, 1, 1, 1, 1)

        self.bottoneImmaginePrecedente = QPushButton(self.centralWidget)
        self.bottoneImmaginePrecedente.setMinimumSize(QSize(50, 50))
        self.bottoneImmaginePrecedente.setMaximumSize(QSize(50, 50))
        self.bottoneImmaginePrecedente.setCursor(QCursor(Qt.PointingHandCursor))
        self.bottoneImmaginePrecedente.setObjectName("BottoneImmaginePrecedente")
        self.bottoneImmaginePrecedente.setToolTip("Immagine precedente")
        self.bottoneImmaginePrecedente.setIcon(self.bottoneImmaginePrecedente.style().standardIcon(QStyle.SP_ArrowLeft))
        self.bottoneImmaginePrecedente.setIconSize(QSize(24, 24))
        self.bottoneImmaginePrecedente.setShortcut(QKeySequence.MoveToPreviousChar)
        self.gridLayout.addWidget(self.bottoneImmaginePrecedente, 1, 2, 1, 1)

        self.bottoneImmagineSuccessiva = QPushButton(self.centralWidget)
        self.bottoneImmagineSuccessiva.setMinimumSize(QSize(50, 50))
        self.bottoneImmagineSuccessiva.setMaximumSize(QSize(50, 50))
        self.bottoneImmagineSuccessiva.setCursor(QCursor(Qt.PointingHandCursor))
        self.bottoneImmagineSuccessiva.setObjectName("BottoneImmagineSuccessiva")
        self.bottoneImmagineSuccessiva.setToolTip("Immagine successiva")
        self.bottoneImmagineSuccessiva.setIcon(
            self.bottoneImmagineSuccessiva.style().standardIcon(QStyle.SP_ArrowRight))
        self.bottoneImmagineSuccessiva.setIconSize(QSize(24, 24))
        self.bottoneImmagineSuccessiva.setShortcut(QKeySequence.MoveToNextChar)
        self.gridLayout.addWidget(self.bottoneImmagineSuccessiva, 1, 3, 1, 1)

        self.bottoneRuotaAntiorario = QPushButton(self.centralWidget)
        self.bottoneRuotaAntiorario.setMinimumSize(QSize(50, 50))
        self.bottoneRuotaAntiorario.setMaximumSize(QSize(50, 50))
        self.bottoneRuotaAntiorario.setCursor(QCursor(Qt.PointingHandCursor))
        self.bottoneRuotaAntiorario.setObjectName("BottoneRuotaAntiorario")
        self.bottoneRuotaAntiorario.setToolTip("Ruota immagine in senso antiorario (CTRL+,)")
        iconaAntiorario = QIcon()
        iconaAntiorario.addFile(u"res/icons/rotate_left_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bottoneRuotaAntiorario.setIconSize(QSize(24, 24))
        self.bottoneRuotaAntiorario.setIcon(iconaAntiorario)
        self.bottoneRuotaAntiorario.setShortcut(QKeySequence("Ctrl+,"))
        self.gridLayout.addWidget(self.bottoneRuotaAntiorario, 1, 4, 1, 1)

        self.bottoneRuotaOrario = QPushButton(self.centralWidget)
        self.bottoneRuotaOrario.setMinimumSize(QSize(50, 50))
        self.bottoneRuotaOrario.setMaximumSize(QSize(50, 50))
        self.bottoneRuotaOrario.setCursor(QCursor(Qt.PointingHandCursor))
        self.bottoneRuotaOrario.setObjectName("BottoneRuotaOrario")
        self.bottoneRuotaOrario.setToolTip("Ruota immagine in senso orario (CTRL+.)")
        iconaOrario = QIcon()
        iconaOrario.addFile(u"res/icons/rotate_right_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bottoneRuotaOrario.setIcon(iconaOrario)
        self.bottoneRuotaOrario.setIconSize(QSize(24, 24))
        self.bottoneRuotaOrario.setShortcut(QKeySequence("Ctrl+."))
        self.gridLayout.addWidget(self.bottoneRuotaOrario, 1, 5, 1, 1)

        self.setCentralWidget(self.centralWidget)

    def setImage(self, path):
        self.pixmap = QPixmap(path)
        self.autoresizeImage()

    def rotateImage(self, degrees):
        transform = QTransform().rotate(degrees)
        self.pixmap = self.pixmap.transformed(transform, Qt.SmoothTransformation)
        self.autoresizeImage()

    def autoresizeImage(self):
        self.immagine.setPixmap(
            self.pixmap.scaled(self.immagine.width(), self.immagine.height(), Qt.KeepAspectRatio))

    def addFilenameToWindowTitle(self, filename):
        self.setWindowTitle("Visualizzatore immagini & EXIF - " + filename)
