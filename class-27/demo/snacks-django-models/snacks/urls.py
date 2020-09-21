from django.urls import path
from .views import HomeView, SnacksView, SnackDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('snacks', SnacksView.as_view(), name='snacks'),
    path('snacks/<int:pk>', SnackDetailsView.as_view(), name='snack_details'),
]
