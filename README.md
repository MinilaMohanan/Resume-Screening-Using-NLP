# Resume-Screening-Using-NLP
Resume Screening Using NLP &amp; Machine Learning – A Flask-based web application that predicts the most suitable job role from uploaded resumes using TF-IDF and a KNN classifier. Supports PDF/DOCX upload, resume text extraction, skill detection, and an interactive HTML/CSS interface.

# Resume Screening Using NLP & Machine Learning

## 📌 Overview

Resume Screening Using NLP & Machine Learning is an end-to-end web application that predicts the most suitable job role based on the content of an uploaded resume. The application uses Natural Language Processing (NLP) techniques for text preprocessing and a Machine Learning model trained on resume data to classify resumes into different job categories. The system also extracts relevant technical skills from the uploaded resume and presents the prediction through a simple and responsive web interface.

---

## 🚀 Features

- Upload resumes in **PDF** or **DOCX** format
- Extract text from resumes
- Clean and preprocess resume text using NLP
- Predict the most suitable job role using Machine Learning
- Display prediction confidence score
- Automatically extract technical skills from resumes
- Modern and responsive Flask web interface

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Scikit-learn
- Pandas
- NumPy
- NLTK
- PDFPlumber
- python-docx
- Joblib

---

## 📂 Project Structure

```
Resume-Screening/
│
├── app.py
├── resume_model.pkl
├── tfidf_vectorizer.pkl
├── label_encoder.pkl
├── skills.py
├── uploads/
├── templates/
│   ├── index.html
│   └── result.html
├── static/
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/Resume-Screening.git
```

2. Navigate to the project folder

```bash
cd Resume-Screening
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

4. Run the Flask application

```bash
python app.py
```

5. Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📊 Workflow

1. Upload a resume (PDF/DOCX).
2. Extract text from the uploaded resume.
3. Preprocess the text using NLP.
4. Convert the text into TF-IDF features.
5. Predict the most suitable job role using the trained model.
6. Display the predicted role, confidence score, and extracted skills.

---

## 🎯 Predicted Job Roles

The model is trained to classify resumes into the following roles:

- Java Developer
- Python Developer
- Data Science
- Web Designing
- Testing
- Automation Testing
- DevOps Engineer
- ETL Developer
- SAP Developer
- DotNet Developer
- Database
- Business Analyst
- HR
- Sales
- Operations Manager
- Blockchain
- Hadoop
- Network Security Engineer
- Mechanical Engineer
- Electrical Engineering
- Civil Engineer
- PMO
- Health and Fitness
- Arts
- Advocate

---

## 📸 Screenshots

### Home Page
Upload your resume for analysis.

### Result Page
Displays:
- Predicted Job Role
- Confidence Score
- Extracted Skills
- Resume Status

---

## 🔮 Future Enhancements

- Resume ranking based on job descriptions
- Job recommendation system
- ATS compatibility score
- Skill gap analysis
- Resume improvement suggestions
- Candidate profile dashboard
- Cloud deployment (Render/AWS/Azure)

---

## 👨‍💻 Author

**Minila K M**

M.Sc. Data Science & Analytics

Python | Machine Learning | Data Science | QA Automation

---

## 📄 License

This project is intended for educational and learning purposes.
