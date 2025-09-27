
from .utils import encode_metadata
import os
import qrcode
from PIL import Image

def generate_qr(metadata: dict, output_file: str = None) -> Image.Image:
    """
    Erzeugt einen QR-Code aus Metadaten und speichert ihn in Qr_temp
    (neben der Skriptdatei).

    Args:
        metadata (dict): z.B. {"title": "Für Elise", "composer": "Beethoven"}
        output_file (str, optional): Dateiname zum Speichern im Ordner Qr_temp.
                                     Falls None, wird automatisch ein Name erzeugt.

    Returns:
        PIL.Image.Image: QR-Code Bildobjekt
    """
    qr_data = encode_metadata(metadata)  # <- deine Funktion für Daten-Encoding

    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Ordner relativ zum Skriptpfad
    script_dir = os.path.dirname(os.path.abspath(__file__))
    temp_folder = os.path.join(script_dir, "Qr_temp")

    # Sicherstellen, dass Ordner existiert (falls noch nicht angelegt)
    os.makedirs(temp_folder, exist_ok=True)

    if output_file is None:
        # Automatischen Dateinamen bauen
        title = metadata.get("title", "qr").replace(" ", "_")
        composer = metadata.get("composer", "").replace(" ", "_")
        filename = f"{title}_{composer}.png" if composer else f"{title}.png"
        output_file = filename

    # Vollständiger Pfad im Qr_temp-Ordner
    output_path = os.path.join(temp_folder, output_file)

    img.save(output_path)
    print(f"QR-Code gespeichert in {output_path}")

    return img


