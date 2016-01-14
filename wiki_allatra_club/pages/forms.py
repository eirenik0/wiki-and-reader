from captcha.fields import ReCaptchaField  # Only import different from yesterday
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Div

import floppyforms as forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name ', required=True)
    email = forms.EmailField(label='Email ', required=True)
    subject = forms.CharField(label='Subject ', required=True)
    message = forms.CharField(label='Message ', widget=forms.Textarea)
    captcha = ReCaptchaField()  # Only field different from yesterday

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('reset', 'Reset'))
        super(ContactForm, self).__init__(*args, **kwargs)
