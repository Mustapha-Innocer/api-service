from pydantic import BaseModel


class Category(BaseModel):
    """
    Category schema.
    """

    id: int
    name: str
    created_at: int

    class Config:
        orm_mode = True
