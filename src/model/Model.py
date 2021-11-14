import sys

from pathlib import Path


class Model:
    def __init__(self):
        self.currentImage = Path(sys.argv[1])

        self.imagesList = sorted(self.currentImage.parent.glob("*.jpg"))
        self.imagesIterator = BidirectionalIterator(self.imagesList, self.imagesList.index(self.currentImage))

    def getPreviousImage(self) -> Path:
        return self.imagesIterator.prev()

    def getNextImage(self) -> Path:
        return self.imagesIterator.next()


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
