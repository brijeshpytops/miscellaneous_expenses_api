from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TaksModel
from .serializers import TaksSerializers

@api_view(['GET', 'POST'])
def taskListAPI(request):
    if request.method == 'GET':
        querySet = TaksModel.objects.all()
        serializers= TaksSerializers(querySet, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializers = TaksSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def taskDetailAPI(request, task_id):
    pass
