from fastapi import APIRouter

from app.api.endpoints import users, userGroup, addUserToGroup, Balance, productList ,  productCategories

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(userGroup.router, prefix="/userGroup", tags=["userGroup"])
api_router.include_router(addUserToGroup.router, prefix="/addUserToGroup", tags=["addUserToGroup"])
api_router.include_router(Balance.router, prefix="/balance", tags=["balance"])
api_router.include_router(productList.router, prefix="/productList", tags=["productList"])
api_router.include_router(productCategories.router, prefix="/productCategories", tags=["productCategories"])

