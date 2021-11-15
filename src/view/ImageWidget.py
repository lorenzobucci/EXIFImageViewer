from PyQt5 import QtWidgets, QtCore, QtGui


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
