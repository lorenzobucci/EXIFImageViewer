from src.view.ImageViewer import ImageViewer


class Controller(object):
    def __init__(self, imageViewer: ImageViewer):
        self.imageViewer = imageViewer
        self.imageViewer.windowResized.connect(self.windowResizedHandler)

    def windowResizedHandler(self):
        self.imageViewer.autoresizeImage()
