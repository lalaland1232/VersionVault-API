from app.core.dependencies import GetDocument
from datetime import datetime,timezone
class DocumentService:
    def __init__(self,repo,db):
        self.repo = repo
        self.db = db
    def create_document(self,user_id,request):
        try:
            earlier_doc = self.repo.get_document_by_name(request.document_name,user_id)
            if earlier_doc:
                raise ValueError("Document with this name already exists")
            document=self.repo.create_document(user_id,request)
            self.db.flush()
            self.repo.create_document_version_one(document,request.content)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def get_documents(self,user_id):
        return self.repo.get_documents(user_id)

    def get_document(self,document_id,user_id):
    
            document=self.repo.get_document(user_id,document_id)
            if document is None:
                raise Exception("Document not found")
            content=self.repo.get_latest_version(document_id).content
            response = GetDocument(
                document_name=document.document_name,
                content=content,
                created_at=document.created_at,
                last_updated_at=document.updated_at,
                current_version=document.current_version
            )
            return response
    def update_document(self,document_id,user_id,request):
        document= self.repo.get_document(user_id,document_id)
        if document is None:
            raise Exception("Document not found")
        try:
            self.repo.create_document_version(document,request.content)
            document.current_version += 1
            document.updated_at = datetime.now(timezone.utc)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def update_document_name(self,user_id,document_id,new_name):
        document= self.repo.get_document(user_id,document_id)
        if document is None:
            raise Exception("Document not found")
        try:
            document.document_name = new_name
            document.updated_at = datetime.now(timezone.utc)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
    def get_versions(self,document_id,user_id):
        document= self.repo.get_document(user_id,document_id)
        if document is None:
            raise Exception("Document not found")
        document_versions=self.repo.get_versions(document_id)
        return document_versions
    def restore_version(self,document_id,version_number,user_id):
        doc= self.repo.get_document(user_id,document_id)
        if doc is None:
            raise Exception("Document not found")
        restored_version=self.repo.get_document_version_from_version_number(document_id,version_number)
        if  restored_version is None:
            raise Exception("Document  version not found")
        try:
            self.repo.create_document_version(doc,restored_version.content)
            doc.current_version += 1
            doc.updated_at = datetime.now(timezone.utc)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
    def delete_document(self,document_id,user_id):
        document= self.repo.get_document(user_id,document_id)
        if document is None:
            raise Exception("Document not found")
        try:
            self.db.delete(document)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e