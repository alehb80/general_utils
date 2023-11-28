import pypdf


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        pdf = pypdf.PdfReader(f)
        for page in pdf.pages:
            text += page.extract_text()
    return text


if __name__ == '__main__':
    file_path = "../resources/Pro_Labor.pdf"
    text = extract_text_from_pdf(pdf_path=file_path)

    print(text)
