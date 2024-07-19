from django.urls import path

from .views import about_us_view

urlpatterns = [
    path('aboutus/', about_us_view, name='aboutus'),

]
