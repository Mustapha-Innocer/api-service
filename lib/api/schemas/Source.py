from pydantic import BaseModel


class Source(BaseModel):
    """
    Source schema.
    """

    id: int
    name: str
    country: str
    country_code: str
    created_at: int

    class Config:
        orm_mode = True
