from flask import Flask, render_template, request
import os
import re
import joblib
import pdfplumber
from docx import Document

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load Saved Model
model = joblib.load("resume_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Resume Cleaning Function
def clean_resume(text):

    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"www\S+", " ", text)
    text = re.sub(r"RT|cc", " ", text)
    text = re.sub(r"#\S+", " ", text)
    text = re.sub(r"@\S+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.lower()


# PDF Reader
def extract_text_from_pdf(filepath):

    text = ""

    with pdfplumber.open(filepath) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text

# DOCX Reader
def extract_text_from_docx(filepath):

    doc = Document(filepath)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text

SKILLS = [
    "Python", "Java", "C", "C++", "SQL", "MySQL",
    "Machine Learning", "Deep Learning", "Artificial Intelligence",
    "Data Science", "NLP", "TensorFlow", "Keras", "PyTorch",
    "Scikit-learn", "Pandas", "NumPy", "Flask", "Django",
    "Power BI", "Tableau", "Excel", "Git", "GitHub",
    "Docker", "AWS", "Azure", "GCP", "Spark", "Hadoop",
    "Selenium", "Playwright", "Postman", "Rest Assured",
    "JUnit", "Jira", "HTML", "CSS", "JavaScript", "React"
]
def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))

# Home Page
@app.route("/")
def home():

    return render_template("resume1.html")

# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    print("Predict function called")

    file = request.files["resume"]
    print("File:", file.filename)

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)
    print("File saved")

    extension = os.path.splitext(file.filename)[1].lower()
    print("Extension:", extension)

    if extension == ".pdf":
        resume_text = extract_text_from_pdf(filepath)
    elif extension == ".docx":
        resume_text = extract_text_from_docx(filepath)
    else:
        return "Only PDF and DOCX files are supported."

    print("Text extracted")

    cleaned_resume = clean_resume(resume_text)
    print("Text cleaned")

    resume_vector = tfidf.transform([cleaned_resume])
    print("Vector created")

    prediction = model.predict(resume_vector)
    print("Prediction:", prediction)

    predicted_role = label_encoder.inverse_transform(prediction)[0]
    print("Role:", predicted_role)

    confidence = round(max(model.predict_proba(resume_vector)[0]) * 100, 2)

    skills = extract_skills(resume_text)

    return render_template(
        "resume2.html",
        filename=file.filename,
        prediction=predicted_role,
        confidence=confidence,
        skills=skills
    )

# Run Flask
if __name__ == "__main__":

    app.run(debug=True)
