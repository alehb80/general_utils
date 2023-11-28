import base64
import io

import pdf2image


def pdf_to_base64_images(pdf_file):
    """
    Converte un PDF in una lista di immagini base64.

    Args:
      pdf_file: Il percorso del file PDF da convertire.

    Returns:
      Una lista di stringhe base64, ognuna delle quali rappresenta una pagina del PDF.
    """

    with open(pdf_file, "rb") as f:
        pdf = pdf2image.convert_from_bytes(f.read())

    base64_images = []
    for page in pdf:
        buf = io.BytesIO()
        page.save(buf, format="PNG")
        base64_images.append(base64.b64encode(buf.getvalue()).decode())

    return base64_images


if __name__ == '__main__':
    # Esempio di utilizzo
    pdf_file = "../Resources/attention_is_all_you_need.pdf"
    base64_images = pdf_to_base64_images(pdf_file)

    # Stampa la lista delle immagini base64
    for base64_image in base64_images:
        print(base64_image)
