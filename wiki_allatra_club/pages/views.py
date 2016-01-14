from django.core.mail import send_mail
from django.views.generic import FormView, TemplateView

from .forms import ContactForm


class BaseViewMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BaseViewMixin,
                        self).get_context_data(**kwargs)
        context["request"] = self.request
        return context


class ContactView(BaseViewMixin, FormView):
    form_class = ContactForm
    template_name = "pages/contact_us.html"
    success_url = '/thanks/'
    # TODO: transfer parameters to settings
    def form_valid(self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))

        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            from_email='wiki.allatra.club@gmail.com',
            # recipient_list=[Production.LIST_OF_EMAIL_RECIPIENTS],
            recipient_list=['sergiykhalimon@gmail.com'],
        )
        return super(ContactView, self).form_valid(form)


class ThanksView(BaseViewMixin, TemplateView):
    template_name = "pages/thanks.html"


class ChronologyView(BaseViewMixin, TemplateView):
    template_name = "pages/chronology_view.html"
