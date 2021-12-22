# Visualizzatore Immagini & EXIF

**Mini-elaborato per il corso di Human Computer Interaction 2021/2022**

L'elaborato consiste nello sviluppo di un visualizzatore d'immagini JPEG e dei relativi tag EXIF secondo i requisiti
richiesti dall'assegnamento.

Sono state sviluppate anche le funzionalità aggiuntive di geolocalizzazione e di navigazione tra immagini di una stessa
directory.

L'intero progetto è stato scritto in Python 3.9 mediante l'uso del framework PyQt5.

## Eseguire il programma

Per lanciare l'applicazione è necessario eseguire da riga di comando lo script *main.py* della cartella *src*. **È
obbligatorio** specificare come parametro il percorso dell'immagine da visualizzare.

Ad esempio:

```console
python3 src/main.py "../sampleImages/sample.jpg"
```

Eseguendo questo comando si visualizzerà l'immagine *sample.jpg* contenuta nella cartella *sampleImages* di questa
repository. Dopodiché sarà possibile switchare la visualizzazione tra le immagini della directory grazie
all'uso dei bottoni direzionali presenti nell'interfaccia utente.