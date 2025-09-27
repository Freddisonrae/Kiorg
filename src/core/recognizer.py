import cv2
from pyzbar.pyzbar import decode
from typing import List, Dict

def recognize_qr(image_path: str) -> List[Dict]:
    """
    Liest Qr-Codes aus einem Bild und gibt die Inhalte zurück.

    Args: image_path (str)

    Returns: 
            List[Dict]: Liste mit Infos pro gefunden Qr-Code
    """
    image = cv2.imread(image_path)
    decoded_objects = decode(image)


    results = []
    for obj in decoded_objects:
        results.append({
            "data": obj.data.encode("utf-8"),
            "type": obj.type,
            "rect": obj.rect
        })
    return results

if __name__ == "__main__":
    results = recognize_qr("test_qr.png")
    print("Gefundene-Qr-Codes")



