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

        self.image = ImageWidget(self.centralWidget)
        self.image.imageResized.connect(lambda: self.imageResized.emit())
        self.gridLayout.addWidget(self.image, 0, 0, 1, 7)

        leftSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(leftSpacer, 1, 0, 1, 1)

        rightSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(rightSpacer, 1, 6, 1, 1)

        self.tagEXIFBtn = QPushButton(self.centralWidget)
        self.tagEXIFBtn.setMinimumSize(QSize(50, 50))
        self.tagEXIFBtn.setMaximumSize(QSize(50, 50))
        self.tagEXIFBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.tagEXIFBtn.setObjectName("BottoneTagEXIF")
        self.tagEXIFBtn.setToolTip("Visualizza tag EXIF")
        self.tagEXIFBtn.setIcon(self.tagEXIFBtn.style().standardIcon(QStyle.SP_MessageBoxInformation))
        self.tagEXIFBtn.setIconSize(QSize(24, 24))
        self.gridLayout.addWidget(self.tagEXIFBtn, 1, 1, 1, 1)

        self.prevImageBtn = QPushButton(self.centralWidget)
        self.prevImageBtn.setMinimumSize(QSize(50, 50))
        self.prevImageBtn.setMaximumSize(QSize(50, 50))
        self.prevImageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prevImageBtn.setObjectName("BottoneImmaginePrecedente")
        self.prevImageBtn.setToolTip("Immagine precedente")
        self.prevImageBtn.setIcon(self.prevImageBtn.style().standardIcon(QStyle.SP_ArrowLeft))
        self.prevImageBtn.setIconSize(QSize(24, 24))
        self.prevImageBtn.setShortcut(QKeySequence.MoveToPreviousChar)
        self.gridLayout.addWidget(self.prevImageBtn, 1, 2, 1, 1)

        self.nextImageBtn = QPushButton(self.centralWidget)
        self.nextImageBtn.setMinimumSize(QSize(50, 50))
        self.nextImageBtn.setMaximumSize(QSize(50, 50))
        self.nextImageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.nextImageBtn.setObjectName("BottoneImmagineSuccessiva")
        self.nextImageBtn.setToolTip("Immagine successiva")
        self.nextImageBtn.setIcon(
            self.nextImageBtn.style().standardIcon(QStyle.SP_ArrowRight))
        self.nextImageBtn.setIconSize(QSize(24, 24))
        self.nextImageBtn.setShortcut(QKeySequence.MoveToNextChar)
        self.gridLayout.addWidget(self.nextImageBtn, 1, 3, 1, 1)

        self.antiCwRotateBtn = QPushButton(self.centralWidget)
        self.antiCwRotateBtn.setMinimumSize(QSize(50, 50))
        self.antiCwRotateBtn.setMaximumSize(QSize(50, 50))
        self.antiCwRotateBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.antiCwRotateBtn.setObjectName("BottoneRuotaAntiorario")
        self.antiCwRotateBtn.setToolTip("Ruota immagine in senso antiorario (CTRL+,)")
        antiCwIcon = QIcon()
        antiCwIcon.addFile(_resourcePath("res/icons/rotate_left_black_24dp.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.antiCwRotateBtn.setIconSize(QSize(24, 24))
        self.antiCwRotateBtn.setIcon(antiCwIcon)
        self.antiCwRotateBtn.setShortcut(QKeySequence("Ctrl+,"))
        self.gridLayout.addWidget(self.antiCwRotateBtn, 1, 4, 1, 1)

        self.cwRotateButton = QPushButton(self.centralWidget)
        self.cwRotateButton.setMinimumSize(QSize(50, 50))
        self.cwRotateButton.setMaximumSize(QSize(50, 50))
        self.cwRotateButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cwRotateButton.setObjectName("BottoneRuotaOrario")
        self.cwRotateButton.setToolTip("Ruota immagine in senso orario (CTRL+.)")
        cwIcon = QIcon()
        cwIcon.addFile(_resourcePath("res/icons/rotate_right_black_24dp.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.cwRotateButton.setIcon(cwIcon)
        self.cwRotateButton.setIconSize(QSize(24, 24))
        self.cwRotateButton.setShortcut(QKeySequence("Ctrl+."))
        self.gridLayout.addWidget(self.cwRotateButton, 1, 5, 1, 1)

        self.setCentralWidget(self.centralWidget)

    def setImage(self, path):
        self.pixmap = QPixmap(path)
        self.autoresizeImage()

    def rotateImage(self, degrees):
        transform = QTransform().rotate(degrees)
        self.pixmap = self.pixmap.transformed(transform, Qt.SmoothTransformation)
        self.autoresizeImage()

    def autoresizeImage(self):
        self.image.setPixmap(
            self.pixmap.scaled(self.image.width(), self.image.height(), Qt.KeepAspectRatio))

    def addFilenameToWindowTitle(self, filename):
        self.setWindowTitle("Visualizzatore immagini & EXIF - " + filename)


def _resourcePath(relativePath):
    try:
        basePath = Path(sys._MEIPASS)
    except Exception:
        basePath = Path(".").absolute()

    return str(Path.joinpath(basePath, relativePath).absolute())
