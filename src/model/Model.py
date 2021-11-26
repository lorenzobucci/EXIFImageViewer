import re
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
        if "GPSInfo" in self.currentEXIFData:
            gpsinfo = {ExifTags.GPSTAGS[k]: v for k, v in self.currentEXIFData["GPSInfo"].items() if
                       k in ExifTags.GPSTAGS}
            if "GPSLatitude" in gpsinfo and "GPSLongitude" in gpsinfo:
                latitudeStr = str(int(gpsinfo["GPSLatitude"][0])) + "°" + \
                              str(int(gpsinfo["GPSLatitude"][1])) + "\'" + \
                              str(gpsinfo["GPSLatitude"][2]) + "\"" + gpsinfo["GPSLatitudeRef"]
                longitudeStr = str(int(gpsinfo["GPSLongitude"][0])) + "°" + \
                               str(int(gpsinfo["GPSLongitude"][1])) + "\'" + \
                               str(gpsinfo["GPSLongitude"][2]) + "\"" + gpsinfo["GPSLongitudeRef"]
                self.currentEXIFData["GPS Coordinates (DMS)"] = latitudeStr + " " + longitudeStr
                longDD, latDD = parseDMS(self.currentEXIFData["GPS Coordinates (DMS)"])
                self.currentEXIFData["GPS Coordinates (DD)"] = str(longDD) + ", " + str(latDD)

            self.currentEXIFData.update(gpsinfo)
            self.currentEXIFData.pop("GPSInfo")


class BidirectionalIterator:
    def __init__(self, actualList: list, currentIndex: int):
        self._list = actualList
        self._index = currentIndex

    def next(self):
        self._index = (self._index + 1) % len(self._list)
        return self._list[self._index]

    def prev(self):
        self._index = (self._index - 1) % len(self._list)
        return self._list[self._index]

    def __iter__(self):
        return self


def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes) / 60 + float(seconds) / (60 * 60)
    if direction == 'S' or direction == 'W':
        dd *= -1
    return dd


def parseDMS(dms):
    parts = re.split('[°\' "]', dms)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])
    lng = dms2dd(parts[4], parts[5], parts[6], parts[7])

    return lat, lng
