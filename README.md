# Resume Matching Engine

An AI-powered Resume Matching Engine built with **Python** and **Django** to analyze how well a candidate's resume matches a job description. The system uses **Cosine Similarity** and Natural Language Processing (NLP) techniques to calculate a matching score, making the recruitment process faster and more objective.

---

## Features

* Upload and process candidate resumes.
* Compare resumes against job descriptions.
* Calculate similarity scores using Cosine Similarity.
* Analyze candidate skills from resumes.
* Store and manage data using Django.
* Docker support for easy deployment.

---

## Technologies Used

* Python
* Django
* Scikit-learn
* Pandas
* NumPy
* Cosine Similarity (TF-IDF Vectorization)
* SQLite
* Docker

---

## Project Structure

```text
Resume_Matching_Engine/
│
├── config/                         # Django project configuration
├── resume_matcher/                 # Resume matching application
├── Dockerfile                      # Docker configuration
├── requirements.txt                # Python dependencies
├── manage.py                       # Django management script
├── db.sqlite3                      # SQLite database
├── jobs_dataset_skills_final.csv   # Job skills dataset
├── dummy_cv.docx                   # Sample resume
├── cosine_similarity_example.py    # Cosine similarity implementation
├── README.md
└── LICENSE
```

---

## How the Matching Engine Works

1. Upload a candidate's resume.
2. Extract the text from the resume.
3. Preprocess the resume and job description.
4. Convert the text into TF-IDF vectors.
5. Calculate Cosine Similarity between the resume and job description.
6. Generate a similarity score that indicates how well the resume matches the job requirements.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Simran-arch-alt/Resume_Matching_Engine.git
cd Resume_Matching_Engine
```

### Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Django Server

```bash
python manage.py migrate
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

---

## Docker

Build the Docker image:

```bash
docker build -t resume-matching-engine .
```

Run the container:

```bash
docker run -p 8000:8000 resume-matching-engine
```

---

## Dataset

The project includes a sample dataset:

* `jobs_dataset_skills_final.csv`

This dataset is used to compare candidate skills with job requirements and calculate matching scores.

---

## Future Improvements

* Resume upload interface.
* PDF and DOCX resume parsing.
* Skill gap analysis.
* Personalized learning recommendations.
* Job recommendation engine.
* MongoDB integration.
* Frontend using React or Flutter.
* REST API for external applications.

---

## License

This project is licensed under the MIT License.

---

## Author

**Simran Karmacharya**

Bachelor of Computer Science (Hons)

AI & Resume Matching Engine Project


