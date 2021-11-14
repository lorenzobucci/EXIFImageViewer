import sys

from src.view.ImageViewer import ImageViewer


class Controller:
    def __init__(self, imageViewer: ImageViewer):
        self.imageViewer = imageViewer

        self.imageViewer.imageResized.connect(self.imageResizedHandler)
        self.imageViewer.bottoneRuotaAntiorario.clicked.connect(self.bottoneRuotaAntiorarioHandler)
        self.imageViewer.bottoneRuotaOrario.clicked.connect(self.bottoneRuotaOrarioHandler)

        self.imageViewer.setImage(sys.argv[1])

    def imageResizedHandler(self):
        self.imageViewer.autoresizeImage()

    def bottoneRuotaAntiorarioHandler(self):
        self.imageViewer.rotateImage(-90)

    def bottoneRuotaOrarioHandler(self):
        self.imageViewer.rotateImage(90)