import sys

from src.view.ImageViewer import ImageViewer


class Controller(object):
    def __init__(self, imageViewer: ImageViewer):
        self.imageViewer = imageViewer
        self.imageViewer.imageResized.connect(self.windowResizedHandler)
        self.imageViewer.setImage(sys.argv[1])

    def windowResizedHandler(self):
        self.imageViewer.autoresizeImage()
