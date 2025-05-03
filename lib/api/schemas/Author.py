from pydantic import BaseModel


class Author(BaseModel):
    """
    Author schema.
    """

    id: int
    name: str
    created_at: int

    class Config:
        orm_mode = True
