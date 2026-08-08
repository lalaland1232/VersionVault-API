from app.db.models import Document,DocumentVersion
class DocumentRepository:
    def __init__(self,db):
        self.db = db
    def create_document(self,user_id,request):
        new_document = Document(
            user_id=user_id,
            document_name=request.document_name
        )

        self.db.add(new_document)
        return new_document
    def create_document_version_one(self,document,content):
        document_version= DocumentVersion(
                document_id=document.document_id,
                version_number=1,
                content=content
        )
        self.db.add(document_version)
    def create_document_version(self,document,content):
        
        document_version= DocumentVersion(
                document_id=document.document_id,
                version_number=document.current_version+1,
                content=content
        )
        self.db.add(document_version)

    def get_documents(self,user_id):
        return self.db.query(Document).filter(Document.user_id==user_id).all()

    def get_document(self,user_id,document_id):
        return self.db.query(Document).filter(Document.user_id==user_id,Document.document_id==document_id).first()

    def get_latest_version(self,document_id):
        return self.db.query(DocumentVersion).filter(DocumentVersion.document_id==document_id).order_by(DocumentVersion.version_number.desc()).first()
    def get_versions(self,document_id):
        return self.db.query(DocumentVersion).filter(DocumentVersion.document_id==document_id).order_by(DocumentVersion.version_number).all()

    def get_document_version_from_version_number(self,document_id,version_number):
        return self.db.query(DocumentVersion).filter(DocumentVersion.document_id==document_id,DocumentVersion.version_number==version_number).first()

    def get_document_by_name(self,document_name,user_id):
        return self.db.query(Document).filter(Document.document_name==document_name,Document.user_id==user_id).first()