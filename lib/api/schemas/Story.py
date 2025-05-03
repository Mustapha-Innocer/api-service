from pydantic import BaseModel


class Story(BaseModel):
    """
    Story schema.
    """

    id: int
    source_id: int
    category_id: int
    author_id: int
    url: str
    title: str
    body: str
    image_url: str
    summary: str
    published_at: int
    created_at: int

    class Config:
        orm_mode = True
