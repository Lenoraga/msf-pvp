from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Tournament
from .serializers import *


class TournamentsView(APIView):

    def get(self, request):
        query = Tournament.objects

        tournaments = query.all()
        total_amount = query.count()

        serializer = TournamentListSerializer({'total_amount': total_amount, 'tournaments': tournaments})
        return Response(serializer.data, status=status.HTTP_200_OK)
