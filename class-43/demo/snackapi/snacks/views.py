from rest_framework.generics import ListCreateAPIView

from .models import Snack
from .serializers import SnackSerializer

class SnackList(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
