from django import forms
from assessment.models import Attachment

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ('title', 'document', )