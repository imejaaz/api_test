from rest_framework import views
from rest_framework.response import Response
from .models import Data
from rest_framework import status

class TextDataApiView(views.APIView):

    def get(self, request):
        return Response({'message': 'Get request received'})

    def post(self, request):

        title=request.data.get('title')
        text=request.data.get('text')

        if len(text) > 2000:
            return Response({'message':'Your text is exceeding then 2000 characters.'},  status=status.HTTP_400_BAD_REQUEST)

        Data.objects.create(Title=title, Text=text)
        return Response({'message':'Data have been stored'}, status=status.HTTP_201_CREATED)