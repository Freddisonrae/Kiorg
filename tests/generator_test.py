from qr import generator
def test_generateqr():
    test_metadata = {
        "title": "Für Elise",
        "composer": "Beethoven",
        "year": "1810"
    }
    generator.generate_qr(test_metadata, output_file="test_qr.png")

test_generateqr()