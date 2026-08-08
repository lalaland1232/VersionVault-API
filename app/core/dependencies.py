from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

class SignUpRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class CreateDocument(BaseModel):
    document_name: str
    content:str

class GetDocument(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    document_name: str
    content: str
    created_at: datetime
    last_updated_at: datetime
    current_version: int

class UpdateDocument(BaseModel):
    content: str

class UpdateDocumentName(BaseModel):
    document_name: str