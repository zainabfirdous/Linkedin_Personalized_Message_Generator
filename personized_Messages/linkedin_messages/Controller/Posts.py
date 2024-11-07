from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from linkedin_messages.Validation.linkedinDetails import validate_linkedin_details
from linkedin_messages.Service.posts_service import scrape_details
from pydantic import ValidationError

@api_view(['POST'])
def get_posts(request):
    try:
        print(request.data)
        valid_data = validate_linkedin_details(request.data)
        result = scrape_details(valid_data)
        print(result)
        response = Response({"details":result},status=status.HTTP_200_OK)
        return response
    except ValidationError as e:
        return Response({"error":str(e.errors())},status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
