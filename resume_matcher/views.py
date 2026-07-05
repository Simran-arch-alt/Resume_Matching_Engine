import PyPDF2
import docx
from django.shortcuts import render
from .forms import ResumeUploadForm
from .skill_matcher import SkillMatcher

matcher = SkillMatcher()

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return ' '.join(page.extract_text() or '' for page in reader.pages)

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return ' '.join(para.text for para in doc.paragraphs)

def upload_resume(request):
    results = None
    extracted_skills = None
    error = None

    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['resume']
            ext = file.name.split('.')[-1].lower()
            try:
                if ext == 'pdf':
                    text = extract_text_from_pdf(file)
                else:
                    text = extract_text_from_docx(file)
                results, extracted_skills = matcher.match(text)
                if not results:
                    error = 'No matching skills found in your resume.'
            except Exception as e:
                error = f'Error processing file: {e}'
    else:
        form = ResumeUploadForm()

    return render(request, 'resume_matcher/upload.html', {
        'form': form,
        'results': results,
        'extracted_skills': extracted_skills,
        'error': error,
    })
