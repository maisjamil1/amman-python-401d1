from django.urls import path
from .views import SnacksView, SnackDetailsView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('snacks-list', SnacksView.as_view(), name='snacks'),
    path('snack/<int:pk>', SnackDetailsView.as_view(), name='snack_details'),
    path('snack/new', SnackCreateView.as_view(), name='snack_create'),
    path('snack/<int:pk>/update', SnackUpdateView.as_view(), name='snack_update'),
    path('snack/<int:pk>/delete', SnackDeleteView.as_view(), name='snack_delete'),


]



# snack/2/update
