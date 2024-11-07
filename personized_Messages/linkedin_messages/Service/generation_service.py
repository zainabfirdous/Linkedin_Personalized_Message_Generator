from linkedin_messages.Data.targetProfileDetails import targetProfileDetails
from .openai_service import generate_message

def messageGeneration(data):
    try:
        user = targetProfileDetails.objects.filter(name=str(data)).values('name','location','posts')
        details = (list(user))
        message = [
            {
                "role":"system",
                "content":"You are a professional networker, an expert in cultivating and expanding client's network/professional relationships."
            },
            {
                "role":"user",
                "content":f"I want to connect with {details[0]['name']} who lives in {details[0]['location']} and their recent posts are {details[0]['posts']} to expand by network."
            },
            {
                "role":"system",
                "content": "Create a 2 line connect message tailored for the user that will catch the other party's attention"
            }
        ]

        response = generate_message(message)
        return response
    except Exception as e:
        raise e
