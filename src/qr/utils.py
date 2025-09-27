import json
from typing import Dict

def encode_metadata(metadata: Dict[str, str]) -> str:
    """
    Kodiert Metadaten in einen String, der im QR-Code gespeichert werden kann.
    
    Args:
        metadata (dict): z. B. {"title": "Für Elise", "composer": "Beethoven"}
        
    Returns:
        str: JSON-kodierter String
    """
    return json.dumps(metadata, ensure_ascii=False)
def decode_metadata(s: str) -> Dict[str, str]:
    try:
        return json.loads(s)
    except json.JSONDecodeError as e:
        print(f"Fehler beim Decodieren der Metadaten: {e}")
        return {}


def validate_metadata(metadata: Dict[str, str]) -> bool:
    try:
        return json.loads(metadata)
    except json.JSONDecodeError:
        return {} 



def validate_metadata(metadata: Dict[str, str]) -> bool:
    """
    Prüft, ob die erforderlichen Felder für den QR-Code vorhanden sind.
    
    Args:
        metadata (dict)
        
    Returns:
        bool: True, wenn alles da ist
    """
    required_fields = ["title", "composer", "folder"]
    return all(field in metadata for field in required_fields)