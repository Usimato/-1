from django.urls import path

from blog.views import home_view

urlpatterns = [
    path("", home_view)
]
