from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon, QKeySequence
from PyQt5.QtWidgets import QStyle


class ImageViewer(QtWidgets.QMainWindow):
    pixmap = None

    imageResized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setObjectName("ImageViewer")
        self.resize(1020, 620)
        self.setMinimumHeight(200)
        self.setWindowTitle("Visualizzatore immagini & EXIF")

        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.immagine = ImageWidget(self.centralWidget)
        self.immagine.imageResized.connect(lambda: self.imageResized.emit())
        self.gridLayout.addWidget(self.immagine, 0, 0, 1, 7)

        spacerSx = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerSx, 1, 0, 1, 1)

        spacerDx = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerDx, 1, 6, 1, 1)

        self.bottoneTagEXIF = QtWidgets.QPushButton(self.centralWidget)
        self.bottoneTagEXIF.setMinimumSize(QSize(50, 50))
        self.bottoneTagEXIF.setMaximumSize(QSize(50, 50))
        self.bottoneTagEXIF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bottoneTagEXIF.setObjectName("BottoneTagEXIF")
        self.bottoneTagEXIF.setToolTip("Visualizza tag EXIF")
        self.bottoneTagEXIF.setIcon(self.bottoneTagEXIF.style().standardIcon(QStyle.SP_MessageBoxInformation))
        self.bottoneTagEXIF.setIconSize(QSize(24, 24))
        self.gridLayout.addWidget(self.bottoneTagEXIF, 1, 1, 1, 1)

        self.bottoneImmaginePrecedente = QtWidgets.QPushButton(self.centralWidget)
        self.bottoneImmaginePrecedente.setMinimumSize(QSize(50, 50))
        self.bottoneImmaginePrecedente.setMaximumSize(QSize(50, 50))
        self.bottoneImmaginePrecedente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bottoneImmaginePrecedente.setObjectName("BottoneImmaginePrecedente")
        self.bottoneImmaginePrecedente.setToolTip("Immagine precedente")
        self.bottoneImmaginePrecedente.setIcon(self.bottoneImmaginePrecedente.style().standardIcon(QStyle.SP_ArrowLeft))
        self.bottoneImmaginePrecedente.setIconSize(QSize(24, 24))
        self.bottoneImmaginePrecedente.setShortcut(QKeySequence.MoveToPreviousChar)
        self.gridLayout.addWidget(self.bottoneImmaginePrecedente, 1, 2, 1, 1)

        self.bottoneImmagineSuccessiva = QtWidgets.QPushButton(self.centralWidget)
        self.bottoneImmagineSuccessiva.setMinimumSize(QSize(50, 50))
        self.bottoneImmagineSuccessiva.setMaximumSize(QSize(50, 50))
        self.bottoneImmagineSuccessiva.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bottoneImmagineSuccessiva.setObjectName("BottoneImmagineSuccessiva")
        self.bottoneImmagineSuccessiva.setToolTip("Immagine successiva")
        self.bottoneImmagineSuccessiva.setIcon(
            self.bottoneImmagineSuccessiva.style().standardIcon(QStyle.SP_ArrowRight))
        self.bottoneImmagineSuccessiva.setIconSize(QSize(24, 24))
        self.bottoneImmagineSuccessiva.setShortcut(QKeySequence.MoveToNextChar)
        self.gridLayout.addWidget(self.bottoneImmagineSuccessiva, 1, 3, 1, 1)

        self.bottoneRuotaAntiorario = QtWidgets.QPushButton(self.centralWidget)
        self.bottoneRuotaAntiorario.setMinimumSize(QSize(50, 50))
        self.bottoneRuotaAntiorario.setMaximumSize(QSize(50, 50))
        self.bottoneRuotaAntiorario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bottoneRuotaAntiorario.setObjectName("BottoneRuotaAntiorario")
        self.bottoneRuotaAntiorario.setToolTip("Ruota immagine in senso antiorario (CTRL+,)")
        iconaAntiorario = QIcon()
        iconaAntiorario.addFile(u"res/icons/rotate_left_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bottoneRuotaAntiorario.setIconSize(QSize(24, 24))
        self.bottoneRuotaAntiorario.setIcon(iconaAntiorario)
        self.bottoneRuotaAntiorario.setShortcut(QKeySequence("Ctrl+,"))
        self.gridLayout.addWidget(self.bottoneRuotaAntiorario, 1, 4, 1, 1)

        self.bottoneRuotaOrario = QtWidgets.QPushButton(self.centralWidget)
        self.bottoneRuotaOrario.setMinimumSize(QSize(50, 50))
        self.bottoneRuotaOrario.setMaximumSize(QSize(50, 50))
        self.bottoneRuotaOrario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        transform = QtGui.QTransform().rotate(degrees)
        self.pixmap = self.pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
        self.autoresizeImage()

    def autoresizeImage(self):
        self.immagine.setPixmap(
            self.pixmap.scaled(self.immagine.width(), self.immagine.height(), QtCore.Qt.KeepAspectRatio))


class ImageWidget(QtWidgets.QLabel):
    imageResized = QtCore.pyqtSignal()

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setObjectName("immagine")

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        super(ImageWidget, self).resizeEvent(a0)
        self.imageResized.emit()
