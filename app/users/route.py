from app.db.database import get_db 
from app.core.security import get_current_user
from fastapi import APIRouter , Depends
from app.users.service import UserService
from app.users.repo import UserRepository
user_router = APIRouter()
def get_repo(db = Depends(get_db)):
    return UserRepository(db)
def get_service(repo=Depends(get_repo),db=Depends(get_db)):
    return UserService(repo,db)

@user_router.get("/profile")
def get_user(service=Depends(get_service),user=Depends(get_current_user)):
    return user 

