from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from linkedin_messages.Service.generation_service import messageGeneration

@api_view(['GET'])
def generateMsg(request):
    try:
        name = request.GET.get("name", None)
        result = messageGeneration(name)
        response = Response({result}, status=status.HTTP_200_OK)
        return response
    except Exception as e:
        return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)