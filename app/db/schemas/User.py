from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str

    class Config:
        arbitrary_types_allowed = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str