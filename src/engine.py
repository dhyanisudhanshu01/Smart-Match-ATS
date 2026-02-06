import pdfplumber
from sentence_transformers import SentenceTransformer,util
from dotenv import load_dotenv
import os
import re
import google.generativeai as genai   

# Load the pre-trained SentenceTransformer model
load_dotenv()  # Load environment variables from .env file
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

gemini_model = genai.GenerativeModel("gemini-2.5-flash")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def normalize_text(text):

    text = text.lower()

    text = text.replace("\n", " ").replace("\t", " ")

    text = re.sub(r"[^a-z0-9\s]", " ", text)

    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()
    words = [w for w in words if len(w) > 2]

    return " ".join(words)

def extract_text_from_pdf(file):
    #extract text from a PDF file

    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.strip()


def compute_similarity(resumetext, jobdescription):
    # Compute the cosine similarity between two texts

    # Encode the texts into embeddings
    jobdescription = normalize_text(jobdescription)

    resumetext = normalize_text(resumetext)

    embeddings = embedding_model.encode([resumetext, jobdescription], convert_to_tensor=True)

    # Compute cosine similarity
    similarity = util.cos_sim(embeddings[0], embeddings[1])[0][0]

    return float(similarity * 100)

def gemini_gap_analysis(resume_text, job_description):
    # Use Gemini to analyze the gap between resume and job description

    prompt = f"""
    You are an ATS system.

    Compare the following Resume and Job Description.

    Tasks:
    1. List missing skills.
    2. Suggest resume improvements.
    3. Give short professional feedback.

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """

    response = gemini_model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    pdf_path = "data/sample_resume.pdf"  # Replace with your PDF file path
    extracted_text = extract_text_from_pdf(pdf_path)
    jd_text = "We are looking for a motivated Accounting & Audit Fresher to support day-to-day accounting activities and assist in audit assignments. The candidate will gain hands-on exposure to bookkeeping, financial records, and compliance processes."
    print("Matching Score:", compute_similarity(extracted_text, jd_text))
    print("\nGemini Feedback:\n")
    print(gemini_gap_analysis(extracted_text, jd_text))