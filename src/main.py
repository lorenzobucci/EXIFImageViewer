import sys

from PyQt5.QtWidgets import QApplication

from controller.Controller import Controller
from model.Model import Model
from view.ImageViewer import ImageViewer

app = QApplication(sys.argv)

# Inizializzazione modello, vista e relativo controller per dependency injection
model = Model()
mainWindow = ImageViewer()
controller = Controller(mainWindow, model)

# Lancio finestra principale PyQt
# Vengono passati i parametri ricevuti da riga di comando all'intera applicazione
mainWindow.show()
sys.exit(app.exec_())
