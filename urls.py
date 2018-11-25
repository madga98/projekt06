from django.urls import path

from .views import HomePageView, AboutPageView, MojePageView

urlpatterns = [
    path('moje/', MojePageView.as_view(), name='moje'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
