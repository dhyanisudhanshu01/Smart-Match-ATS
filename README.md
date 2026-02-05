🚀 Smart-Match ATS — AI-Powered Resume Optimizer (Fully Free Stack)

Smart-Match ATS is a Generative AI–powered Applicant Tracking System designed to bridge the gap between job seekers and recruiters. Unlike traditional keyword-based screening tools, Smart-Match ATS uses semantic similarity and LLM reasoning to understand resumes in context — not just match exact keywords.

This project is built using a completely free technology stack, making it ideal for learning, experimentation, and portfolio demonstration.

🌟 Key Features

✅ Semantic Resume Matching
Uses local vector embeddings to compare meanings instead of keywords (e.g., “Deep Learning” ≈ “Neural Networks”).

✅ Instant Match Score
Calculates resume–job description similarity using Cosine Similarity.

✅ Skill Gap Analysis (Gemini AI)
Identifies missing skills and provides actionable resume improvement suggestions using Google Gemini (Free Tier).

✅ AI Resume Feedback
Generates personalized recommendations to better align resumes with job requirements.

✅ Interactive Web App
Streamlit-based UI for uploading resumes and job descriptions.

🛠️ Tech Stack (100% Free)
🔧 Core

🐍 Python 3.10+

🤖 AI / ML

📊 Scikit-Learn (Cosine Similarity)
🧠 Google Gemini API (Free Tier)

🧬 Embeddings

🔹 SentenceTransformers (MiniLM – local & free)

📝 NLP & Document Processing

📄 PyPDF2 / pdfplumber

🌐 Frontend

🎈 Streamlit

🔐 Configuration

🌱 python-dotenv

📁 Project Structure
├── data/               # Sample resumes and job descriptions
├── src/
│   ├── engine.py       # Embedding + similarity + Gemini prompts
│   └── app.py          # Streamlit application
├── requirements.txt    # Project dependencies
└── README.md

⚙️ How It Works

Extracts text from Resume & Job Description PDFs

Generates embeddings locally using SentenceTransformers

Computes similarity score via Cosine Similarity

Sends both texts to Gemini for skill-gap analysis

Displays match score + AI suggestions in Streamlit UI

▶️ Run Locally
git clone <repo-url>
cd smart-match-ats
pip install -r requirements.txt


Create .env file:

GEMINI_API_KEY=your_api_key_here


Run the app:

streamlit run src/app.py

🎯 Use Cases

Resume screening automation

Job–candidate matching

AI-powered career guidance

Data Science portfolio project

🚀 Future Improvements

Multi-resume batch processing

Recruiter dashboard

PDF resume export with AI suggestions

Deployment on Streamlit Cloud

Interview question generation

📌 Project Goal

This project demonstrates real-world applications of:

NLP

Semantic Search

Vector Similarity

LLM Reasoning

End-to-end ML App Development

Built as part of my journey transitioning into Data Science & Artificial Intelligence.

If you’d like next, I can help with:

✅ Architecture diagram
✅ Resume bullet points
✅ LinkedIn project description
✅ Interview explanation
✅ Streamlit Cloud deployment steps

Just say 👍
