from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('landing/',TemplateView.as_view(template_name="index.html")),
]