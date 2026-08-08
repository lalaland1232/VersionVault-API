from fastapi import FastAPI
from app.refresh.route import refresh_router
from app.documents.route import document_router
from app.signup.route import signup_router
from app.login.route import login_router
from app.users.route import user_router
app = FastAPI()
app.include_router(signup_router)
app.include_router(login_router)
app.include_router(refresh_router)
app.include_router(user_router)
app.include_router(document_router)
