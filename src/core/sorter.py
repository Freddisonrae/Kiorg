import recognizer
import os
from typing import Dict
from..qr import utils
"""
Diese Datei soll den Qr Code löschen nachdem die Informationen herausgelesen worden sind.
Dabei soll sie auf die Funktionen encode_metadata zurückgreifen und die Funktion recognizer um die Informationen auszulesen.
Danach soll sie je nach Information, das Notenblatt passend in die Datenbank einordnen und anschließend den passenden Platz zurückgeben
""" 
def inf_Auslesen(inf: Dict[str, str]) -> str:
  #  img = Dateipfad des temporären Qr_Codes

    return 