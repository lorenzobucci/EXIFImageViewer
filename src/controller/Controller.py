import sys

from pathlib import Path

from model import Model
from view.EXIFDialog import EXIFDialog
from view.ImageViewer import ImageViewer


class Controller:
    def __init__(self, imageViewer: ImageViewer, model: Model):
        self.imageViewer = imageViewer
        self.model = model

        self.imageViewer.imageResized.connect(self.imageResizedHandler)
        self.imageViewer.bottoneTagEXIF.clicked.connect(self.bottoneTagEXIFHandler)
        self.imageViewer.bottoneImmaginePrecedente.clicked.connect(self.bottoneImmaginePrecedenteHandler)
        self.imageViewer.bottoneImmagineSuccessiva.clicked.connect(self.bottoneImmagineSuccessivaHandler)
        self.imageViewer.bottoneRuotaAntiorario.clicked.connect(self.bottoneRuotaAntiorarioHandler)
        self.imageViewer.bottoneRuotaOrario.clicked.connect(self.bottoneRuotaOrarioHandler)

        imagePath = Path(sys.argv[1])
        self.imageViewer.setImage(str(imagePath))
        self.imageViewer.addFilenameToWindowTitle(imagePath.name)

    def imageResizedHandler(self):
        self.imageViewer.autoresizeImage()

    def bottoneTagEXIFHandler(self):
        exifDialog = EXIFDialog(self.model.currentEXIFData)
        exifDialog.exec()

    def bottoneImmaginePrecedenteHandler(self):
        imagePath = self.model.getPreviousImage()
        self.imageViewer.setImage(str(imagePath))
        self.imageViewer.addFilenameToWindowTitle(imagePath.name)

    def bottoneImmagineSuccessivaHandler(self):
        imagePath = self.model.getNextImage()
        self.imageViewer.setImage(str(imagePath))
        self.imageViewer.addFilenameToWindowTitle(imagePath.name)

    def bottoneRuotaAntiorarioHandler(self):
        self.imageViewer.rotateImage(-90)

    def bottoneRuotaOrarioHandler(self):
        self.imageViewer.rotateImage(90)
