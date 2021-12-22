import sys

from pathlib import Path

from model.Model import Model
from view.EXIFDialog import EXIFDialog
from view.ImageViewer import ImageViewer


class Controller:
    def __init__(self, imageViewer: ImageViewer, model: Model):
        """
        Inizializza il Controller connettendo gli eventi della view ai loro handler e imposta sulla view l'immagine iniziale da visualizzare.
        """
        self.imageViewer = imageViewer
        self.model = model

        self.imageViewer.imageResized.connect(self._imageResizedHandler)
        self.imageViewer.tagEXIFBtn.clicked.connect(self._tagEXIFBtnHandler)
        self.imageViewer.prevImageBtn.clicked.connect(self._prevImageBtnHandler)
        self.imageViewer.nextImageBtn.clicked.connect(self._nextImageBtnHandler)
        self.imageViewer.antiCwRotateBtn.clicked.connect(self._antiCwRotateBtnHandler)
        self.imageViewer.cwRotateButton.clicked.connect(self._cwRotateButtonHandler)

        imagePath = Path(sys.argv[1])  # percorso dell'immagine passata come parametro da riga di comando
        self.imageViewer.setImage(str(imagePath))
        self.imageViewer.addFilenameToWindowTitle(imagePath.name)

    def _imageResizedHandler(self):
        """
        Notifica alla view che il widget contenente l'immagine è stato ridimensionato e conseguentemente l'immagine deve essere scalata opportunamente.
        """
        self.imageViewer.autoresizeImage()

    def _tagEXIFBtnHandler(self):
        """
        Preleva dal modello i dati EXIF e mostra il dialogo per la loro visualizzazione.
        """
        exifDialog = EXIFDialog(self.model.currentEXIFData)
        exifDialog.exec()

    def _prevImageBtnHandler(self):
        """
        Preleva dal modello l'immagine precedente e la imposta sulla view.
        """
        imagePath = self.model.getPreviousImage()
        self.imageViewer.setImage(str(imagePath))
        self.imageViewer.addFilenameToWindowTitle(imagePath.name)

    def _nextImageBtnHandler(self):
        """
        Preleva dal modello l'immagine successiva e la imposta sulla view.
        """
        imagePath = self.model.getNextImage()
        self.imageViewer.setImage(str(imagePath))
        self.imageViewer.addFilenameToWindowTitle(imagePath.name)

    def _antiCwRotateBtnHandler(self):
        """
        Ruota di 90° in senso antiorario l'immagine.
        """
        self.imageViewer.rotateImage(-90)

    def _cwRotateButtonHandler(self):
        """
        Ruota di 90° in senso orario l'immagine.
        """
        self.imageViewer.rotateImage(90)
