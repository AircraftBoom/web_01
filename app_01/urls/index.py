from django.urls import path
from app_01.views.index import home_page

urlpatterns = [
    path("", home_page, name="home_page"),
]
