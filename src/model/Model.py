import sys

from pathlib import Path
from PIL import Image, ExifTags


class Model:
    def __init__(self):
        self.currentImage = Path(sys.argv[1])
        self._updateEXIFData()

        self.imagesList = sorted(self.currentImage.parent.glob("*.jpg"))
        self.imagesIterator = BidirectionalIterator(self.imagesList, self.imagesList.index(self.currentImage))

    def getPreviousImage(self) -> Path:
        self.currentImage = self.imagesIterator.prev()
        self._updateEXIFData()
        return self.currentImage

    def getNextImage(self) -> Path:
        self.currentImage = self.imagesIterator.next()
        self._updateEXIFData()
        return self.currentImage

    def _updateEXIFData(self):
        imageWithEXIF = Image.open(self.currentImage)
        self.currentEXIFData = {ExifTags.TAGS[k]: v for k, v in imageWithEXIF._getexif().items() if k in ExifTags.TAGS}
        if self.currentEXIFData["GPSInfo"] is not None:
            self.currentEXIFData["GPSInfo"] = {ExifTags.GPSTAGS[k]: v for k, v in
                                               self.currentEXIFData["GPSInfo"].items() if k in ExifTags.GPSTAGS}


class BidirectionalIterator:
    def __init__(self, actualList: list, currentIndex: int):
        self.list = actualList
        self.index = currentIndex

    def next(self):
        self.index = (self.index + 1) % len(self.list)
        return self.list[self.index]

    def prev(self):
        self.index = (self.index - 1) % len(self.list)
        return self.list[self.index]

    def __iter__(self):
        return self
