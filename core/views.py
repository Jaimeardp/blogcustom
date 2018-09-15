from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kargs):
        return render(request, self.template_name,{'title':'Mi super blog'})


class SampleView(TemplateView):
    template_name = "core/sample.html"
