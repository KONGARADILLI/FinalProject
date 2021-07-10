from django import forms
from OnlinejobportalApp.models import Apply

class AplForm(forms.ModelForm):
	class Meta:
		model = Apply
		fields = ["student_resumes"]