from django.views.generic import TemplateView
# Create your views here.


class HomePage(TemplateView):
    """
    Home Page
    """
    template_name = "index.html"