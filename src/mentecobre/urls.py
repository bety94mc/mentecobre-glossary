from django.urls import path

from .views import base

urlpatterns = [
    path('glosario', base.GlossaryView.as_view(), name='glossary'),

]
