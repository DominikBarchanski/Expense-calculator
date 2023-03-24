from pydantic import BaseModel


class UserGroupMembershipBase(BaseModel):
    user_id: int
    group_id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserGroupMembershipCreate(UserGroupMembershipBase):
    pass


class UserGroupMembership(UserGroupMembershipBase):
    id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
