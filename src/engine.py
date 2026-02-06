import pdfplumber

def extract_text_from_pdf(pdf_path):
    #extract text from a PDF file

    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.strip()

if __name__ == "__main__":
    pdf_path = "data/sample_resume.pdf"  # Replace with your PDF file path
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)