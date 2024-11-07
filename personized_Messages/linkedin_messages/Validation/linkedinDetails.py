from pydantic import BaseModel, AnyUrl

class linkedinDetails(BaseModel):
    username:str
    password:str
    profileUrl: AnyUrl

def validate_linkedin_details(payload):
    result = linkedinDetails(**payload)
    return result