from pydantic import BaseModel


class ExpenseBase(BaseModel):
    group_id: int
    user_id: int
    amount: float
    description: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ExpenseCreate(ExpenseBase):
    pass


class Expense(ExpenseBase):
    id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
