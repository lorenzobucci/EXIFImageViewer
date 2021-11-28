from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QLabel, QWidget, QSizePolicy


class ImageWidget(QLabel):
    imageResized = pyqtSignal()

    def __init__(self, parent: QWidget):
        super().__init__(parent)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setAlignment(Qt.AlignCenter)
        self.setObjectName("immagine")

    def resizeEvent(self, a0: QResizeEvent) -> None:
        super(ImageWidget, self).resizeEvent(a0)
        self.imageResized.emit()
