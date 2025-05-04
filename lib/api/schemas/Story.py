from datetime import datetime

from pydantic import BaseModel, field_validator


class Story(BaseModel):
    """
    Story schema.
    """

    url: str
    title: str
    body: str
    image_url: str
    summary: str
    published_at: datetime
    created_at: datetime
    source: str
    category: str
    author: str

    class Config:
        from_attributes = True

    @field_validator("source", "category", "author", mode="before")
    @classmethod
    def get_name(cls, value):
        """
        Get the source name from the source.
        """
        if value is not None:
            return value.name

    @field_validator("published_at", "created_at", mode="before")
    @classmethod
    def convert_timestamp(cls, value):
        """
        Convert the timestamp to a datetime object.
        """
        if value is not None:
            return datetime.fromtimestamp(value)
