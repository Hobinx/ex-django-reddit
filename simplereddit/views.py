from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'simplereddit/test.html'


class ThanksPage(TemplateView):
    template_name = 'simplereddit/thanks.html'


class HomePage(TemplateView):
    template_name = 'simplereddit/index.html'
