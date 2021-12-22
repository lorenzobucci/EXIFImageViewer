import sys

from pathlib import Path

from model.Model import Model
from view.EXIFDialog import EXIFDialog
from view.ImageViewer import ImageViewer


class Controller:
    def __init__(self, imageViewer: ImageViewer, model: Model):
        self.imageViewer = imageViewer
        self.model = model

        self.imageViewer.imageResized.connect(self.imageResizedHandler)
        self.imageViewer.tagEXIFBtn.clicked.connect(self.tagEXIFBtnHandler)
        self.imageViewer.prevImageBtn.clicked.connect(self.prevImageBtnHandler)
        self.imageViewer.nextImageBtn.clicked.connect(self.nextImageBtnHandler)
        self.imageViewer.antiCwRotateBtn.clicked.connect(self.antiCwRotateBtnHandler)
        self.imageViewer.cwRotateButton.clicked.connect(self.cwRotateButtonHandler)

        imagePath = Path(sys.argv[1])
        self.imageViewer.setImage(str(imagePath))
        self.imageViewer.addFilenameToWindowTitle(imagePath.name)

    def imageResizedHandler(self):
        self.imageViewer.autoresizeImage()

    def tagEXIFBtnHandler(self):
        exifDialog = EXIFDialog(self.model.currentEXIFData)
        exifDialog.exec()

    def prevImageBtnHandler(self):
        imagePath = self.model.getPreviousImage()
        self.imageViewer.setImage(str(imagePath))
        self.imageViewer.addFilenameToWindowTitle(imagePath.name)

    def nextImageBtnHandler(self):
        imagePath = self.model.getNextImage()
        self.imageViewer.setImage(str(imagePath))
        self.imageViewer.addFilenameToWindowTitle(imagePath.name)

    def antiCwRotateBtnHandler(self):
        self.imageViewer.rotateImage(-90)

    def cwRotateButtonHandler(self):
        self.imageViewer.rotateImage(90)
