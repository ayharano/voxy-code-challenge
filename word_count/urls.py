from django.urls import path

from . import views


app_name = 'word_count'

urlpatterns = [
    path('', views.word_count, name='word_count'),
]
