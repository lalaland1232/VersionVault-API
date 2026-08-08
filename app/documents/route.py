from fastapi import APIRouter,Depends
from app.documents.repo import DocumentRepository
from app.documents.service import DocumentService
from app.db.database import get_db
from app.core.security import get_current_user
from app.core.dependencies import CreateDocument,UpdateDocument,UpdateDocumentName
document_router = APIRouter()
def get_repo(db=Depends(get_db)):
    return DocumentRepository(db)

def get_service(repo=Depends(get_repo),db=Depends(get_db)):
    return DocumentService(repo,db)
@document_router.post("/create_document")
def create_document(request:CreateDocument,user=Depends(get_current_user),service=Depends(get_service)):
    service.create_document(user.user_id,request)

@document_router.get("/documents")
def get_documents(user=Depends(get_current_user),service=Depends(get_service)):
    return service.get_documents(user.user_id)

@document_router.get("/documents/{document_id}")
def get_document(document_id:int,user=Depends(get_current_user),service=Depends(get_service)):
    print(f"Fetching document with ID: {document_id} for user: {user.user_id}")
    return service.get_document(document_id,user.user_id)

@document_router.post("/documents/{document_id}/update_content")
def update_document(document_id:int,request:UpdateDocument,user=Depends(get_current_user),service=Depends(get_service)):
     service.update_document(document_id,user.user_id,request)

@document_router.post("/documents/{document_id}/update_name")
def update_document_name(document_id:int,request:UpdateDocumentName,user=Depends(get_current_user),service=Depends(get_service)):
    service.update_document_name(user.user_id,document_id,request.document_name)

@document_router.get("/documents/{document_id}/versions")
def get_versions(document_id:int,user=Depends(get_current_user),service=Depends(get_service)):
    return service.get_versions(document_id,user.user_id)

@document_router.post("/documents/{document_id}/restore_version/{version_number}")
def restore_version(document_id:int,version_number:int,user=Depends(get_current_user),service=Depends(get_service)):
    service.restore_version(document_id,version_number,user.user_id)

@document_router.delete("/documents/{document_id}")
def delete_document(document_id:int,user=Depends(get_current_user),service=Depends(get_service)):
    service.delete_document(document_id,user.user_id)
