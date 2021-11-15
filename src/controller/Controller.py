import sys

from src.model import Model
from src.view.EXIFDialog import EXIFDialog
from src.view.ImageViewer import ImageViewer


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

        self.imageViewer.setImage(sys.argv[1])

    def imageResizedHandler(self):
        self.imageViewer.autoresizeImage()

    def bottoneTagEXIFHandler(self):
        exifDialog = EXIFDialog(self.model.currentEXIFData)
        exifDialog.exec()

    def bottoneImmaginePrecedenteHandler(self):
        self.imageViewer.setImage(str(self.model.getPreviousImage()))

    def bottoneImmagineSuccessivaHandler(self):
        self.imageViewer.setImage(str(self.model.getNextImage()))

    def bottoneRuotaAntiorarioHandler(self):
        self.imageViewer.rotateImage(-90)

    def bottoneRuotaOrarioHandler(self):
        self.imageViewer.rotateImage(90)
