from datetime import date
from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Article

class CreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-Form'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))
    

    class Meta:
        model = Article
        fields = [
            'name',
            'content',
            'image',
            'category',
            'draft',
            'publish_date',
        ]

    def clean_publish_date(self):
        data = self.cleaned_data['publish_date']
        if data < date.today():
            raise forms.ValidationError(
                _("Publish date cannot be in the past.")
            )
        return data