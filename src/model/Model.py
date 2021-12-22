import re
import sys

from pathlib import Path
from PIL import Image, ExifTags


class Model:
    def __init__(self):
        """
        Inizializza il modello recuperando i tag EXIF dell'immagine e creando una lista delle immagini JPEG contenute nella directory dell'immagine attualmente in uso.
        """
        self.currentImage = Path(sys.argv[1])  # percorso dell'immagine passata come parametro da riga di comando
        self._updateEXIFData()

        self.imagesList = sorted(self.currentImage.parent.glob("*.jpg"))
        self.imagesIterator = BidirectionalIterator(self.imagesList, self.imagesList.index(self.currentImage))

    def getPreviousImage(self) -> Path:
        """
        Imposta come immagine corrente l'immagine precedente e ne carica i dati EXIF.
        :return: Percorso dell'immagine precedente.
        """
        self.currentImage = self.imagesIterator.prev()
        self._updateEXIFData()
        return self.currentImage

    def getNextImage(self) -> Path:
        """
        Imposta come immagine corrente l'immagine successiva e ne carica i dati EXIF.
        :return: Percorso dell'immagine successiva.
        """
        self.currentImage = self.imagesIterator.next()
        self._updateEXIFData()
        return self.currentImage

    def _updateEXIFData(self):
        """
        Aggiorna il dizionario contenente i tag EXIF dell'immagine corrente. I dati GPS vengono trattati a parte e convertiti sia in DMS che DD.
        """
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
                longDD, latDD = _parseDMS(self.currentEXIFData["GPS Coordinates (DMS)"])
                self.currentEXIFData["GPS Coordinates (DD)"] = str(longDD) + ", " + str(latDD)

            self.currentEXIFData.update(gpsinfo)
            self.currentEXIFData.pop("GPSInfo")


# Realizza l'iteratore circolare per scorrere le immagini
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


# Funzione di utilità per la gestione dei dati GPS
def _dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes) / 60 + float(seconds) / (60 * 60)
    if direction == 'S' or direction == 'W':
        dd *= -1
    return dd


# Funzione di utilità per la gestione dei dati GPS
def _parseDMS(dms):
    parts = re.split('[°\' "]', dms)
    lat = _dms2dd(parts[0], parts[1], parts[2], parts[3])
    lng = _dms2dd(parts[4], parts[5], parts[6], parts[7])
    return lat, lng
