from django.urls import path
from app_01.views.home_page import home_page

urlpatterns = [
    path("", home_page, name="home_page"),
]
