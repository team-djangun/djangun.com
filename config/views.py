from django.views.generic import TemplateView


class WelcomeView(TemplateView):
    template_name = "pages/welcome.html"


welcome_view = WelcomeView.as_view()
