from django import forms

class ResumeUploadForm(forms.Form):
    resume = forms.FileField(
        label='Upload your resume (PDF or DOCX)',
        help_text='Supported formats: .pdf, .docx'
    )

    def clean_resume(self):
        file = self.cleaned_data['resume']
        ext = file.name.split('.')[-1].lower()
        if ext not in ('pdf', 'docx'):
            raise forms.ValidationError('Only PDF and DOCX files are supported.')
        if file.size > 5 * 1024 * 1024:
            raise forms.ValidationError('File size must be under 5MB.')
        return file
