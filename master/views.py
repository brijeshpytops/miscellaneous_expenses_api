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
    try:
        querySet = TaksModel.objects.get(id=task_id)
    except TaksModel.DoesNotExist:
        return Response({
            'message':'Data not found'
        }, status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            serializers= TaksSerializers(querySet)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        
        if request.method == 'PUT':
            serializers = TaksSerializers(querySet, data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
            else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
            
        if request.method == 'PATCH':
            serializers = TaksSerializers(querySet, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
            else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


        if request.method == 'DELETE':
            querySet.delete()
            return Response({'message':"Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
