import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Job

SKILL_PATTERNS = {
    'python': r'\bpython\b',
    'java': r'\bjava\b',
    'javascript': r'\bjavascript\b',
    'c++': r'\bc\+\+\b',
    'c#': r'\bc\#\b',
    'typescript': r'\btypescript\b',
    'go': r'\bgo\b',
    'rust': r'\brust\b',
    'sql': r'\bsql\b',
    'html': r'\bhtml\b',
    'css': r'\bcss\b',
    'react': r'\breact\b',
    'angular': r'\bangular\b',
    'node.js': r'\bnode\.?(js)?\b',
    'django': r'\bdjango\b',
    'flask': r'\bflask\b',
    'spring': r'\bspring\b',
    'aws': r'\baws\b',
    'azure': r'\bazure\b',
    'docker': r'\bdocker\b',
    'kubernetes': r'\bkubernetes\b',
    'git': r'\bgit\b',
    'linux': r'\blinux\b',
    'excel': r'\bexcel\b',
    'tableau': r'\btableau\b',
    'pandas': r'\bpandas\b',
    'machine learning': r'\bmachine learning\b',
    'deep learning': r'\bdeep learning\b',
    'tensorflow': r'\btensorflow\b',
    'rest api': r'\brest api\b',
    'power bi': r'\bpower bi\b',
}

class SkillMatcher:
    def __init__(self):
        self.rows = list(Job.objects.all())

        job_texts = []
        self.job_titles = []
        for r in self.rows:
            skills = r.skills_str.strip().lower()
            if skills:
                skills = skills.replace(', ', '|').replace(',', '|')
                job_texts.append(skills)
                self.job_titles.append(f"{r.job_title} @ {r.company}")

        self.vectorizer = CountVectorizer(binary=True, token_pattern=r'[^|]+')
        self.X = self.vectorizer.fit_transform(job_texts)

    def extract_skills(self, text):
        text_lower = text.lower()
        found = []
        for skill_name, pattern in SKILL_PATTERNS.items():
            if re.search(pattern, text_lower):
                found.append(skill_name)
        return ', '.join(found)

    def match(self, text):
        skills_str = self.extract_skills(text)
        if not skills_str:
            return [], skills_str

        processed = skills_str.replace(', ', '|').replace(',', '|')
        vec = self.vectorizer.transform([processed])
        sims = cosine_similarity(vec, self.X).flatten()
        top_idx = np.argsort(sims)[::-1][:10]

        results = []
        for idx in top_idx:
            if sims[idx] > 0:
                r = self.rows[idx]
                results.append({
                    'title': r.job_title,
                    'company': r.company,
                    'score': round(float(sims[idx]), 4),
                    'required_skills': r.skills_str,
                })
        return results, skills_str
