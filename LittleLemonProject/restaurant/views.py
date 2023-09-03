from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class BookingView(APIView):

    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)
    
