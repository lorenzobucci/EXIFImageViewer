from PyQt5.QtCore import Qt, QVariant, QAbstractTableModel

headers = ["Tag", "Valore"]


class QEXIFModel(QAbstractTableModel):
    def __init__(self, exifDict: dict):
        super().__init__()
        self.exifDict = exifDict

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.exifDict)

    def columnCount(self, parent=None, *args, **kwargs):
        return len(headers)

    def data(self, modelIndex, role=None):
        if role != Qt.DisplayRole or not modelIndex.isValid():
            return QVariant()
        return str(sorted(self.exifDict.items())[modelIndex.row()][modelIndex.column()])

    def headerData(self, p_int, Qt_Orientation, role=None):
        if role != Qt.DisplayRole or Qt_Orientation != Qt.Horizontal:
            return QVariant()
        return headers[p_int]
