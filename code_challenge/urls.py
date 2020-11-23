from django.urls import include, path
from django.views.generic.base import RedirectView


urlpatterns = [
    path('word_count/', include('word_count.urls')),
    path('', RedirectView.as_view(pattern_name='word_count:word_count'), name='home'),
]
