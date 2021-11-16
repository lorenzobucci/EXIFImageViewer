from PyQt5.QtCore import *

headers = ["Tag", "Valore"]


class QEXIFModel(QAbstractTableModel):
    def __init__(self, exifDict: dict):
        super().__init__()
        self.exifDict = exifDict

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.exifDict)

    def columnCount(self, parent=None, *args, **kwargs):
        return len(headers)

    def data(self, QModelIndex, role=None):
        if role != Qt.DisplayRole or not QModelIndex.isValid():
            return QVariant()
        return str(sorted(self.exifDict.items())[QModelIndex.row()][QModelIndex.column()])

    def headerData(self, p_int, Qt_Orientation, role=None):
        if role != Qt.DisplayRole or Qt_Orientation != Qt.Horizontal:
            return QVariant()
        return headers[p_int]
