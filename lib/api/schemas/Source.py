from pydantic import BaseModel


class Source(BaseModel):
    """
    Source schema.
    """

    name: str
    country: str
    country_code: str

    class Config:
        from_attributes = True
