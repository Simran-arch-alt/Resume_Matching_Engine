import csv
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#with open ensures the file is closed after reading
with open('jobs_dataset_skills_final.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

#preprocessing job data
job_texts = []
job_titles = []
for r in rows:
    skills = r['skills_str'].strip().lower()
    if skills:
        skills = skills.replace(', ', '|').replace(',', '|')
        job_texts.append(skills)
        job_titles.append(f"{r['job_title']} @ {r['company']}")

# Vectorization turning text into math
vectorizer = CountVectorizer(binary=True, token_pattern=r'[^|]+')
X = vectorizer.fit_transform(job_texts)
all_skills = vectorizer.get_feature_names_out()
print(f"Skill vocabulary size: {len(all_skills)}")
print(f"Vocabulary: {', '.join(all_skills)}")
print(f"Total jobs indexed: {X.shape[0]}\n")

student_raw = "python, sql, machine learning, pandas, aws, git, docker"
student_processed = student_raw.strip().lower().replace(', ', '|').replace(',', '|')
student_vec = vectorizer.transform([student_processed])
sims = cosine_similarity(student_vec, X).flatten()
top_idx = np.argsort(sims)[::-1][:10]

print(f"Student skills: {student_raw}\n")
print(f"{'Rank':<5} {'Score':<10} {'Job Title':<60} {'Skills'}")
print("-" * 140)
seen = set()
rank = 0
for idx in top_idx:
    if rank >= 10:
        break
    score = sims[idx]
    title = job_titles[idx][:59]
    skills = rows[idx]['skills_str'][:65]
    if title not in seen:
        rank += 1
        seen.add(title)
        print(f"{rank:<5} {score:<10.4f} {title:<60} {skills}")

print(f"\n--- Gap Analysis (Top Match) ---")
top_idx_real = top_idx[0]
job_skills = set(s.strip().lower() for s in rows[top_idx_real]['skills_str'].split(','))
student_set = set(s.strip().lower() for s in student_raw.split(','))
missing = sorted(job_skills - student_set)
matched = sorted(student_set & job_skills)
print(f"Job: '{rows[top_idx_real]['job_title']}' @ {rows[top_idx_real]['company']}")
print(f"  Your skills: {', '.join(sorted(student_set))}")
print(f"  Matched:     {', '.join(matched)}")
print(f"  Missing:     {', '.join(missing) if missing else 'None - full match!'}")
