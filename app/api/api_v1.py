from fastapi import APIRouter

from app.api.endpoints import users, userGroup, addUserToGroup

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(userGroup.router, prefix="/userGroup", tags=["userGroup"])
api_router.include_router(addUserToGroup.router, prefix="/addUserToGroup", tags=["addUserToGroup"])