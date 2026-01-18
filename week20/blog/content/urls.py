from django.urls import path
from content.views import home_page

urlpatterns = [
    path("hello", home_page, name="index.page")
]