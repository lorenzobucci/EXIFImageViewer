from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QLabel, QWidget, QSizePolicy


# Widget per la visualizzazione dell'immagine
class ImageWidget(QLabel):
    imageResized = pyqtSignal()

    def __init__(self, parent: QWidget):
        """
        Inizializza le dimensioni del widget.
        """
        super().__init__(parent)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setAlignment(Qt.AlignCenter)
        self.setObjectName("immagine")

    def resizeEvent(self, a0: QResizeEvent) -> None:
        """
        Emette il segnale imageResized quando le dimensioni del widget variano per eventi esterni.
        """
        super(ImageWidget, self).resizeEvent(a0)
        self.imageResized.emit()
